import socket
from clientFunc import *

host = "127.0.0.1"
port = 1233                   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

LogInSequence(s)
incoming_information = s.recv(2048)
print(incoming_information.decode())
MenuSequence(s)



    
