import socket

def LogInSequence(serverSocket):
    print('Username > ')
    username = input()
    serverSocket.sendall(username.encode())
    print('Password > ')
    password = input()
    serverSocket.sendall(password.encode())

def MenuSequence(serverSocket):
    print('|Developer Mode|\n'
          '1. List Songs\n'
          '2. Download Song\n'
          '3. Quit')
        
    choice = input(">> ")
    serverSocket.sendall(choice.encode())
    incoming_information = serverSocket.recv(2048)
    print(incoming_information.decode())


    
