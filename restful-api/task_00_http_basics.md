#HTTP/HTTPS Basics

## 1. Differences Between HTTP and HTTPS

### HTTP
- **Plaintext communication**: Data travels unencrypted, making it readable by anyone intercepting.
- **Port 80 (default)**.
- **Less secure**: Not recommended for sensitive data transfers.

### HTTPS
- **Encryption**: Uses TLS/SSL, ensuring data is protected in transit.
- **Server Authentication**: SSL certificates verify the server’s identity.
- **Port 443 (default)**.
- **Secure by default**: Highly recommended for any site handling personal or payment data.

---

## 2. Structure of an HTTP Request and Response

### A. HTTP Request

- **Method**: Commonly `GET`, `POST`, `PUT`, `DELETE`, etc.
- **Path**: The resource location (e.g., `/index.html` or `/api/users`).
- **Version**: Often `HTTP/1.1` or `HTTP/2`.
- **Headers**: Provide additional info (like `Host`, `User-Agent`, `Accept`).
- **Body (optional)**: Present with methods like `POST` or `PUT` to send data.

### B. HTTP Response

- **Version**: e.g., `HTTP/1.1`.
- **Status Code**: e.g., `200`, `404`, `500`.
- **Status Message**: e.g., `OK`, `Not Found`, `Internal Server Error`.
- **Headers**: Include metadata (like `Content-Type`, `Content-Length`).
- **Body (optional)**: The content returned (HTML, JSON, images, etc.).

---

## 3. Four Common HTTP Methods

1. **GET**
   - **Description**: Reads or retrieves data.
   - **Use Case**: Loading webpages, fetching API data.

2. **POST**
   - **Description**: Sends data to the server, creating or processing resources.
   - **Use Case**: Submitting forms, creating new records in a database.

3. **PUT**
   - **Description**: Updates or creates a resource at a given URL.
   - **Use Case**: Editing an existing resource or uploading a file to a specific location.

4. **DELETE**
   - **Description**: Removes a specified resource.
   - **Use Case**: Deleting a user account or removing an entry from a database.

---

## 4. Five Common HTTP Status Codes

1. **200 OK**
   - **Meaning**: The request succeeded.
   - **Example**: A webpage loaded successfully or an API returned valid data.

2. **301 Moved Permanently**
   - **Meaning**: The resource has permanently moved to a new URI.
   - **Example**: Redirecting old URLs to new ones.

3. **403 Forbidden**
   - **Meaning**: The server understands the request, but is refusing to fulfill it.
   - **Example**: A user without permissions trying to access an admin page.

4. **404 Not Found**
   - **Meaning**: The requested resource cannot be found.
   - **Example**: A broken link or a mistyped URL.

5. **500 Internal Server Error**
   - **Meaning**: The server encountered an unexpected condition.
   - **Example**: A bug in server-side code prevents fulfilling the request.

---

## Summary

- **HTTP vs. HTTPS**: HTTPS adds TLS/SSL encryption and server authentication to plain HTTP, making data transfers secure and private.
- **Structure**: Both HTTP requests and responses have a start line, optional headers, and an optional body.
- **Methods**: `GET`, `POST`, `PUT`, and `DELETE` are fundamental operations used in RESTful APIs.
- **Status Codes**: Indicate request outcomes, from success (`2xx`) to client errors (`4xx`) and server errors (`5xx`).
