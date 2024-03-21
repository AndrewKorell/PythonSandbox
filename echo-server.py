import socket 

HOST = "127.0.0.1"

PORT = 65532

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen() #blocking task 
    conn, addr = s.accept()

with conn:
    print(f"connect by {addr}")
    while True :
        data = conn.recv(1024)
        if not data :
            break
        conn.sendall(data)