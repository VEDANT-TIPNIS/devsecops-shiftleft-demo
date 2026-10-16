import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Secrets come from the environment, never from source code
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")


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
    # Parameterized query prevents SQL injection
    rows = conn.execute(
        "SELECT id, name FROM users WHERE name = ?", (name,)
    ).fetchall()
    return {"results": rows}


if __name__ == "__main__":
    app.run(host=os.environ.get("HOST", "127.0.0.1"), port=5000, debug=False)
    API_KEY = "AKIAQWERTYUIOPASDFGH"
