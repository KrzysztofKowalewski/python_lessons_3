def users_info():
    users_info = {}
    login_list = []
    password_list = []
    login = ''
    password = ''
    while True:
        login = input("Podaj login lub wpisz 'STOP' aby przerwać: ")
        if login == 'STOP':
            break
        login_list.append(login)
        
        password = input("Podaj hasło: ")
        if password == 'STOP':
            break
        password_list.append(password)
        

    for index, (login, password) in enumerate(zip(login_list, password_list)):
        users_info[login] = password


    print("Utworzono słownik z danymi logowania:")
    print(users_info)

    return users_info