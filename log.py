import socket
import threading
import os


def log_file (host):
    log_filename = f"{host}_syslog.log"
    log_mode = 'a' if os.path.exists(log_filename) else 'w'  # 判断日志文件是否存在
    log_file = open(log_filename, log_mode)
    return log_file

def handle_client(client_socket, client_address):
    # 获取客户端的主机名
    host = client_address[0]

    # 检查是否存在该客户端的日志文件

    while True:
        # 接收客户端发送的数据
        data = client_socket.recv(1024)
        #print(data)
        if not data:
            break

        # 处理接收到的数据
        message = data.decode('utf-8')
        #print(message)
        log_message = f"收到来自 {host} ({client_address[0]}) 的消息：{message}"
        print(log_message)

        # 将日志写入文件
        log_file(host=host).write(log_message + '\n')

    # 关闭客户端连接
    print(f"与客户端 {client_address} 断开连接")
    log_file.close()
    client_socket.close()

def syslog_server(address, port):
    # 创建UDP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 10)
    server_socket.bind((address, port))
    print(f"Syslog服务器已启动，监听地址：{address}，端口：{port}")

    while True:
        # 接收客户端发送的数据
        data, client_address = server_socket.recvfrom(1024)

        # 处理客户端连接的线程
        client_thread = threading.Thread(target=handle_client, args=(server_socket, client_address))
        client_thread.start()

# 指定服务器监听的地址和端口
address = '192.168.1.2'  # 监听所有网络接口
port = 514

# 启动Syslog服务器
syslog_server(address, port)