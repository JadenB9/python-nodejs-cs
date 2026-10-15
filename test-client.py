#!/usr/bin/env python3

import socket
import sys
import time

SERVER_HOST = 'localhost'

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

SERVER_PORT = port_from_args(7777)

def main():
    """Test client that sends predefined messages"""
    try:
        # Create socket and connect
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print(f"Connected to server at {SERVER_HOST}:{SERVER_PORT}")

        # Receive welcome message
        welcome = client_socket.recv(1024)
        print(f"Server response: {welcome.decode('utf-8').strip()}")

        # Send first test message
        message1 = "Hello from test client!"
        client_socket.sendall(message1.encode('utf-8'))
        response1 = client_socket.recv(1024)
        print(f"Server response: {response1.decode('utf-8').strip()}")

        # Wait a bit
        time.sleep(1)

        # Send second test message
        message2 = "Second message from client"
        client_socket.sendall(message2.encode('utf-8'))
        response2 = client_socket.recv(1024)
        print(f"Server response: {response2.decode('utf-8').strip()}")

        # Wait a bit
        time.sleep(1)

        # Send quit message
        client_socket.sendall(b"quit")
        response3 = client_socket.recv(1024)
        print(f"Server response: {response3.decode('utf-8').strip()}")

        # Close connection
        client_socket.close()
        print("Connection closed")

    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    main()