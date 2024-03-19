'''
###################################################################################################################
Dziś zajęcia dotyczą tworzenia funkcji ze zmienną liczbą argumentów wejściowych.
Przed realizacją zadań koniecznie zapoznaj się ze slajdami prezentacji do Wykładu 3 

Dodatkowe linki do filmów, które ułatwią Ci zrozumienie materiału z laboratorium:
"Co oznacza zapis *args oraz **kwargs w funkcjach?"   -  https://www.youtube.com/watch?v=7nwXBWzkqNU
####################################################################################################################

'''
##################################### Zadanie 0   na rozgrzewkę ##################
## Utwórz funkcję o nazwie "Rozprawka.py", która będzie wyświetlała,
## na ekranie napis "to poprostu jest wspaniałe i niesamowite, musisz to zobaczyć",
## następnie używając w/w funkcji napisz tekst reklamujący, opisujący jeden z 7 Cudów świata gdzie 
## wywołasz tą funkcję w tekście minimum 3 krotnie
######################################################################################################################

############################### Teoria: Funkcja z dowolną liczbą argumentów wejściowych (*args)  #########################
### def nazwa_funkcji(*args):
###    instrukcje
##     return obiekt                 *args - krotka argumentów pozycyjnych

###### Wyrażenie “args” bierze się z od słowa “arguments” czyli argumenty i jest to zazwyczaj zmienna,
###### która zawiera tuple argumentów pozycyjnych. Wyrażenia z jedną gwiazdką (*) używamy gdy do funkcji
### chcemy przekazać dowolną liczbę argumentów pozycyjnych (czyli takich dla których
### przy wywołaniu funkcji nie podajemy ich nazwy, a przypisanie wartości bazuje na kolejności argumentów dlatego
### args - argumenty umieszczane są w krotce/tupli po której możemy iterować args[0], args[1] itd.
## używamy *args gdy nie są istotne dla nas nazwy zmiennych
### Pamiętaj aby parametr *args umieszczać na końcu listy parametrów w definicji funkcji!


################################## Przykład 1  suma dowolnego ciągu cyfr
# def suma(*args):
#     if not args:                        # wkazane jest kontrolowanie przypadku braku argumentów
#         return('brak argumentów')
#     return(sum(args))
#
# print(suma(1,2,3))
# print(suma(1,2,3,4,5,6))


################################### Przykład 2:  suma dowolnego ciągu cyfr plus wartość stałej
# def suma2(x,*args):
#     sumaLiczb = x + sum(args)
#     return(sumaLiczb)
#
# print(suma2(100,1,2,3))

#################################### Przykład 3:  suma pierwszych 4 cyfr dowolnego ciągu cyfr
# def suma3(*args):
#     if bool(args):
#         sumaLiczb = args[0] + args[1] + args[2] + args[3]
#     else:
#         sumaLiczb = 0
#     
#      print(sumaLiczb)
#     return(None)
#
# suma3(1,2,3,4,5,6,7,8,9,10)
# suma3()

#########################################################################################################
#############funkcje z dowolną liczbą argumentów kluczowych (**kwargs) ############
### ** kwargs pozwala przekazywać zmienną długość argumentów ze słowami kluczowymi do funkcji.
### W przypadku gdy do naszej funkcji chcemy przekazywać argumenty, które wyróżniają
### się nazwą możemy użyć parametru z dwoma gwiazdkami (**).
### Przekazane w ten sposób argumenty są dostępne w funkcji w postaci słownika.
### Jego pary klucz-wartość stanowią nazwa i wartość przekazanego argumentu.
### używamy **kwargs gdy istotna dla nas jest nazwa zmiennych

# def nazwa_funkcji(**kwargs):
#     instrukcje
#     return obiekt                 # kwargs - słownik argumentów kluczowe

######## wstaw jako argument funkcji:  *kwargs  ########################################

## “kwargs” z j.ang. “keyword arguments” czyli argumenty nazwane
## i zmienna taka zawiera pary nazwa-wartość argumentu.

## Przykład
# def slownik(**kwargs):
#    for klucz, wartosc in kwargs.items():
#        print(klucz, wartosc)
#
# slownik(a=1, b=2, c=3)

# def witaj(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))
#
# witaj(name="yasoob")

########################################## Zapamiętaj:
#### 1. “args” i “kwargs” możesz zastąpić dowolnymi innymi nazwami zmiennych
#### 2. Pamiętaj umieszczając w definicji funkcji wyrażenie z jedną lub dwoma gwiazdkami
### pozwalamy na przekazywanie do niej argumentów w dowolniej liczbie i nazwie.
### bez konieczności konkretnego określenia tych parametrów.
### 3. Pamiętaj o kolejności – wyrażenie z dwoma gwiazdkami
### musi być na końcu, z jedną gwiazdką wcześniej, a pozostałe zdefiniowane argumenty na początku.


#### Gwiazdek możesz również używać w wywołaniu funkcji.
#### Jest to tak zwane rozpakowywanie list i słowników z argumentami.
#### Jeżeli funkcja przyjmuje kilka argumentów i posiadasz listę,
#### która zawiera argumenty, które chcesz przekazać do tej funkcji
#### wystarczy poprzedzić nazwę listy gwiazdką zamiast podawać kolejne argumenty ręcznie.

# list_arg = [1, 3, 5]
#
# def rozpakowywanie(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#
#
# rozpakowywanie(*list_arg)     # odpowiednik dużo dłuższego kodu:   rozpakowywanie(list_arg[0], list_arg[1], list_arg[2])
############################################################################################################################################

################################   Zadania do realizacji
## Zadanie 1
# Utwórz 1 funkcje wielu-zmiennych wejściowych, która obliczy wartość wyrażenia
## dla dowolnego jednego argumentu wejściowego, x^x
## dla dowolnych dwóch argumentów wejściowych  x^x, 
#dla pozostałych przypadków wyświetli komunikat, że jest błąd.

def zad1(*args):
    if len(args) == 1:
        result = args[0]**args[0]
    elif len(args) == 2:
        result = args[0]**args[1]
    else:
        print("Wystąpił błąd!")
        exit()
    print(result)

#zad1(2,3)


######### Zadanie 2
## Wczytaj poniższy fragment tekstu opisujący komputer
## Napisz funkcję która ustali liczbę występujących w tym tekście wyrazów wskazanych przez użytkownika
## ciąg nazw i liczba wyszukiwanych wyrazów podanych przez użytkownika jest dowolna,
## niemniej w tekście są wyrazy o nazwach kluczowych i potencjalnie zawsze ważnych
### dla innych użytkowników np. komputera, skaner, uwzględnij je w wyszukiwaniu.

text = 'Wczytywanie do komputera tekstów, ilustracji, fotografii, itp. jest '   \
       'możliwe dzięki urządzeniom zewnętrznym zwanym skanerami. Skaner to ' \
       'urządzenie umożliwiające wprowadzenie do komputera grafiki i tekstu. ' \
       'Dzięki zamianie skanowanej płaszczyzny na postać cyfrową może ona zostać ' \
       'wyświetlona na ekranie monitora i zapisana na dysku w odpowiednim formacie ' \
       'oraz może zostać poddana komputerowej obróbce. Skanery dzielimy na dwie podstawowe ' \
       'grupy: ręczne (np. czytniki kodów paskowych) oraz stacjonarne. Najpopularniejszym ' \
       'typem skanerów są skanery stacjonarne płaskie, które umożliwiają skanowanie ' \
       'dokumentów o formacie A3 lub A4 i ich pochodnych. Są one podłączane do ' \
       'komputerów przez port równoległy, uniwersalną magistralę szeregową lub sterownik SCSI.'

# print(text)

def zad2(*args):
    zbior = {}
    for i in args:
        zbior[i] = 0
    for wyraz in text.lower().split():
        for wyraz_szukany in args:
            if wyraz == wyraz_szukany:
                zbior[wyraz_szukany] += 1
    
    print(zbior)

#zad2('komputera','skanery')





############ Zadanie 3 #################
## Utwórz funkcję o nazwie "SredniaLiczb.py", która wczyta N dowolnych liczb 
## i obliczy średnią z w/w liczb, podane przez użytkownika liczby przypisz do listy

from SredniaLiczb import srednia

#srednia(1,2,3,4,5)



############ Zadanie ##################
## Utwórz funkcję o nazwie "ZdanieRozdziel.py", która wczyta od użytkownika pewien dowolny tekst,'
## a następnie podzieli go na zdania (zakładamy, że jednoznacznie kropka rozdziela zdania)'
## funkcja w zależności od ustawionych kolejnych parametrów wejściowych funkcji 
## (ustaw domyślnie argumenty wejściowe: True), 
## może ale nie musi wyświetlić następujące informacje: 
## ile w każdym zdaniu jest fragmentów rozdzielonych przez określony znak np. ',', ';' 
#(domyślnie argument wejściowy to przecinek: ',')
## ile w każdym zdaniu jest wyrazów (zakładamy, że spacja oddziela wyrazy w zdaniu)
## użyj odpowiednich metod dla zmiennych typu string np. split do rozdzielenia elementów: x = ‘blue,red,green’,   x.split(“,”)

########### Zadanie 6  ########################
## Zdefiniuj funkcję "CiagGeometryczny.py", która dla podanych trzech parametrów:
## n=numer elementu ciągu, a1=wartość pierwszego elementu ciągu (domyślnie: 1),
## q=wartość iloczynu ciągu geometrycznego (domyślnie: 2) 
## zwróci w zależności od ustawianych parametrów funkcji
## a) wartość n-tego elementu ciągu geometrycznego
## b) sumę elementów ciągu geometrycznego

def ciag_g(n,a1,q):
    ciag_sum = 0
    n_element_value = a1*q**(n-1)
    print(n_element_value)
    if q == 1:
        ciag_sum = a1*n
    else:
        ciag_sum = a1*((1-q**(n))/(1-q))
    print(ciag_sum)

#ciag_g(4,1,2)

############Przykład
### Mamy 2 sklepy  z różnymi produktami
# def test_kwargs(id_sklep = 0, liczba_pracownikow = 5, **kwargs):
#     print(id_sklep)
#     print(liczba_pracownikow)
#     print(kwargs)

# test_kwargs(1, mleko=100, woda=500)
# print('#################')
# test_kwargs(2, liczba_pracownikow = 15, drabina=500, cement=200)

# ########################## Zadanie 7
## Zaprojektuj program służący do obsługi prostej bazy danych dla sklepu z
## dowolnej branży o różnej liczbie pracowników. Program zapisuje do kolejnych list
## liczby produktów dostarczonych w danym dniu (nazwa listy odpowiada nazwie towaru)
## liczba towarów powinna być zapamiętana 

# Przetestuj swój program dla różnych przypadków dostawy towaru
# Pamiętaj że asortyment sprzedawanego towaru ulega zmianie
# Użyj kwargs

def dodaj_dostawe(baza_danych, nazwa_produktu, liczba_produktow, **kwargs):
    for produkt in baza_danych:
        if produkt[0] == nazwa_produktu:
            produkt[1].append(liczba_produktow)
    baza_danych.append([nazwa_produktu, [liczba_produktow]])

def wyswietl_produkty(baza_danych):
    for produkt in baza_danych:
        print(f"{produkt[0]}: {produkt[1]}")

def otworz_sklep():
    baza_danych = []
    
    while True:
            print("1. Dodaj dostawę")
            print("2. Wyświetl bazę danych")
            print("3. Zakończ program")
            
            wybor = input("Wybierz działanie: ")

            if wybor == '1':
                nazwa_produktu = input("Podaj nazwę produktu: ")
                liczba_produktow = int(input("Podaj liczbę produktów: "))
                dodaj_dostawe(baza_danych, nazwa_produktu, liczba_produktow)
                print("Dostawa dodana.")
            elif wybor == '2':
                print("\nBaza danych sklepu:")
                wyswietl_produkty(baza_danych)
            elif wybor == '3':
                print("Zakończono program.")
                break
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")

#otworz_sklep()

# ########################## Zadanie 8
## W module pole_prostokata.py 
## Zdefiniuj funkcję która obliczy pole powierzchni prostokąta
## W module pole_trojkata.py 
## Zdefiniuj funkcję która obliczy pole powierzchni trójkąta
# W module pola.py
## Korzystając z modułów pole_prostokata i pole_trojkata
## napisz funkcję która ma możliwość obliczenia pola prostokąta, trójkąta i kwadratu
## Użyj zmiennych globals, utwórz moduł globals.py w którym będą przechowywane 
## domyślne wartości dla boków prostokąta, trójkąta, kwadratu (równe 1)

from pola import oblicz_pole
from poleprostokata import pole_prostokata
from poletrojkata import pole_trojkata

def zad8():
    print(oblicz_pole('prostokat'))
    print(oblicz_pole('trojkat'))
    print(oblicz_pole('kwadrat'))

#zad8()


# ########################## Zadanie 9
## Zdefiniuj funkcję wyższego rzędu która ma możliwość obliczenia
## pole powierzchni prostokąta i pola powierzchni trójkąta
## Nie modyfikując zawartości wyżej wymienionej funkcji, użyj dekoratora i dodaj możliwość 
## obliczenia pola kwadratu
# Funkcja wyższego rzędu

def oblicz_pole_zad9(figura):
    if figura == "prostokat":
        return pole_prostokata
    elif figura == "trojkat":
        return pole_trojkata
    else:
        print("Zły rodzaj figury")


# Dekorator
def dodaj_kwadrat(funkcja):
    def wewnetrzna(a, b=None):
        if b is None:
            print("pole kwadratu")
            return funkcja(a)
        else:
            return funkcja(a, b)

    return wewnetrzna


# Przykłady użycia

# Użycie funkcji wyższego rzędu bez dekoratora
pole_prostokata = oblicz_pole_zad9("prostokat")
#print("Pole prostokąta:", pole_prostokata(4, 5))

pole_trojkata = oblicz_pole_zad9("trojkat")
#print("Pole trójkąta:", pole_trojkata(3, 6))

# Użycie funkcji wyższego rzędu z dekoratorem
@dodaj_kwadrat
def pole_kwadratu(a):
    return a * a

#print("Pole kwadratu:", pole_kwadratu(4))


# ########################## Zadanie 10
## Utwórz funkcję która umożliwia logowanie na serwer
## Ma dwa argumenty wejściowe:
## user i password (domyślne wartości odpowiednio: 'edek2003', 'Wsx123')
## a) nie modyfikując zawartości w/w funkcji, użyj dekoratora i dodaj dodatkowe
## pola tj. host, port
## b) nie modyfikując zawartości w/w funkcji, użyj dekoratora i  daj możliwość 
## wprowadzania dodatkowych innch pól użytkownikowi (wprowadzane jako słownik
##  np. {'data_base': 'https://pl.wikipedia.org'})

# ########################## Zadanie 11
## Zdefiniuj funkcję ciag_gometryczny, która dla podanych trzech parametrów:
## n=numer elementu ciągu, a1=wartość pierwszego elementu ciągu (domyślnie: 1),
## q=wartość iloczynu ciągu geometrycznego (domyślnie: 2) 
## zwróci w zależności od ustawianych parametrów funkcji
## a) wartość n-tego elementu ciągu geometrycznego

## Następnie korzystając z dekoratora udoskonal swoją funkcję,
## dodaj możliwość obliczenia sumy elementów ciągu geometrycznego





