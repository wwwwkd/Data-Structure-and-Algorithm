import socket
import threading

def handle_client(c, addr):
    print(addr, 'connected.')
    while True:
        data = c.recv(1024)
        if not data:
            break
        c.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 1024))
    s.listen()

    while True:
        c, addr = s.accept()

        # 避免程序阻塞，创建一个新的线程，并将客户端的socket c 和地址传递给这个线程
        t = threading.Thread(target=handle_client, args=(c, addr))
        t.start()