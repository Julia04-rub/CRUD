from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import sqlite3
import bcrypt

app = Flask(__name__, static_folder="static")
CORS(app)

app.config["JWT_SECRET_KEY"] = "secret123"
jwt = JWTManager(app)


def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        position TEXT,
        salary INTEGER
    )
    """)

    conn.commit()
    conn.close()


init_db()


@app.route("/")
def home():
    return send_from_directory("static", "login.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("static", path)


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username, hashed)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "User registered"})


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data["username"]
    password = data["password"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    conn.close()

    if user and bcrypt.checkpw(password.encode("utf-8"), user[2]):
        token = create_access_token(identity=username)
        return jsonify({"access_token": token})

    return jsonify({"message": "Invalid login"})


@app.route("/employees", methods=["GET"])
@jwt_required()
def get_employees():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    conn.close()

    employees = []

    for r in rows:
        employees.append({
            "id": r[0],
            "name": r[1],
            "position": r[2],
            "salary": r[3]
        })

    return jsonify(employees)


@app.route("/employees", methods=["POST"])
@jwt_required()
def add_employee():

    data = request.get_json()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO employees(name,position,salary) VALUES(?,?,?)",
        (data["name"], data["position"], data["salary"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Employee added"})


@app.route("/employees/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_employee(id):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employees WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return jsonify({"message": "Employee deleted"})


if __name__ == "__main__":
    app.run(debug=True)