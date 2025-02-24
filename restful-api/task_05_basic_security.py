from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# User database
user_data = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password123"),
        "role": "user"
    },
    "admin": {
        "username": "admin",
        "password": generate_password_hash("adminpass"),
        "role": "admin"
    }
}

app.config['JWT_SECRET_KEY'] = 'super_secure_key'
jwt = JWTManager(app)

@auth.verify_password
def authenticate(username, password):
    user = user_data.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None

@app.route('/secure-basic', methods=['GET'])
@auth.login_required
def secure_basic():
    return jsonify({"message": "Access Granted: Basic Authentication Successful"})

@app.route('/auth-login', methods=['POST'])
def auth_login():
    credentials = request.get_json()
    username = credentials.get("username")
    password = credentials.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = user_data.get(username)
    if user and check_password_hash(user["password"], password):
        token = create_access_token(identity={"username": username, "role": user['role']})
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/secure-jwt', methods=['GET'])
@jwt_required()
def secure_jwt():
    return jsonify({"message": "Access Granted: JWT Authentication Successful"})

@app.route('/admin-area', methods=['GET'])
@jwt_required()
def admin_area():
    user_identity = get_jwt_identity()
    if user_identity['role'] != 'admin':
        return jsonify({"error": "Administrator access required"}), 403
    return jsonify({"message": "Administrator Privileges Granted"})

@jwt.unauthorized_loader
def unauthorized_access(error):
    return jsonify({"error": "Authorization token is missing or invalid"}), 401

@jwt.invalid_token_loader
def invalid_token(error):
    return jsonify({"error": "The provided token is invalid"}), 401

@jwt.expired_token_loader
def expired_token(error):
    return jsonify({"error": "Your session token has expired"}), 401

@jwt.revoked_token_loader
def revoked_token(error):
    return jsonify({"error": "This token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def fresh_token_required(error):
    return jsonify({"error": "A fresh authentication token is needed"}), 401

if __name__ == '__main__':
    app.run(debug=True)
