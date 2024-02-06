import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_addr = ('192.168.111.90', 4567)
my_sock.bind(my_addr)

my_sock.accept(10)



client, addr = my_sock.accept()
data = client.recv(2048)
request = data.decode()

print('Ah shit, here we go again!', request)

content ="""
<html>
    <head>
        <title>EEEEE_Rock<title>
    </head>
    <body>
        <h1>Ya obosralsya...</h1>
    </body>
</html>
"""
http_msg = f"""HTTP/1.1 200 OK
Content-Type:text/html
Content-Lenght:{len(content)}
"""


client.send(request.encode('utf-8'))
print(f"Recieved:{data.decode('utf-8')}, from {addr}")

