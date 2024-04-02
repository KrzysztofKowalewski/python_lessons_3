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




from SredniaLiczb import srednia

srednia(1,2,3,4,5)


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

from pola import oblicz_pole
from poleprostokata import pole_prostokata
from poletrojkata import pole_trojkata

def zad8():
    print(oblicz_pole('prostokat'))
    print(oblicz_pole('trojkat'))
    print(oblicz_pole('kwadrat'))

#zad8()


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


pole_prostokata = oblicz_pole_zad9("prostokat")
#print("Pole prostokąta:", pole_prostokata(4, 5))

pole_trojkata = oblicz_pole_zad9("trojkat")
#print("Pole trójkąta:", pole_trojkata(3, 6))

# Użycie funkcji wyższego rzędu z dekoratorem
@dodaj_kwadrat
def pole_kwadratu(a):
    return a * a

#print("Pole kwadratu:", pole_kwadratu(4))






