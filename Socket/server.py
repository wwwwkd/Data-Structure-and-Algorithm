import socket
# with python 的语法糖，当离开with块时，执行s.close()来销毁socket4
# 参数1：socket.AF_INET 代表IPv4的地址家族 参数2 socket.SOCK_STREAM 代表使用tcp协议
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 用bind()函数将创建的socket关联到主机的某一个网卡和端口上
    # 其中网卡可以用ip地址指定，这里使用的时"0.0.0.0"特殊地址，代表主机上任意网卡都可以使用这个socket进行通信
    s.bind(("0.0.0.0", 1234))
    # 函数listen()将socket置为监听状态，等待客户端的连接
    s.listen()
    # 函数accept()等待任意客户端连接
    # 返回客户端c 和其 ip地址
    # socket s 主要用于监听，socket c 主要用于与连接的客户端通信
    c, addr = s.accept()
    with c:
        print(addr, 'connected') # 打印客户端的ip地址
        while True:
            # 此循环一直调用recv()函数接收客户端传来的消息 1024代表一次性接收最大长度1024字节
            data = c.recv(1024)
            # 只要不为空，就原封不动的将数据回传给客户端
            if not data:
                break
            c.sendall(data)
