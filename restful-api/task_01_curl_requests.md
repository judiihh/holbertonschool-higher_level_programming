# Consume Data from an API Using Command Line Tools (curl)

## 1. Introduction to curl

**curl** (Client URL) is a powerful command-line tool used to transfer data from or to a server. It supports multiple protocols, including **HTTP, HTTPS, FTP, and more**.  

This tool is commonly used for:
- Debugging APIs.
- Testing network requests.
- Automating data transfers.

---

## 2. Installing and Checking curl

### **Installation**
- **Linux/macOS**: curl is pre-installed on most systems. If missing, install it with:
  ```sh
  sudo apt install curl   # Debian/Ubuntu
  sudo yum install curl   # CentOS
  brew install curl       # macOS (Homebrew)
  ```
- **Windows**: Download from [curl official site](https://curl.se/windows/) or use Git Bash.

### **Verify Installation**
To confirm that curl is installed, run:
```sh
curl --version
```
Expected output (example):
```sh
curl 7.79.1 (x86_64-pc-linux-gnu) libcurl/7.79.1 OpenSSL/1.1.1l zlib/1.2.11
```

---

## 3. Fetching Data from an API

To retrieve **posts** from the JSONPlaceholder API, run:
```sh
curl https://jsonplaceholder.typicode.com/posts
```
This returns a **JSON array** containing multiple posts. Example output:
```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "Sample title",
    "body": "This is a sample post body."
  },
  {
    "userId": 1,
    "id": 2,
    "title": "Another post",
    "body": "More content..."
  }
]
```

---

## 4. Fetching Only Headers

To retrieve only the response headers (useful for debugging):
```sh
curl -I https://jsonplaceholder.typicode.com/posts
```
Example output:
```sh
HTTP/1.1 200 OK
Date: Sat, 23 Feb 2025 10:30:00 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 500
Connection: keep-alive
Cache-Control: max-age=43200
```

---

## 5. Sending Data Using a POST Request

To create a new post using **POST**, run:
```sh
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```
Example response (JSONPlaceholder simulates creation):
```json
{
  "title": "foo",
  "body": "bar",
  "userId": 1,
  "id": 101
}
```
**Explanation of flags used:**
- `-X POST` → Specifies the HTTP method (`POST`).
- `-d` → Sends the request body (URL-encoded format).

---

## 6. Using JSON with POST Requests

Instead of sending URL-encoded data, we can use JSON format:
```sh
curl -X POST -H "Content-Type: application/json" -d '{"title": "foo", "body": "bar", "userId": 1}' https://jsonplaceholder.typicode.com/posts
```
**Explanation of flags used:**
- `-H "Content-Type: application/json"` → Sets the header to indicate JSON data.
- `-d '{"title": "foo", "body": "bar", "userId": 1}'` → Sends JSON data.

---

## 7. Additional curl Commands

### **Follow Redirects Automatically**
```sh
curl -L http://example.com
```
(The `-L` flag ensures that curl follows redirects, useful when sites move to HTTPS.)

### **Save API Response to a File**
```sh
curl -o response.json https://jsonplaceholder.typicode.com/posts
```
(Saves the API output to `response.json`.)

### **Make a GET Request with a Custom User-Agent**
```sh
curl -A "MyCustomAgent/1.0" https://jsonplaceholder.typicode.com/posts
```

---

## 8. Summary

- **`curl --version`** → Check installation.  
- **`curl URL`** → Fetch data.  
- **`curl -I URL`** → Get headers only.  
- **`curl -X POST -d "data"`** → Send data via `POST`.  
- **`curl -X POST -H "Content-Type: application/json" -d "json data"`** → Send JSON data.  
- **`curl -L URL`** → Follow redirects.  
- **`curl -o filename URL`** → Save response to a file.  

Using **curl**, you can efficiently interact with APIs, debug requests, and automate data retrieval!
