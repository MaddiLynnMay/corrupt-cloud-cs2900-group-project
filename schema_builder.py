import sys
import sqlite3
import dummy_data


reset_queries = [
    "DROP TABLE IF EXISTS User;",
    "DROP TABLE IF EXISTS Account;",
    "DROP TABLE IF EXISTS AccTransaction;"
]


schema_queries = [
    """
    CREATE TABLE User (
        ID INTEGER PRIMARY KEY,
        name TEXT,
        username TEXT,
        p_word TEXT
    );
    """,
    """
    CREATE TABLE Account(
        ID INTEGER PRIMARY KEY,
        userID INTEGER,
        acc_name TEXT,
        balance INTEGER
    );
    """,
    """
    CREATE TABLE AccTransaction(
        ID INTEGER PRIMARY KEY,
        accountID INTEGER,
        date TEXT,
        amount INTEGER,
        balance INTEGER,
        note TEXT
    );
    """
]


def main():
    conn = sqlite3.connect("dummy_bank.db")
    cursor = conn.cursor()

    for query in reset_queries:
        print(f"running query:\n{query}")
        input("Return to run...")
        conn.execute(query)
        print("ran")
    conn.commit()
    print("Ran all reset queries.\n")

    print("Building schema")
    for query in schema_queries:
        print(f"running query:\n{query}")
        input("Return to run...")
        conn.execute(query)
        print("ran")
    conn.commit()
    print("Ran all schema queries.\n")

    
    load_dummy_data = input("Load Dummy Data? (y/n): ")
    if load_dummy_data.lower() == 'y':

        print("Loading User Data...")
        cursor.executemany(
            "INSERT INTO User (ID, name, username, p_word) VALUES (?, ?, ?, ?)",
            dummy_data.users
        )

        print("Loading Account Data...")
        cursor.executemany(
            "INSERT INTO Account (ID, userID, acc_name, balance) VALUES (?, ?, ?, ?)",
            dummy_data.accounts
        )

        print("Loading AccTransaction Data...")
        cursor.executemany(
            "INSERT INTO AccTransaction (ID, accountID, date, amount, balance, note) VALUES (?, ?, ?, ?, ?, ?)",
            dummy_data.transactions
        )
        conn.commit()
        print("All data *should* be loaded now... ")
    
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()