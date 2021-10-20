import random
lista = [["9 * 9=? ", 81], ["15 + 10=? ", 25], ["50 - 17=? ", 33], ["10 * 9= ?", 90], ["8 + 6=? ", 14], ["5 * 5=? ", 25], ["4 * 4=? ", 16], ["4 * 9= ? ", 36], ["6 * 6=? ", 36],
["10:2=? ", 5]]
indexy = list(range(0,len(lista)))
quizy = list(range(1,5))
punkty = 0

def intCheck(x):
    while True:
            odpowiedz = input(x)
            if odpowiedz.isdigit():
                return int(odpowiedz)
            else:
                print("błąd podana odpowiedź nie jest liczbą, podaj liczbę!")

def intro():
    checked = 0
    while True:
        odpowiedz = intCheck("1. matematyka 2. angielski ")
        for x in quizy:
            if odpowiedz == x:
                checked = 1
                break
        if checked == 1:
            break
        else:
            print ("Quiz nie istnieje, bądź już go rozwiązałeś! wybierz inny quiz z listy!")
    return odpowiedz


def mathQuiz():
    punktyM = 0
    for i in range(4):
        nrpytania = random.choice(indexy)
        indexy.pop(indexy.index(nrpytania))
        x = 0
        if intCheck(lista[nrpytania][0]) == lista[nrpytania][1]:
            print("poprawna odpowiedź!")
            punktyM += 1
        else:
            print("błąd! Poprawna odpowiedź to " + str(lista[nrpytania][1]))
    print("uzyskałeś " + str(punktyM) + " punktów")
    if float(punktyM) > 2:
        print("gratulacje zdałeś egzamin!!!!!!")
    else:
        print("niestety nie udało ci się zdać. Wróć w sierpniu!")


def engQuiz():
    print("jestem testem z angielskiego")
print("Witaj Użytkowniku!")
print("wybierz quiz z listy wpisując jego numer")

        

for z in range(2):
    while True:
        odpowiedz = intro()
        if odpowiedz == 1:
            quizy.pop(odpowiedz - 1)
            mathQuiz()
            break
        elif odpowiedz == 2:
            engQuiz()
            break
        else:
            print("podaj poprawny numer quizu")
print ("koniec quizów")