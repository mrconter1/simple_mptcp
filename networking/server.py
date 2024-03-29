import os
import sys
import socket
import struct

print("Creating socket...")
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 262)
    print("Using mptcp...")
except:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Using tcp...")

server_socket.settimeout(None)

buffer_size = 65536  # Adjust this value as needed
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, buffer_size)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, buffer_size)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("10.0.2.2", 12345))
server_socket.listen()

#print("Server is listening on localhost:12345...")

client_socket, client_address = server_socket.accept()
#print("Accepted connection from", client_address)

data = client_socket.recv(1024)

data_request_size = struct.unpack("<Q", data)[0]
#print("Received requested data size:", data_request_size)

random_bytes = os.urandom(data_request_size)
print(len(random_bytes))
client_socket.sendall(random_bytes)
#print("Replying with", data_request_size, "number of bytes")

client_socket.close()
server_socket.close()
