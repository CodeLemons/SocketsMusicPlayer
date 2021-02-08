import socket

def LogInSequence(serverSocket):
    print('Username > ')
    username = input()
    serverSocket.sendall(username.encode())
    print('Password > ')
    password = input()
    serverSocket.sendall(password.encode())
    
