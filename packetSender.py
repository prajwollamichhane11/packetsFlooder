import socket
import random
import time

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to Connect")
    sys.exit();

print("Socket Created")

host = input()
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("Hostname could not be received")
    sys.exit()

print ("IP Address: "+ remote_ip)

s.connect((remote_ip,port))

print("Socket Connected to"+ host + "using IP" + remote_ip)

message = "GET/HTTP/1.1\r\n\r\n"

try:
    s.sendall(message.encode())
except socket.error:
    print("Did not Send Successfully")
    sys.exit()

print("Message Sent Successfully")

reply = s.recv(4096)

print(reply.decode())

s.close()
