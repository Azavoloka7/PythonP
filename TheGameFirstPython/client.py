import socket
import random

def client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = ('localhost', 12345)
    print('Connecting to {} port {}'.format(*server_address))
    client_socket.connect(server_address)

    try:
        # Receive the target number from the server
        data = client_socket.recv(16)
        target_number = int(data.decode())
        print('Target number:', target_number)

        # Take guesses from the user and send them to the server
        while True:
            guess = int(input('Enter your guess: '))
            client_socket.sendall(str(guess).encode())

            # Receive feedback from the server
            data = client_socket.recv(16)
            print(data.decode())

            if data == b'Correct! You win!':
                break

    finally:
        # Clean up the connection
        client_socket.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        if sys.argv[1] == 'server':
            server()
        elif sys.argv[1] == 'client':
            client()
        else:
            print("Usage: python game.py [server|client]")
    else:
        print("Usage: python game.py [server|client]")
