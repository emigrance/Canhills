from flask import Flask, jsonify, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import sqlite3

app = Flask(__name__)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Logic to save user to the database
    conn = sqlite3.connect('job_board.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (username, password, role) VALUES (?, ?, ?)", (username, password, 'job_seeker'))
    conn.commit()
    conn.close()

    return jsonify({"message": "User registered successfully"}), 201

@app.route('/apply', methods=['POST'])
def apply_job():
    data = request.json
    job_id = data.get('job_id')
    applicant_name = data.get('name')
    applicant_email = data.get('email')
    applicant_message = data.get('message')

    # Logic to save application to the database
    conn = sqlite3.connect('job_board.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Applications (job_id, applicant_name, applicant_email, message) VALUES (?, ?, ?, ?)", (job_id, applicant_name, applicant_email, applicant_message))
    conn.commit()
    conn.close()

    return jsonify({"message": "Application submitted successfully"}), 201




@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Logic to check user credentials
    conn = sqlite3.connect('job_board.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        user_obj = User(user[0], user[1], user[2], user[3])
        login_user(user_obj)
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@login_manager.user_loader
def load_user(user_id):
    # Logic to load user from the database
    conn = sqlite3.connect('job_board.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return User(user[0], user[1], user[2], user[3]) if user else None

if __name__ == '__main__':
    app.run(debug=True)
