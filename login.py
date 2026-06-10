def login(username, password):
    if username == "admin" and password == "1234":
        return "Добро пожаловать"
    else:
        return "Ошибка входа"
