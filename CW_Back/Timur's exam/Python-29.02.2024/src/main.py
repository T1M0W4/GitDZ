import sys
from app import AbcApplication

def main():
    if len(sys.argv) == 1:
        # Запуск в режиме клиента с адресом сервера по умолчанию (localhost)
        app = AbcApplication()
        app.start()
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'server':
            # Запуск в режиме сервера с адресом localhost
            app = AbcApplication(mode='server')
            app.start()
        else:
            # Запуск в режиме клиента с указанным адресом сервера
            app = AbcApplication(hostname=sys.argv[1])
            app.start()
    elif len(sys.argv) == 3:
        if sys.argv[1] == 'server':
            # Запуск в режиме сервера с указанным адресом
            app = AbcApplication(mode='server', hostname=sys.argv[2])
            app.start()
        else:
            print("Usage: python main.py [server] [server_address]")
    else:
        print("Usage: python main.py [server] [server_address]")

if __name__ == "__main__":
    main()
