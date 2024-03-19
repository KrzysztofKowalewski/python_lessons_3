################ Methods versus function (metoda vs funkcja)
#### Example
# a = [2, 70, 5, 6]
# a.sort()   # wywołanie metody na obiekcie
# print(a)

# a = [2, 70, 5, 6]
# a = sorted(a)  # override of a variable (nadpisanie zmiennej)
# print(a)

###### Generally, methods and functions have one or more parameters
###### (Metody i funkcje często mają jeden lub więcej parametrów)

#### Example
# a = [2, 70, 5, 6]
# a.sort(reverse=True)
# print(a)
#
# a = [2, 70, 5, 6]
# a = sorted(a, reverse=True)  # override of a variable
# print(a)

######## Function: break() and continue()
## the break() function is often used to stop loops (for, while)
## the continue() function allows to leave a block of instructions and return to the beginning of the loop

## Funkcja break() jest używana często do zakończenia pętli (for, while)
# podczas gdy funkcja continue() pozwala opuścić blok instrukcji i wrócić do początku pętli.

#### Example: the program only prints the numbers 0 1 2 3 4

# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# licz = 0
# while licz in list_1:
#     print(list_1[licz]),
#     licz += 1  # licz = licz + 1
#     if licz >= 5:
#         break

####### Example: the program prints out only odd numbers: 1 3 5 7 9
# for x in range(1, 10):
#     if x % 2 == 0:  # Sprawdź, czy x jest parzystą liczbą
#         continue
#     print(x)


# # ################################ Task 1
## Write a program using if statement, for loop, break(), continue() which takes 2 digits: x, y as input and
###### calculate multiplication x*y. The program stops working if x or y is equal to 0.
## Korzystając z instrukcji sterujących napisz program który będzie wczytywał kolejno z klawiatury 2 liczby,
## a następnie obliczał i wyświetlał na ekranie iloczyn wprowadzonych przez użytkownika liczb,
## program kończy działanie jeżeli uzytkownik wprowadzi cyfrę 0. Użytkownik może wykonać obliczenia tylko na
## liczbach całkowitych (wstaw odpowiedni warunek).

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




## # ################################ Task 2
## Napisz program, który wyświetli twoje imię i nazwisko jeżeli użytkownik poda
## właściwe hasło, jedno z 2 do wyboru, (hasła są przechowywane w krotce)

def zad2():
    hasla = ("python", "pajton")
    haslo = input("Podaj hasło: ")
    if haslo in hasla:
        print("Witaj Krzysztof Kowalewski")
    else:
        print("Błędne hasło!")
#zad2()

## Write a program that will display your name if the user enters the correct
## password (the password is stored in a variable)

############################## Python module random
## Random module implements pseudo-random number generators for various distributions.

### Example:  random - returns a random float number between 0 and 1
# import random     # generator liczb losowych
# print(random.sample(range(10000),4))
# print(random.choice(range(10000)))

################################## Task 3
## Generate list with 100 random numbers (integer type)
## Ascending sort these odd numbers and print only odd numbers from list.

## Wygeneruj listę złożoną z 100 liczb całkowitych parzystych i nieparzystych
## wypisz wszystkie liczby parzyste z tablicy liczby, od najmniejszej do największej.
## Do losowania liczb wykorzystaj moduł random patrz przykład poniżej

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

#################### One line if/else statement in Python
########### Example
## Syntax/Składnia: <expression1> if <condition> else <expression2>
## Option 1
# a = 20
# b = 1
# print('większe') if a > b else print('mniejsze')

# Option 2
# a = 1
# b = 20
# x = a > b and print('większe') or print('mniejsze')

# Option 3
# age = 21
# print(('adult', 'kid')[age < 20])  # choice from the tuples

# Option 4
# age = 21
# print(('adult', 'kid')[True])

############### Task 4
## Uprość kod z Zadania 2 korzystając w w/w struktur
## Simplify the code from Task 2 using a one line if/else statement


def zad4():
    hasla = ("python", "pajton")
    haslo = input("Podaj hasło: ")
    print("Witaj Krzysztof Kowalewski") if haslo in hasla else print("Błędne hasło!")

#zad4()


################################## Python function
## Syntax: def function_name(input_argument1, input_argument2, ... ,input_argumentN):
##       instructions
##      return output_argument   or  return output_arguments
##
##
## Calling the function (wywołanie funkcji )
## name_function(value of input_argument1, ... ,value of input_argumentN)

### Example

# def sum_numbers(x, y):
#     sum_xy = x + y
#     return sum_xy

# print('Result is equal:', sum_numbers(3,5))

#################### Task 5
## Write a function that calculates the quotient of 3 even numbers
## Utwórz funkcje która obliczy iloraz 3 parzystych liczb, użyj "one line statement"


def zad5_simple(x,y,z):
    result = 0
    result = (x/y)/z
    print(result)

#def zad5_one_line(x,y,z):
# result_lambda5 = lambda x,y,z: (x/y)/z

# zad5_simple(5,6,7)

# print("Funkcja lambda " ,result_lambda(5,6,7))

####################  Python function:  anonymous function lambda()
#########  Funkcja anonimowa lambda()
## Syntax:     lambda input_arguments: instruction

################# Example
# resultLambda1 = lambda x, y: x + y
# print('Wynik wywołania funkcji lambda:', resultLambda1(3,5))
################# Example
# name = 'Ala'
# resultLambda2 = lambda oneWord: oneWord.upper()
# print(resultLambda2(name))

# ########################## Task 6
# Utwórz listę złożoną z pojedynczych liter swojego imienia następnie korzystając
# z funkcji lambda połącz kolejne litery w jeden wyraz (swoje imie)

# name = ['K','r', 'z', 'y', 's', 'z', 't', 'o', 'f']
# result_lambda6 = lambda name: "".join(name)
# print(result_lambda6(name))


# ########################## Task  7
# Przypisz do zmiennej wartość która będzie twoim imieniem i nazwiskiem następnie korzystając
# z funkcji lambda rozdziel zdanie na poszczegolne wyrazy, a potem wyrazy na litery
# użyj funkcji list i metody split - dla zmiennych typu string


# credentials = 'KrzysztofKowalewski'
# result_lambda7 = lambda names: f'Na wyrazy: {names.split()} , a następnie na litery {list(names)}'
# #cred_list = list(credentials)
# #print(cred_list)
# print(result_lambda7(credentials))


##############################################################
######### Function:  map(), zip(), reduce() i filter()

####### Function map()##################
## Funkcja map() wykonuje operacje z użyciem funkcji na każdym elemencie listy/tupli/słownika:
## Syntax: map(function_name, iter)
## function_name - name of function with one input parameter
## iter is list or dictionary or tuples
## output parameter of mam is list type.
## map() realize operation by using function on each elements of list/tuple/dictionary

######### Example: construct your own function + map()

# def power(number):
#     result = number**2
#     return(result)
#
# list_number = [2, 10, 15, 100, -5]  # equivalent to [double(n) for n in listNumber]
# result_map = map(power, list_number)

# print(list(result_map))  # dump to list

######### Example: construct lambda() + map()

# list_word = ['dnA','RnA']
# print(list_word)
# upper_letter = lambda one_word: one_word.upper()
# result_lambda = map(upper_letter, list_word)  # equivalent to map(lambda one_word: one_word.upper(), list_word)
# print('Result: ', list(result_lambda))

##### Function zip()##########################################################################
# zip() creates pair of elements (tuples) from two list
# zip() tworzy za to listę tupli z podanych elementów

######### Example
# list1 = [1,3,5]
# list2 = [2,4,6]
# resultZip = zip(list1, list2)
# print(list(resultZip))

##### Function reduce()######################################################################
## Funkcja reduce() pobiera dane z sekwencji i zwraca na ich podstawie pojedynczą
## wartość np. sumę liczb. Struktura: functools.reduce(function0, sequence, [initial_value]);
## reduce() realizuje operacje zdeklarowane w function0 na pierwszych dwóch elementów sekwencji, następnie
## wykonuje function0 dla wyniku i trzeciego elementu, aż do wyczerpania elementów sekwencji
## Znajduje się w pakiecie functools

## The reduce(fun,seq) function is used to apply a particular function passed
## in its argument to all of the list elements mentioned in the sequence passed along.
## This function is defined in “functools” module.

######## Example
import functools, operator
# resultLambda1 = lambda x, y: x + y
# list1 = [1,2,3,4]
# resultReduce1 = functools.reduce(resultLambda1, list1,0)
# print(resultReduce1)

######## Example
## np.można wykorzystywać szereg operacji z użyciem wbudowanych funkcji
## You can use the following operations available as a function:
## Math operations: add(), sub(), mul(), floordiv(), abs()
## Logical operations: not_(), truth()
## Bitwise operations: and_(), or_(), invert()
## Comparisons: eq() -> equal to, ne() -> not equal, lt()->less than,
## le()-less or equal, gt() -> greater than, and ge() -> greater or equal
## Object identity: is_(), is_not()

# import functools, operator
# list2 = [1,2,3,4]
# resultReduce2 = functools.reduce(operator.mul, list2, 1)
# print(resultReduce2)


##### Function filter()########################################################
##Funkcja filter filtruje elementy sekwencji przy użyciu podanej funkcji,
## która musi zwracać wartość True lub False:

## The filter() method filters the given sequence with the help of a function
## that tests each element in the sequence to be true or not.
## Syntax: filter(function, sequence)

######### Example
# list1 = [1,2,3,4]
# def even(x):
#  if x%2 == 0:
#     return True
#  else:
#     return False

# resultFilter = filter(even, list1)
# print(list(resultFilter))

########### Function enumerate
## Enumerate() adds a counter to an iterable and returns it in the form of the enumerating object.
##
# def main():
#     print("#### function enumerate ###")
#     a = ['a', 'b', 'c']
##    b = [(0, 'a'), (1, 'b')] # sprawdź poniższe również dla zmiennej b
#
#     for i in enumerate(a):
#         print(i)        # [(0, 'a'), (1, 'b')]
#
#     print("#######")
#     for i in enumerate(a):
#         for j in i:
#             print('j element:', j)
#     print("#######")
#     for i in enumerate(a):
#         for j in i[1]:
#             print('j element:', j)
#
# if __name__ == '__main__':
#     main()



# ########################## Task 8
# # Utwórz funkcję która w dowolnym wyrazie (1 argument funkcji)
# # znajdzie dowolną literę (2 argument funkcji)
## użyj lambda


# result_lambda8 = lambda word, letter: word.find(letter)
# print(f"Indeks znalezionej litery to: {result_lambda8('zdanie','a')}")

# ########################## Task 9
## Utwórz dwie listy, do każdej z nich niezależnie zapisuj odpowiednio
## podawane przez użytkowników login (pierwsza lista) i hasło (druga lista),
## operacja zapisu jest powtarzana aż do momentu wpisania przez użytkownika "STOP"
## użyj break, continue, enumerate().
## Następnie login-y i hasła zapisz do słownika (login to klucz słownika).


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



# ########################## Task 10  - Module in Python
# # # Zmodyfikuj poprzednie zadanie, tworząc a następnie importując moduł
# # #Utwórz funkcje Poziom: która rysuje gwiazdki poziomo, liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # #Utwórz funkcje Pion: która rysuje gwiazdeki pionowo, liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # obie funkcje są z modułu o nazwie stars

# zad10 = users_info()
# print("Utworzono słownik z danymi logowania:")
# print(zad10)

from stars import Poziom, Pion

# liczba_gwiazdek = int(input("Podaj liczbę gwiazdek: "))
# print("Gwiazdki w poziomie:")
# Poziom(liczba_gwiazdek)

# print("Gwiazdki w pionie:")
# Pion(liczba_gwiazdek)

# # Korzystając z modułu stars i funkcji Pion Poziom wypisz litery: E, L

def rysuj_E():
    Poziom(5)
    Pion(1)
    Poziom(5)
    Pion(1)
    Poziom(5)


def rysuj_L():
    Pion(5)
    Poziom(5)

# rysuj_E()
# print('\n')
# rysuj_L()


# ########################## Task 11
# # utwórz moduł o nazwie sil, w którym znajdzie się funkcja silnia (użyj lammbda), a następnie korzystając z
# modułu sil, oblicz symbol Newtona dla dowolnych 2 liczb wskazanych przez
# użytkownika(http://www.fizykon.org/wzory/wzory_matem_kombinatoryka.htm)

from sil import silnia

def zad11():
    n = int(input("Wprowadz liczbę n: "))
    k = int(input("Wprowadź liczbę k: "))

    symbol_newtona = silnia(n)/(silnia(k)*silnia(n-k))

    print(symbol_newtona)

#symbol_newtona()

# ########################## Task 12
# # Write a script to filter out only the even items from a list (i.e. made from range(1, 100))
# # using filter() and lambda functions.
# #  The numbers obtained should be printed in a comma-separated sequence on a single line.

def zad12():
    test_object = []
    for i in range(100):
        test_object.append(random.randint(1,100))
    test_object.sort()

    result_lambda12 = lambda x: True if x%2 != 0 else False
    result_filter = filter(result_lambda12,test_object)
    print(list(result_filter))

#zad12()


# ########################## Task 13
#### Write a script, using reduce(), which will multiply elements in range (1, 100)

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

# ########################## Task 14
### Write a program which will find all such numbers which are
### divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included)

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
    

# ########################## Task 15
#  # # Utwórz funkcje Poziom: która rysuje gwiazdki poziomo, liczbę gwiazdek podaje użytkownik
##### jako argument funkcji
# # # Utwórz funkcje Pion: która rysuje gwiazdki pionowo,
# ### liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # # Korzystając z w/w funkcji narysuj litery: E, L

def zad15():
    rysuj_E()
    print('\n')
    rysuj_L()

zad15()