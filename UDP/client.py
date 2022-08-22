import socket


UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

# Create a UDP socket  ( internet, UDP )
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

# Close the socket
# sock.close()
