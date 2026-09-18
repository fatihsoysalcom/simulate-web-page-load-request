import http.client
import ssl

# This script simulates the journey of a click, from sending a request to receiving a response.

# Step 1: User initiates a request (e.g., by typing a URL or clicking a link).
# The browser (simulated by this script) prepares to send an HTTP request.
TARGET_HOST = "www.example.com"
TARGET_PATH = "/" # Requesting the root path of the website

print(f"Simulating a web request to: https://{TARGET_HOST}{TARGET_PATH}\n")

try:
    # Step 2: The browser establishes a connection to the remote server.
    # For HTTPS, an SSL/TLS context is needed for secure communication.
    # This is where DNS resolution would typically happen to find the server's IP address.
    context = ssl.create_default_context()
    conn = http.client.HTTPSConnection(TARGET_HOST, context=context)
    print(f"Connection established to {TARGET_HOST}.\n")

    # Step 3: The browser sends an HTTP GET request to the server.
    # This request includes the method (GET), path, and HTTP headers.
    conn.request("GET", TARGET_PATH, headers={"User-Agent": "SimulatedBrowser/1.0"})
    print(f"Request sent: GET {TARGET_PATH} HTTP/1.1 (User-Agent: SimulatedBrowser/1.0)\n")

    # Step 4: The server processes the request and sends back a response.
    # This response includes a status code, headers, and the actual content (HTML, CSS, JS, etc.).
    response = conn.getresponse()
    print(f"Response received from server.\n")

    # Step 5: The browser receives and processes the response.
    # First, it checks the status code.
    print(f"--- HTTP Status Code ---")
    print(f"Status: {response.status} {response.reason}\n") # 200 OK means success

    # Then, it reads the response headers.
    print(f"--- Response Headers ---")
    for header, value in response.getheaders():
        print(f"{header}: {value}")
    print("\n")

    # Finally, it reads the response body (the actual content of the web page).
    # In a real browser, this HTML content would be parsed and rendered.
    print(f"--- Response Body (first 500 characters) ---")
    body = response.read().decode('utf-8', errors='ignore')
    print(body[:500] + "..." if len(body) > 500 else body)
    print("\n")

    print("Web page load simulation complete.")

except http.client.HTTPException as e:
    print(f"HTTP Error: {e}")
except ssl.SSLError as e:
    print(f"SSL Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close() # Always close the connection
        print("Connection closed.")
