import socket
from _thread import *
from clientFunc import *

host = "127.0.0.1"
port = 1233                   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# user_input = input("Username: ")
# s.sendall(user_input.encode())
# ServerSocket = socket.socket()

LogInSequence(s)

incoming_information = s.recv(2048)
print(incoming_information.decode())

while True:
    msg = input(">> ")
    s.sendall(msg.encode()) 
    
