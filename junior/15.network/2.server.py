#!/usr/bin/env python

import socket


TCP_IP = '10.135.121.90'
TCP_PORT = 5045
BUFFER_SIZE = 1024
MESSAGE = b'Hello, World!'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)

root@om-test-kibana:~# cat server.py 
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
#server_address = ('192.168.56.1', 5000)
server_address = ('0.0.0.0', 5045)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print(sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print(sys.stderr, 'received "%s"' % data)
            if data:
                #print(sys.stderr, 'sending data back to the client'
                #connection.sendall(data))
                print('data')
            else:
                print(sys.stderr, 'no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()
