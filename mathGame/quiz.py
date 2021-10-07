from random import randint
liczba = randint(1, 10)
odp = -1
i = 0
print ("podaj liczbe od 1 do 10")
while float(odp) != liczba:
    odp = input("podaj liczbę ")
    if odp.isdigit():
        i += 1
        if float(odp) > liczba:
            print("nie zgadłeś! Podana liczba jest za duża!")
        elif float(odp) < liczba:
            print("nie zgadłeś! Podana liczba jest za mała")
        else:
            print("udało ci się! ")
            print("zgadłeś liczbę za " + str(i) + " razem")
    else:
        print("podana odpowiedź nie jest liczbą!")
        odp = -1