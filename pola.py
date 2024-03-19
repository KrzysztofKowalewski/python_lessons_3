from poleprostokata import pole_prostokata
from poletrojkata import pole_trojkata
from globals import a,b,h

def oblicz_pole(figura):
    if figura == "prostokat":
        return pole_prostokata(a,b)
    elif figura == "trojkat":
        return pole_trojkata(a,h)
    elif figura == "kwadrat":
        return pole_prostokata(a,a)
    else:
        print("Zły rodzaj figury")

