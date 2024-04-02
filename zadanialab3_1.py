def zad1():
    working = True
    while(working == True):
        x = int(input("Wprowadź liczbę całkowitą x"))
        y = int(input("Wprowadź liczbę całkowitą y"))
        if x == 0 or y == 0:
            break
        else:
            print(f"Twój wynik to: {x*y}")

#zad1()

def zad2():
    hasla = ("python", "pajton")
    haslo = input("Podaj hasło: ")
    if haslo in hasla:
        print("Witaj Krzysztof Kowalewski")
    else:
        print("Błędne hasło!")
#zad2()

import random


def zad3():
    random_num = []
    for i in range(1, 100):
        random_num.append(random.randint(1,100))
    random_num.sort()
    for element in random_num:
        if element % 2 == 0:
            print(element)


#zad3()


def zad4():
    hasla = ("python", "pajton")
    haslo = input("Podaj hasło: ")
    print("Witaj Krzysztof Kowalewski") if haslo in hasla else print("Błędne hasło!")

#zad4()



def zad5_simple(x,y,z):
    result = 0
    result = (x/y)/z
    print(result)

#def zad5_one_line(x,y,z):

result_lambda5 = lambda x,y,z: (x/y)/z

#zad5_simple(5,6,7)

#print("Funkcja lambda " ,result_lambda(5,6,7))

name = ['K','r', 'z', 'y', 's', 'z', 't', 'o', 'f']
result_lambda6 = lambda name: "".join(name)
#print(result_lambda6(name))


credentials = 'KrzysztofKowalewski'
result_lambda7 = lambda names: f'Na wyrazy: {names.split()} , a następnie na litery {list(names)}'
#cred_list = list(credentials)
#print(cred_list)
print(result_lambda7(credentials))



import functools, operator

# result_lambda8 = lambda word, letter: word.find(letter)
# print(f"Indeks znalezionej litery to: {result_lambda8('zdanie','a')}")

# users_info = {}
# login_list = []
# password_list = []
# login = ''
# password = ''
# while True:
#     login = input("Podaj login lub wpisz 'STOP' aby przerwać: ")
#     if login == 'STOP':
#         break
#     login_list.append(login)
    
#     password = input("Podaj hasło: ")
#     if password == 'STOP':
#         break
#     password_list.append(password)
    

# for index, (login, password) in enumerate(zip(login_list, password_list)):
#     users_info[login] = password



from users_info import users_info


zad10 = users_info()
print("Utworzono słownik z danymi logowania:")
print(zad10)

from stars import Poziom, Pion

def rysuj_E():
    Poziom(5)
    Pion(1)
    Poziom(5)
    Pion(1)
    Poziom(5)


def rysuj_L():
    Pion(5)
    Poziom(5)

rysuj_E()
print('\n')
rysuj_L()

from sil import silnia

def zad11():
    n = int(input("Wprowadz liczbę n: "))
    k = int(input("Wprowadź liczbę k: "))

    symbol_newtona = silnia(n)/(silnia(k)*silnia(n-k))

    print(symbol_newtona)

#symbol_newtona()

def zad12():
    test_object = []
    for i in range(100):
        test_object.append(random.randint(1,100))
    test_object.sort()

    result_lambda12 = lambda x: True if x%2 != 0 else False
    result_filter = filter(result_lambda12,test_object)
    print(list(result_filter))

#zad12()

def zad13():
    num_list = []
    for i in range(1,100):
        num_list.append(i)

    num_list_smol = [2,4,6,8,12]
    #print(num_list)
    multiply = lambda x,y: x*y

    result = functools.reduce(multiply, num_list, 1)
    result_smol = functools.reduce(multiply,num_list_smol, 1)
    print(result)
    print(result_smol)

#zad13()

def zad14_easy():
    test_object = [567,700,574]

    for i in range(10):
        test_object.append(random.randint(1,100))

    for i in test_object:
        if i % 7 == 0 and (i*5) >= 2000 and (i*5) <= 3200:
            print(i, end=" ")

#zad14_easy()

def zad14():
    dividing_7 = lambda x: True if x%7 == 0 else False
    multiply1 = lambda x: True if x*5 >= 2000 else False
    multiply2 = lambda x: True if x*5 <= 3200 else False
    test_object = [567,700,574]

    for i in range(10):
        test_object.append(random.randint(400,1000))
    
    for i in test_object:
        if dividing_7(i) == True and multiply1(i) == True and multiply2(i) == True:
            print(i, end=" ")
    print('\n')
    
zad14()


def zad15():
    rysuj_E()
    print('\n')
    rysuj_L()

zad15()
