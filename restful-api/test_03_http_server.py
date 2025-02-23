#!/usr/bin/python3
import unittest
import requests
import time
import subprocess

PORT = 8000
BASE_URL = f"http://localhost:{PORT}"

class TestSimpleHTTPServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Start the HTTP server in the background"""
        cls.server = subprocess.Popen(["python3", "task_03_http_server.py"])
        time.sleep(1)  # Give the server time to start

    @classmethod
    def tearDownClass(cls):
        """Kill the server process after tests"""
        cls.server.terminate()
        cls.server.wait()

    def test_root_endpoint(self):
        """Test if root endpoint returns correct content."""
        response = requests.get(BASE_URL + "/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, this is a simple API!")
        print("Test if root endpoint returns correct content.: OK")

    def test_data_endpoint(self):
        """Test if /data endpoint returns correct JSON."""
        response = requests.get(BASE_URL + "/data")
        expected_data = {"name": "John", "age": 30, "city": "New York"}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
        print("Test if data endpoint returns correct data.: OK")

    def test_status_endpoint(self):
        """Test if /status endpoint returns correct status."""
        response = requests.get(BASE_URL + "/status")
        expected_data = {"status": "OK"}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
        print("Test if status endpoint returns correct status.: OK")

    def test_info_endpoint(self):
        """Test if /info endpoint returns correct response."""
        response = requests.get(BASE_URL + "/info")
        expected_data = {"version": "1.0", "description": "A simple API built with http.server"}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
        print("Test if info endpoint returns correct response.: OK")

    def test_undefined_endpoint(self):
        """Test if an undefined endpoint returns 404."""
        response = requests.get(BASE_URL + "/undefined")
        expected_data = {"error": "404 Not found"}
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), expected_data)
        print("Test if undefined endpoint returns correct status.: OK")

if __name__ == "__main__":
    unittest.main()
