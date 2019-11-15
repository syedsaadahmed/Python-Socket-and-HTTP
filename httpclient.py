import socket
import sys

print('---------------------------')
url = sys.argv[1]
host = url.split("//")[-1].split("/")[0]
a = url.split("//")[1].split("/")[1:]
seperator = '/'
query_param = seperator.join(a)

server_address = (host, 80)
message  = ('GET /' + query_param + ' HTTP/1.1\r\n').encode()
message += ('Host: ' + host + ':80\r\n').encode()
message += ('Connection: close\r\n').encode()
message += ('\r\n').encode()

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