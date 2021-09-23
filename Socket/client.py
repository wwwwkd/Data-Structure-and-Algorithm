import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # 直接connect 传入服务端的ip地址，和端口号
    s.connect(("127.0.0.1", 1234))
    # 向服务端发送数据，发送的不是字符串，而是一个字节序列，前面夹b
    s.sendall(b'hello, Ross!')
    # 调用recv()函数接收服务器的消息
    data = s.recv(1024)
    # 结果打印
    print('Received:', repr(data))
