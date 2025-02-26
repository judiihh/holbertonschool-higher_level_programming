# 📌 RESTful API Project

## 📖 Introduction
In the evolving world of software development, understanding how to communicate and transfer data efficiently between systems is essential. This project delves into the domain of **RESTful APIs**, a cornerstone in the realm of web services. The **Representational State Transfer (REST)** architecture is a set of constraints that ensure a scalable, stateless, and cacheable communication system. This approach allows for the easy integration of web services, making them accessible to a wide range of applications.

## 🌍 RESTful API Architecture
RESTful APIs follow a client-server architecture, where the client makes requests to a server that processes them and returns responses. The key constraints of RESTful APIs include:
- **Statelessness**: Each request from a client to a server must contain all the information needed to process the request.
- **Client-Server Separation**: The client and server are independent and interact only through requests and responses.
- **Cacheability**: Responses must define whether they can be cached to improve performance.
- **Layered System**: Clients interact with the server through multiple intermediary layers for security and scalability.
- **Uniform Interface**: A consistent interface simplifies interactions between components.

## 🎯 Learning Objectives
- **HTTP/HTTPS Basics**: Understand the foundational principles of the web’s primary protocol.
- **API Consumption with Command Line**: Interact with APIs using basic command-line tools.
- **API Consumption with Python**: Fetch and process data using Python’s requests library.
- **API Development with http.server**: Create an API using Python’s built-in modules.
- **API Development with Flask**: Build APIs using Flask, handling routes and data.
- **API Security & Authentication**: Implement security measures for safe API interactions.
- **API Standards & Documentation with OpenAPI**: Learn how to document APIs for maintainability.

## 🔥 Importance
In our interconnected digital world, **RESTful APIs** serve as the backbone of system integration. They enable communication between different services, from social media platforms to financial applications. Mastering RESTful APIs allows developers to create efficient, scalable, and secure web applications.

## 🛠 REST API Conceptual Diagram
```
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database
```

## 📌 Tasks
### ✅ Task 0: Basics of HTTP/HTTPS
- Learn about HTTP and HTTPS differences.
- Explore HTTP request and response structures.
- Understand common HTTP methods and status codes.

### ✅ Task 1: Consume data from an API using command-line tools (curl)
- Use `curl` to interact with APIs.
- Fetch and inspect API responses.
- Perform GET and POST requests.

### ✅ Task 2: Consuming and processing data from an API using Python
- Use Python’s `requests` library.
- Parse and manipulate JSON data.
- Convert JSON data into CSV format.

### ✅ Task 3: Develop a simple API using Python with the `http.server` module
- Implement a basic HTTP server in Python.
- Handle GET requests and serve JSON data.
- Implement error handling for undefined endpoints.

### ✅ Task 4: Develop a Simple API using Python with Flask
- Set up a Flask API and define routes.
- Serve JSON data and handle POST requests.
- Implement dynamic routing and user management.

### ✅ Task 5: API Security and Authentication Techniques
- Implement Basic Authentication using Flask.
- Secure APIs with JSON Web Tokens (JWT).
- Enforce role-based access control for different users.

## 📂 Repository Structure
- `restful-api/task_00_http_basics.md` – Documentation on HTTP/HTTPS basics.
- `restful-api/task_01_curl_requests.sh` – Script for consuming APIs via `curl`.
- `restful-api/task_02_requests.py` – Python script for API interaction and data processing.
- `restful-api/task_03_http_server.py` – Simple API using Python’s `http.server`.
- `restful-api/task_04_flask.py` – API development using Flask.
- `restful-api/task_05_basic_security.py` – Implementation of API security techniques.

## 🚀 How to Run the Project
### Install Dependencies
```bash
pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended
```
### Running the API Server
```bash
python3 task_03_http_server.py
```
### Running the Flask API
```bash
flask --app task_04_flask.py run
```
### Testing the API with curl
```bash
curl http://localhost:8000/data
```

## 📝 Conclusion
This project provides a hands-on approach to working with **RESTful APIs**, from basic HTTP interactions to building and securing APIs using Python. By completing these tasks, you gain essential skills in web development, API consumption, and security best practices.
