#!/usr/bin/env python3

import socket
import sys
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

TCP_HOST = 'localhost'
HTTP_PORT = 3001

def port_from_args(default):
    """Optional --port N on the command line"""
    args = sys.argv[1:]
    if '--port' not in args:
        return default
    try:
        port = int(args[args.index('--port') + 1])
        if 1 <= port <= 65535:
            return port
    except (IndexError, ValueError):
        pass
    print("usage: --port <1-65535>")
    sys.exit(1)

TCP_PORT = port_from_args(7777)

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        response = {"message": "Hello from your new Python server!"}
        self.wfile.write(json.dumps(response).encode())

    def log_message(self, format, *args):
        pass

def handle_client(client_socket, client_address):
    """Handle individual client connections"""
    print(f"Client connected: {client_address[0]}:{client_address[1]}")

    try:
        client_socket.sendall(f"Welcome to TCP Server on {TCP_HOST}:{TCP_PORT}\n".encode('utf-8'))

        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            message = data.decode('utf-8', errors='replace').strip()
            print(f"Received from client: {message}")

            if message.lower() == 'quit':
                client_socket.sendall(b"Bye\n")
                break

            response = f"Echo: {message}\n"
            client_socket.sendall(response.encode('utf-8'))

    except ConnectionResetError:
        print("Socket error: Connection reset by peer")
    except Exception as e:
        print(f"Socket error: {e}")
    finally:
        print("Client disconnected")
        client_socket.close()

def start_tcp_server():
    """Start the TCP server"""
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        tcp_server.bind((TCP_HOST, TCP_PORT))
        tcp_server.listen(5)
        print(f"TCP Server running on {TCP_HOST}:{TCP_PORT}")

        while True:
            client_socket, client_address = tcp_server.accept()
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.daemon = True
            client_thread.start()

    except KeyboardInterrupt:
        print("\nTCP Server shutting down...")
    except Exception as e:
        print(f"TCP Server error: {e}")
    finally:
        tcp_server.close()

def start_http_server():
    """Start the HTTP server"""
    try:
        httpd = HTTPServer(('localhost', HTTP_PORT), HTTPRequestHandler)
        print(f"HTTP Server running on port {HTTP_PORT}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nHTTP Server shutting down...")
    except Exception as e:
        print(f"HTTP Server error: {e}")

def main():
    """Main function to start both servers"""
    print("Starting Python TCP and HTTP servers...")

    # Start HTTP server in a separate thread
    http_thread = threading.Thread(target=start_http_server)
    http_thread.daemon = True
    http_thread.start()

    # Start TCP server in main thread
    start_tcp_server()

if __name__ == "__main__":
    main()