import socket


class Listener:
    addr = ()
    sock = None
    running = False


    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        self.addr = (ip, port)
        self.sock.bind(self.addr)


    def worker(self):
        while self.running:
            data, addr = self.sock.recvfrom(1024)
            message = data.decode('utf8')
            self.controller.on_message_received(message, addr[0])