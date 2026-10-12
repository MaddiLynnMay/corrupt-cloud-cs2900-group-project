import sqlite3

class DB_Controler():
    def __init__(self, database):
        self.db = database
        self.queries = {
            "all users": "SELECT ID FROM User WHERE name = 'Aragorn';"
        }

    def run_query(self, query):
        """Takes a query or a query key from the controler dictionary
        and returns the results of that query ran against the
        database"""
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

        if query in self.queries.keys():
            results = cursor.execute(self.queries[query])
        else:
            try:
                results = cursor.execute(query)
            except:
                cursor.close()
                conn.close()
                print("Bad Query")
                return -1
        
        out = [r for r in results]

        # For now I just have it closing the connection between each
        # query, and reopening it as needed.
        cursor.close()
        conn.close()

        return out
    
        


def main():
    dbc = DB_Controler("dummy_bank.db")

    query = "SELECT name FROM User;"

    results = dbc.run_query("all users")
    if type(results) == list:
        for row in results:
            print(row)



if __name__ == "__main__":
    main()