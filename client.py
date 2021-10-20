import socket
import threading
from port_scanner import scanner
from auth import auth


ask_scan = input('Скан? 1 - да, 0 - нет: ')
hostname = input('Введите имя хоста: ')
if ask_scan == '1':
    hostname = scanner(socket, hostname)

port = int(input('Введите порт: '))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = client.connect((hostname, port))
run = True
while True:
    name = input('Введите имя: ')
    password = input('Введите пароль: ')

    if auth(name, password):
        break


def client_send():
    while True:
        data = input("")
        client.send(f'{name}: {data}'.encode())
        if data.lower() == 'off':
            run = False
            client.close()
            break


def client_recv():
    try:
        while True:
            recv = client.recv(1024)
            print(recv.decode())
    except OSError:
        print('Соединение разорванно')


t1 = threading.Thread(target=client_send)
t2 = threading.Thread(target=client_recv)
t1.start()
t2.start()
