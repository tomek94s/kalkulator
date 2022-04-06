a = int(input("Podaj składnik 1: "))
b = int(input("Podaj składnik 2. "))
dzialanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
def oblicz(type):
    if type == 1:
        wynik = a + b
    if type == 2:
        wynik = a - b
    if type == 3:
        wynik = a * b
    if type == 4:
        wynik = a / b
    if type > 4:
        wynik = ("nie ma takiego dzialania")
    if type < 1:
        wynik = ("nie ma takiego dzialania")
    print(wynik)

oblicz(dzialanie)


  

