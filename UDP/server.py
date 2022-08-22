import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = s.recvfrom(1024)    # buffer size is 1024 bytes
    msg = data.decode('utf-8')
    print("received message:", msg)


# UDP does not have a connection, it is a connectionless protocol.
# It doesn't care if the messages are received or not.
