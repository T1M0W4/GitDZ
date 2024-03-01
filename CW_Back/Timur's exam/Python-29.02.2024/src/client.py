import socket
import json

class AbcClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, word):
        """
        Отправляет серверу информацию о слове.
        """
        data = {'word': word}
        msg = json.dumps(data)
        self.sock.sendto(msg.encode('utf8'), (self.host, self.port))

    def connect(self):
        """
        Отправляет запрос на подключение к серверу.
        """
        self.send('hello')

    def end(self):
        """
        Отправляет серверу информацию о завершении игры.
        """
        data = {'gameover': ''}
        msg = json.dumps(data)
        self.sock.sendto(msg.encode('utf8'), (self.host, self.port))

    def receive(self):
        """
        Получает информацию о слове от сервера.
        """
        data, _ = self.sock.recvfrom(1024)
        data = data.decode('utf8')
        data = json.loads(data)
        if 'word' in data:
            return data['word']
        elif 'gameover' in data:
            return ''
        elif 'hello' in data:
            return 'hello'
        else:
            print('Invalid data received from server.')
