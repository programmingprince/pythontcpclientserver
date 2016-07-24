#this is a tcp server

import socket

SERVER_IP="127.0.0.1"
PORT=2343
BUFFER_SIZE=1024

#creating a socket object
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=(SERVER_IP,PORT)
s.bind(server_address)
s.listen(1)
connection, clientAddr=s.accept()
print("Got connection request from: ",clientAddr)
data=connection.recv(BUFFER_SIZE)
content=data.decode("utf-8")
print('Client:',content)
data=input('Enter any text to send...')
connection.send(data.encode(encoding="utf-8"))
connection.close()