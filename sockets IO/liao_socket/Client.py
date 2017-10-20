# -*- coding: utf-8 -*-

# 客户端:创建TCP连接时，主动发起连接的叫客户端

# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket对象就创建成功，但是还没有建立连接
# 建立连接,客户端要主动发起TCP连接，必须带上服务器的IP地址和端口号等参数:
s.connect(('www.sina.com.cn', 80))  # 注意参数是一个tuple，包含地址和端口号
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')  # 发送的文本格式必须符合HTTP标准
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)     # 调用recv(max)方法，recv()返回空数据，表示接收完毕
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接:
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
