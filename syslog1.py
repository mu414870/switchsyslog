import socket
import threading
import os
import pymysql

def handle_client(client_socket, client_address):
    # 获取客户端的主机名
    host = client_address

    # 连接数据库
    conn = pymysql.connect(
        host='192.168.99.141',
        user='root',
        password='LhL20020218@',
        database='syslog'
    )
    cursor = conn.cursor()

    # 创建日志表（如果不存在）
    cursor = conn.cursor()

    # 根据连接地址作为表名创建日志表（如果不存在）
    table_name = client_address[0]
    cursor.execute(f"CREATE TABLE IF NOT EXISTS `{table_name}` (id INT AUTO_INCREMENT PRIMARY KEY, message TEXT)")

    while True:
        # 接收客户端发送的数据
        data = client_socket.recv(1024)
        if not data:
            break

        # 处理接收到的数据
        message = data.decode('utf-8')
        log_message = f"收到来自 {host} ({client_address[0]}) 的消息：{message}"
        print(log_message)

        # 将日志插入到对应的连接地址表中
        cursor.execute(f"INSERT INTO `{table_name}` (message) VALUES (%s)", (message,))
        conn.commit()

    # 关闭数据库连接
    conn.close()

    # 关闭客户端连接
    print(f"与客户端 {client_address} 断开连接")
    client_socket.close()

def syslog_server(address, port):
    # 创建UDP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 10)
    server_socket.bind((address, port))
    print(f"Syslog服务器已启动，监听地址：{address}，端口：{port}")

    while True:
        # 接收客户端发送的数据
        data, client_address = server_socket.recvfrom(1024)

        # 处理客户端连接的线程
        client_thread = threading.Thread(target=handle_client, args=(server_socket, client_address))
        client_thread.start()

# 指定服务器监听的地址和端口
address = '0.0.0.0'  # 监听所有网络接口
port = 514

# 启动Syslog服务器
syslog_server(address, port)
