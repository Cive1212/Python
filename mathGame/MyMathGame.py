import random
lista = [["9 * 9=? ", 81], ["15 + 10=? ", 25], ["50 - 17=? ", 33], ["10 * 9= ?", 90], ["8 + 6=? ", 14], ["5 * 5=? ", 25], ["4 * 4=? ", 16], ["4 * 9= ? ", 36], ["6 * 6=? ", 36],
["10:2=? ", 5]]
indexy = list(range(0,len(lista)))
punkty = 0
for i in range(4):
    nrpytania = random.choice(indexy)
    indexy.pop(indexy.index(nrpytania))
    x = 0
    while x < 1:
        odpowiedz = input(lista[nrpytania][0])
        if odpowiedz.isdigit():
            x += 1
        else:
            print("błąd podana odpowiedź nie jest liczbą, podaj liczbę!")
    if int(odpowiedz) == lista[nrpytania][1]:
        print("poprawna odpowiedź!")
        punkty += 1
    else:
        print("błąd! Poprawna odpowiedź to " + str(lista[nrpytania][1]))
print("uzyskałeś " + str(punkty) + " punktów")
if float(punkty) > 2:
    print("gratulacje zdałeś egzamin!!!!!!")
else:
    print("niestety nie udało ci się zdać. Wróć w sierpniu!")