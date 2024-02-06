import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_addr = ('localhost', 4567)

my_sock.bind(my_addr)

msg = ''
while msg != 'exit':
    data, addr = my_sock.recvfrom(1024)
    print(f"Получили: '{data.decode('utf-8')}' от {addr}")

