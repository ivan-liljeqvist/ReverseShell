# Ivan Liljeqvist

import socket
import sys


# creating the socket
def create_socket():
    try:
        global host
        global port
        global theSocket
        global MAX_CONNECTIONS
        host = ''
        port = 9997
        theSocket = socket.socket()
        MAX_CONNECTIONS = 10
    except socket.error as errorMessage:
        print("Error while creating socket: "+str(errorMessage))


# connect the socket to the port and wait for the client
def bind_socket():
    try:
        global host
        global port
        global theSocket
        print("Binding socket to port: "+str(port))
        theSocket.bind((host, port))
        theSocket.listen(MAX_CONNECTIONS)
    except socket.error as errorMessage:
        print("Error while binding socket: "+str(errorMessage)+"\n Retrying...")
        bind_socket()


# establish the connection with a client.
# in order for this to work, the socket must be listening
def accept_socket():
    connection, address = theSocket.accept()
    print("Connection has been established! IP: "+address[0]+" Port: "+str(address[1]))
    send_commands(connection)  # wait for commands from the connection
    connection.close()


def send_commands(connection):
    while True:  # keep waiting for new commands
        command = input()  # get input from the terminal
        if command == 'quit':
            connection.close()
            theSocket.close()
            sys.exit()
        if len(str.encode(command)) > 0:
            connection.send(str.encode(command))
            client_response = str(connection.recv(1024), "utf-8")
            print("\nClient responded: \n"+client_response, end="")


def main():
    create_socket()
    bind_socket()
    accept_socket()

main()
