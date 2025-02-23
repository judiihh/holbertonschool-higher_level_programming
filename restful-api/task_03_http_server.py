#!/usr/bin/python3
"""
This module defines a simple HTTP server with multiple endpoints.
"""
import http.server as hs
import json


PORT = 8000


class SimpleHTTPGet(hs.BaseHTTPRequestHandler):
    """
    A simple HTTP request handler with GET endpoints.
    """
    def do_GET(self):
        """
        Handles GET requests and routes them to the appropriate handler
        based on the request path.
        """
        if self.path == "/":
            self.handle_root()
        elif self.path == "/data":
            self.route_data()
        elif self.path == "/status":
            self.status()
        else:
            self.route_404()

    def handle_root(self):
        """
        Handles requests to the root endpoint ("/").
        """
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))

    def route_data(self):
        """
        Handles requests to the "/data" endpoint and returns JSON data.
        """
        data = {"name": "John", "age": 30, "city": "New York"}
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(data), "utf-8"))

    def status(self):
        """
        Handles request to the "/status" endpoint and returns a status message.
        """
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        self.wfile.write(bytes("OK", "utf-8"))

    def route_404(self):
        """
        Handles requests to unknown endpoints and returns a 404 error message.
        """
        self.send_response(404)
        self.send_header("Content-type", "text")
        self.end_headers()
        self.wfile.write(bytes("Endpoint not found", "utf-8"))


if __name__ == "__main__":
    server = hs.HTTPServer(('', PORT), SimpleHTTPGet)
    print("Server running on {}".format(PORT))
    server.serve_forever()
