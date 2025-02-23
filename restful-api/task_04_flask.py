#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users (Start empty)
users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    return "OK"

@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        if not data or 'username' not in data:
            return jsonify({"error": "Username is required"}), 400

        username = data['username']
        if username in users:
            return jsonify({"error": "User already exists"}), 400
        
        # Ensure all fields are properly set
        users[username] = {
            "username": username,
            "name": data.get("name", ""),
            "age": data.get("age", 0),
            "city": data.get("city", "")
        }
        
        return jsonify({"message": "User added", "user": users[username]}), 201
    except Exception as e:
        return jsonify({"error": "Invalid request format"}), 400

if __name__ == "__main__":
    app.run(debug=True)
