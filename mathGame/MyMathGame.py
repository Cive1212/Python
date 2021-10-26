import random

myList = ["quizy",
["matematyka", [["9 * 9=? ", 81], ["15 + 10=? ", 25], ["50 - 17=? ", 33], ["10 * 9= ?", 90], ["8 + 6=? ", 14],
["5 * 5=? ", 25], ["4 * 4=? ", 16], ["4 * 9= ? ", 36], ["6 * 6=? ", 36], ["10:2=? ", 5]]],
["angielski", [["jak jest 'pies' po angielsku? ", "dog"], ["jak jest 'żaba' po angielsku ", "frog"],
["jak są 'drzwi' po angielsku ", "door"], ["jak jest 'młotek' po angielsku ", "hammer"],
["jak jest 'drzewo' po angielsku ", "tree"], ["jak jest 'ptak' po angielsku ", "bird"], ["jak jest 'kubek' po angielsku ", "cup"],
["jak jest 'widelec' po angielsku ", "fork"], ["jak jest 'kość' po angielsku ", "bone" ]
  ]]
]
indexes = [list(range(0,len(myList[1][1]))), list(range(0,len(myList[2][1])))]
quizes = list(range(1,5))
points = 0
pointsM = -1
pointsA = -1
def verifyNumber(x):
    while True:
        answer = input(x)
        if answer.isdigit():
            return int(answer)
        else:
            print("błąd podana odpowiedź nie jest liczbą, podaj liczbę!")


def mathQuiz():
    pointsM = 0
    for i in range(4):
        questionNumber = random.choice(indexes[0])
        indexes[0].pop(indexes[0].index(questionNumber))
        if verifyNumber(myList[1][1][questionNumber][0]) == myList[1][1][questionNumber][1]:
            print("poprawna odpowiedź!")
            pointsM += 1
        else:
            print("błąd! Poprawna odpowiedź to " + str(myList[1][1][questionNumber][1]))
    print("uzyskałeś " + str(pointsM) + " punktów")
    if float(pointsM) > 2:
        print("gratulacje zdałeś egzamin!!!!!!")
    else:
        print("niestety nie udało ci się zdać. Wróć w sierpniu!")
    print (pointsM)
    return pointsM

def engQuiz():
    pointsA = 0
    for i in range(4):
        questionNumber = random.choice(indexes[1])
        indexes[1].pop(indexes[1].index(questionNumber))
        answer = input(myList[2][1][questionNumber][0])
        if answer.lower() == myList[2][1][questionNumber][1]:
            print("poprawna odpowiedź!")
            pointsA += 1
        else:
            print("błąd! Poprawna odpowiedź to " + str(myList[2][1][questionNumber][1]))
    print("uzyskałeś " + str(pointsA) + " punktów")
    if float(pointsA) > 2:
        print("gratulacje zdałeś egzamin!!!!!!")
    else:
        print("niestety nie udało ci się zdać. Wróć w sierpniu!")
    return pointsA



def plQuiz():
    print("jestem testem z polskiego")

def healthQuiz():
    print("jestem testem z żywienia")
print("Witaj Użytkowniku!")
print("wybierz quiz z listy wpisując jego numer")

for i in range(4):
    while True:
        answer = verifyNumber("1. matematyka 2. angielski 3. polski 4. żywienie ")
        if answer == 1:
            if pointsM >= 0:
                print ("ten quiz został już wykonany")
            else:
                pointsM = mathQuiz()
                myList[1].pop(answer - 1)
                break
        elif answer == 2:
            if pointsA >= 0:
                print ("ten quiz został już wykonany")
            else:
                pointsA = engQuiz()
                myList[2].pop(answer - 1)
                break
        elif answer == 3:
            plQuiz()
            break
        elif answer == 4:
            healthQuiz()
            break
        else:
            print("podaj poprawny numer quizu")
print ("koniec quizów")