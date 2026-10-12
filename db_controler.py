import sqlite3

class DB_Controler():
    def __init__(self, database):
        self.db = database


    def run_query(self, query):
        """Takes a query and returns the results of that query ran 
        against the database"""
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

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

    ## All queries
    def all_users(self):
        """returns all users in the User table"""
        return self.run_query("all users")

    def user_accounts(self, userID):
        """Returns account names associated with a given userID"""
        query = f"""
            -- Get all account names for a given user's ID
            SELECT u.name, a.acc_name
            FROM Account a
            JOIN User u ON u.ID = a.userID
            WHERE u.ID = '{userID}';
            """
        return self.run_query(query)
    
    def specific_account(self, account_name):
        """Returns an account given its name or ID"""
        try:
            query = f"""
                -- get an account by it's ID
                SELECT *
                FROM Account
                WHERE ID = {int(account_name)};
                """
        except:
            query = f"""
                -- get an account by it's name
                SELECT *
                FROM Account
                WHERE acc_name = '{account_name}';
                """
        return self.run_query(query)

    def account_balance(self, account_name):
        """Returns account balance given the account name or ID"""
        try:
            query = f"""
                -- Account balance by accountID
                SELECT acc_name, balance
                FROM Account
                WHERE ID = {int(account_name)};
                """
        except:
            query = f"""
                -- Account balance by account name
                SELECT acc_name, balance
                FROM Account
                WHERE acc_name = '{account_name}';
                """
        return self.run_query(query)

    def acc_transactions(self, acc_name):
        """Returns all transactions on a given account given the
        account name or ID"""
        try:
            query = f"""
                -- All transactions on given Account by account ID
                SELECT a.acc_name, t.*
                FROM AccTransaction t
                JOIN Account a ON a.ID = t.accountID
                JOIN User u ON u.ID = a.userID
                WHERE a.ID = {int(acc_name)}
                ORDER BY date DESC;
                """
        except:
            query = f"""
                -- All transactions on given Account by account name
                SELECT a.acc_name, t.*
                FROM AccTransaction t
                JOIN Account a ON a.ID = t.accountID
                JOIN User u ON u.ID = a.userID
                WHERE a.acc_name = "{acc_name}"
                ORDER BY date DESC;
                """
        return self.run_query(query)
    
    def acc_transactions_limit(self, acc_name, limit):
        """Returns most recent transactions on given account by name
        or ID, limiting results to given limit"""
        try:
            query = f"""
                -- Recent 5 transactions on given Account by account ID
                SELECT a.acc_name, t.*
                FROM AccTransaction t
                JOIN Account a ON a.ID = t.accountID
                JOIN User u ON u.ID = a.userID
                WHERE a.ID = {int(acc_name)}
                ORDER BY date DESC
                LIMIT {limit};
                """
        except:
            query = f"""
                -- Most recent transactions on given Account
                SELECT a.acc_name, t.*
                FROM AccTransaction t
                JOIN Account a ON a.ID = t.accountID
                JOIN User u ON u.ID = a.userID
                WHERE a.acc_name = "{acc_name}"
                ORDER BY date DESC
                LIMIT {limit};
                """
        return self.run_query(query)
    
    def user_total_balance(self, user):
        """Returns total balance across a given user's accounts by
        user name or ID"""
        try:
            query = f"""
                -- Sum of all account balances by user ID
                SELECT u.name, SUM(a.balance) AS "user_balance"
                FROM User u
                JOIN Account a ON a.userID = u.ID
                WHERE u.ID = {int(user)}
                GROUP BY u.ID;
                """
        except:
            query = f"""
                -- Sum of account balances by user
                SELECT u.name, SUM(a.balance) AS "user_balance"
                FROM User u
                JOIN Account a ON a.userID = u.ID
                WHERE u.name = "{user}"
                GROUP BY u.ID;
                """
        return self.run_query(query)
    
    def user_by_username_pword(self, username, p_word):
        """Returns user if username and p_word match"""
        print(f"Getting user with username: '{username}', and p_word: '{p_word}'")
        query = f"""
            -- Get user by username and password
            SELECT *
            FROM User
            WHERE username = '{username}' AND p_word = '{p_word}';
            """
        return self.run_query(query)
        
        


def main():
    dbc = DB_Controler("dummy_bank.db")

    # query = "SELECT name FROM User;"
    #"""
    uname = "TheWhiteWizard"
    pword = "Fo0lOf4T0ok!"
    #"""
    """#Example of SQL injection on user_by_username_pword
    uname = "' OR 1=1--"
    pword = "--"
    #"""

    # Try query methods here:
    results = dbc.user_by_username_pword(uname, pword)
    
    if results and type(results) == list:
        for row in results:
            print(row)
    else:
        print("No results")



if __name__ == "__main__":
    main()