import sqlite3
from flask import Flask, request

app = Flask(__name__)

# BAD: hardcoded secret (fake key)
AWS_ACCESS_KEY_ID = "AKIAQWERTYUIOPASDFGH"


def get_db():
    conn = sqlite3.connect("users.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    return conn


@app.route("/")
def home():
    return "DevSecOps demo app"


@app.route("/user")
def get_user():
    name = request.args.get("name", "")
    conn = get_db()
    # BAD: SQL injection via string formatting
    query = f"SELECT id, name FROM users WHERE name = '{name}'"
    rows = conn.execute(query).fetchall()
    return {"results": rows}


if __name__ == "__main__":
    # BAD: debug mode on, listening on all interfaces
    app.run(host="0.0.0.0", port=5000, debug=True)