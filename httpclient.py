
# import socket
# s=socket.socket()
# host=socket.gethostbyname('www.google.com')
# port=80
# s.connect((host,port))
# s.sendall(b"GET /\r\n")
# # output = "GET /\r\n"
# # s.sendall(output.encode('utf-8'))
# val = s.recv(100000000)
# # Split off the HTTP headers
# #val = val.split('\r\n\r\n',1)[1]
# # #print(val)
# while (len(val) > 0):
#     #print(val)
#     val = s.recv(10000)
# print(type(val.decode("utf-8")))
# val = val.decode("utf-8")
# headers = val.split('\r\n\r\n', 1)[0]
# body = val.split('\r\n\r\n', 1)[-1]
# print(body)



# import socket
# s=socket.socket()
# host=socket.gethostbyname('west.uni-koblenz.de/')
# port=80
# s.connect((host,port))
# #s.sendall(b"GET /\r\n")
# s.sendall(b'GET /studying/ws1819/webscience HTTP/1.1\r\n\r\n')
# #val = s.recv(100000000)
# def recvall(sock):
#     data = b''
#     bufsize = 409600
#     while True:
#         packet = s.recv(bufsize)
#         data += packet
#         if len(packet) < bufsize:
#             break
#     return data

# data = recvall(s)
# print(type(data.decode("utf-8")))
# data = data.decode("utf-8")
# headers = data.split('\r\n\r\n', 1)[0]
# body = data.split('\r\n\r\n', 1)[-1]
# print(headers)




import socket

server_address = ('west.uni-koblenz.de', 80)
message  = b'GET /studying/ws1819/webscience HTTP/1.1\r\n'
message += b'Host: west.uni-koblenz.de:80\r\n'
message += b'Connection: close\r\n'
message += b'\r\n'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
sock.sendall(message)

data = b''
while True:
    buf = sock.recv(1024)
    if not buf:
        break
    data += buf

sock.close()
data = data.decode("utf-8")
headers = data.split('\r\n\r\n', 1)[0]
body = data.split('\r\n\r\n', 1)[-1]

print(headers)

with open("output.php", "w") as output_file:
    output_file.write(body)
