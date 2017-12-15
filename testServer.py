import socket
#import sys

# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = '183.206.169.96'
print("连接地址: %s" % str(socket.gethostbyname(host)))
port = 9999

# 绑定端口
serversocket.bind((host, port))
# 设置最大连接数，超过后排队
serversocket.listen(5)
while True:
    # 建立客户端连接
    (clientsocket,addr) = serversocket.accept()      
    clientsocket.send(msg.encode('utf-8'))
    print("client ip" ,clientsocket.recv(1024).decode('utf-8'))
    clientsocket.close()