#!/usr/bin/python3
import http.server
import socketserver
import json

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len("Hello, this is a simple API!")))
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            data = {"name": "John", "age": 30, "city": "New York"}
            response = json.dumps(data).encode("utf-8")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            status = {"status": "OK"}
            response = json.dumps(status, separators=(",", ":")).encode("utf-8")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            response = json.dumps(info, separators=(",", ":")).encode("utf-8")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)
        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            error_message = {"error": "Endpoint not found"}
            response = json.dumps(error_message, separators=(",", ":")).encode("utf-8")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

PORT = 8000

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
