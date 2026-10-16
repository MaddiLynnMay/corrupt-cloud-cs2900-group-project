
from flask import Flask, jsonify, request
import sys

sys.path.append("/home/dd/corrupt-cloud-cs2900-group-project")
from db_controler import DB_Controler

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify(message="Hello from the backend!")

@app.route("/users")
def users():
    db = DB_Controler(
        "/home/dd/corrupt-cloud-cs2900-group-project/dummy_bank.db"
    )
    results = db.run_query("SELECT ID, name, username FROM User;")

    if results == -1:
        return jsonify(error="Database query failed"), 500

    return jsonify(users=results)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username", "")
    password = data.get("password", "")

    db = DB_Controler(
        "/home/dd/corrupt-cloud-cs2900-group-project/dummy_bank.db"
    )

    results = db.user_by_username_pword(username, password)

    if results == -1:
        return jsonify(message="Database query failed"), 500

    if results:
        return jsonify(message="Login successful")

    return jsonify(message="Invalid username or password"), 401

@app.route("/bankinfo/<username>")
def bankinfo(username):
    db = DB_Controler(
        "/home/dd/corrupt-cloud-cs2900-group-project/dummy_bank.db"
    )

    users = db.run_query(
        f"SELECT ID, name FROM User WHERE username = '{username}';"
    )

    if users == -1:
        return jsonify(message="Database query failed"), 500

    if not users:
        return jsonify(message="User not found"), 404

    user_id = users[0][0]
    name = users[0][1]

    accounts = db.user_accounts(user_id)

    if accounts == -1:
        return jsonify(message="Database query failed"), 500

    bank_accounts = []

    for account in accounts:
        account_name = account[1]
        balance = db.account_balance(account_name)
        transactions = db.acc_transactions(account_name)

        bank_accounts.append({
            "name": account_name,
            "balance": balance,
            "transactions": transactions
        })

    return jsonify(name=name, accounts=bank_accounts)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
