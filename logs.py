def set_logs(data):
    with open('logs.txt', 'a') as f:
        f.write(f'{data}\n')


def get_logs():
    with open('logs.txt', 'r') as f:
        return f.read()


def clear_logs():
    with open('logs.txt', 'w') as f:
        f.write('')
