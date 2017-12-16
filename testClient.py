
# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# 获取本地主机名
host = '108.61.183.150'
# 设置端口好
port = 20903
# 连接服务，指定主机和端口
s.connect((host, port))
# 接收小于 1024 字节的数据
msg = s.recv(1024)
s.send(str(s.getpeername()).encode('utf-8'))
s.close()

print (msg.decode('utf-8'))