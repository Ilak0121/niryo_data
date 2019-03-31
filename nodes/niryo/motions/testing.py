import socket


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1',4000))
    s.listen(1)
    conn, addr = s.accept()
    print("test")
    
