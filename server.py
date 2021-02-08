import socket
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
# client_list = []

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    username = connection.recv(2048)
    password = connection.recv(2048)
    if username.decode() == "Ali":
        if password.decode() == "1234":
            connection.sendall("Log In Success!".encode())
        else:
            connection.sendall("Incorrect User or password!".encode())
    # client_list.append(user.decode())
    while True: 
        data = connection.recv(2048)
        print(str(username.decode()) + " >> " + data.decode())
        if data.decode() == "q":
            connection.close()
            exit()
        connection.sendall(data)


while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client,))
    ThreadCount += 1
    # client_list.append(str(address))
    print('Thread Number: ' + str(ThreadCount))

