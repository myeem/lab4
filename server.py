import socket
import threading
from time import sleep
from logs import set_logs, get_logs, clear_logs
from auth import clear_auth


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 7777))
server.listen(5)
user_addr = {}
user_ignore = {}


def connect():
    while True:
        data, addr = server.accept()
        user_addr.setdefault(addr, data)
        threading.Thread(target=client_connect, args=[data, addr]).start()
        break


def client_connect(data, addr):
    while True:
        try:
            information = data.recv(1024)
            if information:
                print(information)
                print(user_addr)
                set_logs(information.decode())

                if information.decode().lower().split(':')[1].strip() == 'pause':
                    for i in user_addr:
                        if user_ignore.get(i, False) is False:
                            user_addr[i].send(information)
                    sleep(5)
                    continue

                if information.decode().lower().split(':')[1].strip() == 'log':
                    data.send(get_logs().encode())
                    continue

                if information.decode().lower().split(':')[1].strip() == 'log_clear':
                    clear_logs()
                    continue

                if information.decode().lower().split(':')[1].strip() == 'off':
                    print('Сервер больше не принимает соединения')
                    break
                if information.decode().lower().split(':')[1].strip() == 'auth_clear':
                    clear_auth()
                    continue

                for i in user_addr:
                    if user_ignore.get(i, False) is False:
                        user_addr[i].send(information)
            else:
                raise Exception('Client disconnected')
        except Exception:
            for i in user_addr:
                if i == addr:
                    user_ignore.setdefault(i, data)
            data.close()
            break


t2 = threading.Thread(target=connect)
t2.start()
