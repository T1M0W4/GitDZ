import threading
import time

def work_fun():
    print('Работаю!')
    time.sleep(1)
    print('Работник выполняет задачу')


thread = threading.Thread(target=work_fun)

thread.start()
print('А это основной поток')
