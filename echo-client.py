import socket 

HOST = "127.0.0.1"
PORT = 65532

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(b"Hello, World")  #b means data sent in 8-bit units 
    data = s.recv(1024)

print(f"Received {data}")
