#!/usr/bin/env python3

import socket
import sys
import threading

SERVER_HOST = 'localhost'
SERVER_PORT = 7777

class TCPClient:
    def __init__(self):
        self.socket = None
        self.connected = False

    def connect(self):
        """Connect to the TCP server"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((SERVER_HOST, SERVER_PORT))
            self.connected = True
            print(f"Connected to server at {SERVER_HOST}:{SERVER_PORT}")
            print('Type messages to send to server (type "quit" to exit):')
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False

    def listen_for_messages(self):
        """Listen for messages from server in a separate thread"""
        try:
            while self.connected:
                response = self.socket.recv(1024)
                if not response:
                    break
                print(f"Server response: {response.decode('utf-8').strip()}")
                self.prompt_user()
        except Exception as e:
            if self.connected:
                print(f"Error receiving data: {e}")
        finally:
            self.disconnect()

    def send_message(self, message):
        """Send message to server"""
        try:
            self.socket.send(message.encode('utf-8'))
            if message.lower() == 'quit':
                self.connected = False
        except Exception as e:
            print(f"Error sending message: {e}")
            self.connected = False

    def prompt_user(self):
        """Show prompt for user input"""
        if self.connected:
            sys.stdout.write('> ')
            sys.stdout.flush()

    def disconnect(self):
        """Disconnect from server"""
        if self.connected:
            self.connected = False
            print("Connection closed")
        if self.socket:
            self.socket.close()

    def run(self):
        """Main client loop"""
        if not self.connect():
            return

        # Start listening thread
        listen_thread = threading.Thread(target=self.listen_for_messages)
        listen_thread.daemon = True
        listen_thread.start()

        try:
            while self.connected:
                user_input = input()
                if not self.connected:
                    break

                self.send_message(user_input)

                if user_input.lower() == 'quit':
                    break

        except KeyboardInterrupt:
            print("\nDisconnecting...")
        except EOFError:
            print("\nDisconnecting...")
        finally:
            self.disconnect()

def main():
    client = TCPClient()
    client.run()

if __name__ == "__main__":
    main()