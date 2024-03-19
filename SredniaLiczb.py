def srednia(*args):
    numbers = []
    suma_liczb = 0
    ilosc_liczb = len(args)
    for number in args:
        numbers.append(number)
        suma_liczb += number
    srednia_liczb = suma_liczb/ilosc_liczb
    print(srednia_liczb)

#srednia(1,2,3,4,5)
    

