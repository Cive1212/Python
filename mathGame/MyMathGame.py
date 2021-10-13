pytania = ["9 * 9=? ", "15 + 10=? ", "50 - 17=? ", "10 * 9= ?", "8 + 6=? ", "5 * 5=? ", "4 * 4=? ", "4 * 9= ?", "6 * 6=? ", "10:2=? "]
odpowiedzi = [81, 25, 33, 90, 14, 25, 16, 36, 36, 5]
i = 0
punkty = 0
nrpytania = 0
uzytepytania = []
from random import randrange
while i < 4:
    nrpytania = randrange(0, 10)
  #  if nrpytania == nrpoprzpytania:
   #     continue
    uzytepytania.append(nrpytania)
    odpowiedz = input(pytania[nrpytania])
    if odpowiedz.isdigit():
        if float(odpowiedz) == odpowiedzi[nrpytania]:
            print("poprawna odpowiedź!")
            punkty += 1
            i += 1
            nrpytania += 1
        else:
            print("błąd! Poprawna odpowiedź to " + str(odpowiedzi[nrpytania]))
            i += 1
            nrpytania += 1
    else:
        print("błąd podana odpowiedź nie jest liczbą, podaj liczbę!")
print("uzyskałeś " + str(punkty) + " punktów")
if float(punkty) > 2:
    print("gratulacje zdałeś egzamin!!!!!!")
else:
    print("niestety nie udało ci się zdać. Wróć w sierpniu!")
print(uzytepytania)