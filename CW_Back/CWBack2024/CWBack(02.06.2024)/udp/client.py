import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serv_addr = ('192.168.110.119', 7777)

message = "ДИИИИМООООООООН!"
my_sock.sendto(message.encode('utf-8'), serv_addr)