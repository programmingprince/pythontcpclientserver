# this is a tcp client

import socket

SERVER_IP = "127.0.0.1"
PORT = 2343
BUFFER_SIZE = 2048

# creating socket object for client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (SERVER_IP, PORT)
s.connect(server_address)
data = input('Enter any text to send...')
s.send(data.encode(encoding="utf-8"))
data = s.recv(BUFFER_SIZE)
content = data.decode("utf-8")
print('Server:', content)
s.close()
