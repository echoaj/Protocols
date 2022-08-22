import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = b"Hello, World!"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3 way handshake
s.connect((TCP_IP, TCP_PORT))       # SYN (Synchronization)
# 3 way handshake

s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)



