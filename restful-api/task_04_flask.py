from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store user information
users = {}


@app.route("/")
def home():
    return "Hello! This is a simple Flask API."


@app.route("/data")
def get_user_list():
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    return "Service is running."


@app.route("/users/<username>")
def get_user_info(username):
    user_info = users.get(username)
    if user_info:
        return jsonify(user_info)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def create_user():
    user_data = request.get_json()
    username = user_data.get("username")

    if not username:
        return jsonify({"error": "A username is required."}), 400
    if username in users:
        return jsonify({"error": "This user already exists."}), 400

    users[username] = user_data
    return jsonify({
        "message": "User successfully added.",
        "user": user_data
        }), 201


if __name__ == "__main__":
    app.run(debug=True)
