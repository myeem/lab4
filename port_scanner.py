from progress.bar import IncrementalBar


ports = 65535
result = []

def scanner(socket, hostname):
    progress_line = IncrementalBar('verified', max=ports)
    for i in range(1, ports + 1):
        print(i)
        try:
            progress_line.next()
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connect = client.connect((hostname, i))
            if connect is None:
                result.append(i)
                client.close()
                continue
        except ConnectionRefusedError:
            continue
    progress_line.finish()
    print(f'Открытые порты: {result}')
    return hostname
