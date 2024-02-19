import socket
import random

def server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_address = ('localhost', 12345)
    print('Starting server on {} port {}'.format(*server_address))
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)

    print('Waiting for a connection...')
    connection, client_address = server_socket.accept()

    try:
        print('Connection from', client_address)

        # Generate a random number between 1 and 100
        target_number = random.randint(1, 100)

        # Send the target number to the client
        connection.sendall(str(target_number).encode())

        # Receive guesses from the client
        while True:
            data = connection.recv(16)
            if data:
                guess = int(data.decode())
                print('Received', guess)

                # Compare the guess to the target number
                if guess == target_number:
                    connection.sendall(b'Correct! You win!')
                    break
                else:
                    connection.sendall(b'Incorrect! Try again!')
            else:
                print('No data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
