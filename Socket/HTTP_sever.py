import socket
import threading
import os

WEBROOT = 'webroot'
def handle_client(c, addr):
    print(addr, 'connected!')
    # 读取客户端发来的消息
    with c:
        request = c.recv(1024)

        # Parse HTTP headers
        # 拆分成一行一行的字符串，存放在headers中，HTTP标准中定义的换行符'回车+换行'
        headers = request.split(b'\r\n')
        # 提取请求文件名
        file = headers[0].split()[1].decode()
        # Load file content
        # 若请求的是根路径，直接返回index.html文件
        if file == '/':
            file = 'Socket/index.html'

        # 读取文件的内容
        try:
            with open(WEBROOT + file, 'rb') as f:
                content = f.read()
            response = b'HTTP/1.0 200 OK\r\n\r\n' +content

        except FileNotFoundError:
            response = b'HTTP/1.0 404 NOT FOUND\r\n\r\nFile not found'

        # Send HTTP response
        c.sendall(response)

if __name__ == '__main__':
    # change working directory to script folder
    os.chdir(os.path.dirname((os.path.abspath(__file__))))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 80))
        s.listen()

        while True:
            c, addr = s.accept()
            # 避免程序阻塞，创建一个新的线程，并将客户端的socket c 和地址传递给这个线程
            t = threading.Thread(target=handle_client, args=(c, addr))
            t.start()