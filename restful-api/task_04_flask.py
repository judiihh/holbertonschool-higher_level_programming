from flask import Flask, jsonify, request


app = Flask(__name__)
# user data
users = {}


@app.route("/")  # Route for the root URL
def home():
    return "Welcome to the Flask API!"


@app.route("/data")  # Route to get list of usernames
def data():
    return jsonify(list(users.keys()))


@app.route("/status")  # Route to check status
def status():
    return "OK"


@app.route("/users/<username>")  # Route to get user details by username
def user_page(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])  # Route to add a new user
def add_user():
    newuser = request.json
    if not newuser or "username" not in newuser:
        return jsonify({"error": "Username is required"}), 400

    username = newuser["username"].strip().lower()
    if username == users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": newuser.get("name", ""),
        "age": newuser.get("age", 0),
        "city": newuser.get("city", "")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask development server
