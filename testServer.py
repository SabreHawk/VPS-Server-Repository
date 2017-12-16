import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip = '108.61.183.150'
port = 20903
serversocket.bind((host_ip, port))
# 设置最大连接数，超过后排队
serversocket.listen(5)
msg = "received your request"
while True:
    # 建立客户端连接
    (clientsocket,addr) = serversocket.accept()      
    clientsocket.send(msg.encode('utf-8'))
    print("client ip" ,clientsocket.recv(1024).decode('utf-8'))
    clientsocket.close()