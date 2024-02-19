import socket
import threading
import random

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def handle_client_connection(self, connection, client_number):
        try:
            print('Client {} connected'.format(client_number))

            # Generate a random number between 1 and 100
            target_number = random.randint(1, 100)

            # Send the target number to the client
            connection.sendall(str(target_number).encode())

            # Receive guesses from the client
            while True:
                data = connection.recv(16)
                if data:
                    guess = int(data.decode())
                    print('Client {} guessed: {}'.format(client_number, guess))

                    # Compare the guess to the target number
                    if guess == target_number:
                        connection.sendall(b'Correct! You win!')
                        print('Client {} wins!'.format(client_number))
                        break
                    else:
                        connection.sendall(b'Incorrect! Try again!')
                else:
                    print('No data from client', client_number)
                    break

        finally:
            # Clean up the connection
            connection.close()

    def start(self):
        # Bind the socket to the address and port
        server_address = (self.host, self.port)
        print('Starting server on {} port {}'.format(*server_address))
        self.server_socket.bind(server_address)

        # Listen for incoming connections
        self.server_socket.listen(2)

        client_number = 1
        while True:
            print('Waiting for a connection...')
            connection, client_address = self.server_socket.accept()

            # Handle client connection in a separate thread
            client_thread = threading.Thread(target=self.handle_client_connection, args=(connection, client_number))
            client_thread.start()

            # Increment client number for next connection
            client_number += 1

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        # Connect the socket to the server's address and port
        server_address = (self.host, self.port)
        print('Connecting to {} port {}'.format(*server_address))
        self.client_socket.connect(server_address)

        try:
            # Receive the target number from the server
            data = self.client_socket.recv(16)
            target_number = int(data.decode())
            print('Target number:', target_number)

            # Take guesses from the user and send them to the server
            while True:
                guess = int(input('Enter your guess: '))
                self.client_socket.sendall(str(guess).encode())

                # Receive feedback from the server
                data = self.client_socket.recv(16)
                print(data.decode())

                if data == b'Correct! You win!':
                    break

        finally:
            # Clean up the connection
            self.client_socket.close()

def main():
    # Create a Server instance and start it in a separate thread
    server = Server("localhost", 12345)
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    # Create a Client instance and start it
    client = Client("localhost", 12345)
    client.start()

if __name__ == "__main__":
    main()
