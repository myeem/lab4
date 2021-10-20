import json


def auth(name: str, password: str) -> bool:
    with open('auth_info.json', 'r') as f:
        information = json.load(f)

    for i in range(len(information)):
        if information[i][0] == name and information[i][1] == password:
            print(f'Добро пожаловать {information[i][0]} {information[i][1]}')
            return True
        elif information[i][0] == name and information[i][1] != password:
            print(f'Неверный пароль')
            return False

    with open('auth_info.json', 'w') as f:
        information.append([name, password])
        data = json.dump(information, f)
    print(f'Учетная запись {name} {password} создана')
    return True


def clear_auth():
    with open('auth_info.json', 'w') as f:
        information = json.dump(list(), f)
