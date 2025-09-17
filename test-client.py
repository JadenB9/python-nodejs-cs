#!/usr/bin/env python3

import socket
import time

SERVER_HOST = 'localhost'
SERVER_PORT = 7777

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
        client_socket.send(message1.encode('utf-8'))
        response1 = client_socket.recv(1024)
        print(f"Server response: {response1.decode('utf-8').strip()}")

        # Wait a bit
        time.sleep(1)

        # Send second test message
        message2 = "Second message from client"
        client_socket.send(message2.encode('utf-8'))
        response2 = client_socket.recv(1024)
        print(f"Server response: {response2.decode('utf-8').strip()}")

        # Wait a bit
        time.sleep(1)

        # Send quit message
        client_socket.send(b"quit")
        response3 = client_socket.recv(1024)
        print(f"Server response: {response3.decode('utf-8').strip()}")

        # Close connection
        client_socket.close()
        print("Connection closed")

    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    main()