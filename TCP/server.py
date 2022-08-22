import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)


# 3 way handshake
conn, addr = s.accept()         # Returns (socket object, address info)
# 3 way handshake

print('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        print("No data received")
        break
    msg = data.decode('utf-8')
    print("received data:", msg)
    conn.send(data)  # echo
conn.close()
