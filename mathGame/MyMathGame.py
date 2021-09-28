pytanie1 = "9 * 9=? "
pytanie2 = "15 + 10=? "
pytanie3 = "50 - 17=? "
pytanie4 = "10 * 9=? "
prawidlowa1 = 81
prawidlowa2 = 25
prawidlowa3 = 33
prawidlowa4 = 90
i = 0
punkty = 0
nrpytania = 1
while i < 4:
    if nrpytania == 1:
        pytanie = pytanie1
        prawidlowa = prawidlowa1
    elif nrpytania == 2:
        pytanie = pytanie2
        prawidlowa = prawidlowa2
    elif nrpytania == 3:
        pytanie = pytanie3
        prawidlowa = prawidlowa3
    else:
        pytanie = pytanie4
        prawidlowa = prawidlowa4
    odpowiedz = input(pytanie)
    if odpowiedz.isdigit():
        if float(odpowiedz) == prawidlowa:
            print("poprawna odpowiedź!")
            punkty += 1
            i += 1
            nrpytania += 1
        else:
            print("błąd! Poprawna odpowiedź to " + str(prawidlowa))
            i += 1
            nrpytania += 1

    elif odpowiedz == "sciagam":
        print("Sciagałeś! Egzamin zostaje nieważniony!")
        punkty = 0
        break
    else:
        print("błąd podana odpowiedź nie jest liczbą, podaj liczbę!")
print("uzyskałeś " + str(punkty) + " punktów")
if float(punkty) > 2:
    print("gratulacje zdałeś egzamin!!!!!!")
else:
    print("niestety nie udało ci się zdać. Wróć w sierpniu!")