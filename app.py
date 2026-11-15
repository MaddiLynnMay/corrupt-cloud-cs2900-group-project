
from flask import Flask, jsonify, request
from functools import wraps
import jwt
import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "dummy_bank.db")

from db_controler import DB_Controler

app = Flask(__name__)

# Secret key that the backend uses to sign tokens and verify they haven't
# been tampered with.
# JWT_SECRET_KEY looks for the key stored in the backend
# development_secret_key is a fallback for local development
app.config["SECRET_KEY"] = os.environ.get(
    "JWT_SECRET_KEY", "development-secret-key"
)

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # retrieves JWT cookie 
        token = request.cookies.get("auth_token")

        #checks if user has token
        if not token:
            return jsonify(message="Authentication required"), 401

        try:
            # verifies token signature
            decoded = jwt.decode(
                token,
                app.config["SECRET_KEY"],
                algorithms=["HS256"]
            )

        # detects expired tokens
        except jwt.ExpiredSignatureError:
            return jsonify(message="Token expired"), 401

        # detects invalid tokens
        except jwt.InvalidTokenError:
            return jsonify(message="Invalid token"), 401

        # stores authenticated username for route
        request.current_user = decoded.get("username")

        # allows original route to execute
        return f(*args, **kwargs)

    return decorated

@app.route("/hello")
def hello():
    return jsonify(message="Hello from the backend!")

@app.route("/users")
def users():
    db = DB_Controler(DATABASE_PATH)
    results = db.run_query("SELECT ID, name, username FROM User;")

    if results == -1:
        return jsonify(error="Database query failed"), 500

    return jsonify(users=results)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username", "")
    password = data.get("password", "")

    db = DB_Controler(DATABASE_PATH)

    results = db.user_by_username_pword(username, password)

    if results == -1:
        return jsonify(message="Database query failed"), 500

    if results:
        # .encode creates the actual JWT (json web token)
        token = jwt.encode(
            {
                # identifies which user the token belongs to
                "username": username,
                # token expires in 30 minutes
                "exp": datetime.datetime.now(datetime.timezone.utc)
                + datetime.timedelta(minutes=30)
            },
            # secret key used to sign token
            app.config["SECRET_KEY"],
            # signing algorithm
            algorithm = "HS256"
        )
        response = jsonify(message = "Login successful")

        response.set_cookie(
            "auth_token", # cookie name
            token,
            httponly = True, # prevents javascript access
            secure = False, # allows HTTP during local development, change to True later
            samesite = "Lax", # provides some CSRF protection
            max_age = 1800 # cookie expires after 30 minutes
        )

        return response

    return jsonify(message="Invalid username or password"), 401

# creates endpoint for logging out
@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify(message = "Logout successful")

    # removes authentication cookie
    response.delete_cookie(
        "auth_token",
        # matches cookie settings used duwhring login
        httponly = True,
        secure = False,
        samesite = "Lax"
    )

    return response

@app.route("/bankinfo/")
@require_auth
def bankinfo():
    username = request.current_user

    db = DB_Controler(DATABASE_PATH)

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
