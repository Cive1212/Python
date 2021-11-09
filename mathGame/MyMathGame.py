import random
 
myList = {}
 
mathList =  [
                ["9 * 9=? ", 81],
                ["15 + 10=? ", 25],
                ["50 - 17=? ", 33],
                ["10 * 9= ?", 90],
                ["8 + 6=? ", 14],
                ["5 * 5=? ", 25],
                ["4 * 4=? ", 16],
                ["4 * 9= ? ", 36],
                ["6 * 6=? ", 36],
                ["10:2=? ", 5]
            ]
engList =   [
                ["jak jest 'pies' po angielsku? ", "dog"],
                ["jak jest 'żaba' po angielsku ", "frog"],
                ["jak są 'drzwi' po angielsku ", "door"],
                ["jak jest 'młotek' po angielsku ", "hammer"],
                ["jak jest 'drzewo' po angielsku ", "tree"], 
                ["jak jest 'ptak' po angielsku ", "bird"],
                ["jak jest 'kubek' po angielsku ", "cup"],
                ["jak jest 'widelec' po angielsku ", "fork"],
                ["jak jest 'kość' po angielsku ", "bone" ]
            ]
plList =     [
                ["jak jest 'pies' po angielsku? ", "dog"],
                ["jak jest 'żaba' po angielsku ", "frog"],
                ["jak są 'drzwi' po angielsku ", "door"],
                ["jak jest 'młotek' po angielsku ", "hammer"],
                ["jak jest 'drzewo' po angielsku ", "tree"], 
                ["jak jest 'ptak' po angielsku ", "bird"],
                ["jak jest 'kubek' po angielsku ", "cup"],
                ["jak jest 'widelec' po angielsku ", "fork"],
                ["jak jest 'kość' po angielsku ", "bone" ]
            ]
healthList =   [
                ["jak jest 'pies' po angielsku? ", "dog"],
                ["jak jest 'żaba' po angielsku ", "frog"],
                ["jak są 'drzwi' po angielsku ", "door"],
                ["jak jest 'młotek' po angielsku ", "hammer"],
                ["jak jest 'drzewo' po angielsku ", "tree"], 
                ["jak jest 'ptak' po angielsku ", "bird"],
                ["jak jest 'kubek' po angielsku ", "cup"],
                ["jak jest 'widelec' po angielsku ", "fork"],
                ["jak jest 'kość' po angielsku ", "bone" ]
            ]
 
myList["math"] = mathList
myList["eng"] = engList
myList["polski"] = plList
myList["zywienie"] = healthList
#indexes = [list(range(0,len(myList["math"]))), list(range(0,len(myList["eng"])))]
points = 0

def generateList(x):
    indexes = []
    indexes = list(range(0,len(myList[x])))
    return indexes

def verifyNumber(x):
    while True:
        answer = input(x)
 
        if answer.isdigit():
            return int(answer)
        else:
            print("błąd podana odpowiedź nie jest liczbą, podaj liczbę!")

def quiz(x):
    y = 0

    for i in range(4):
        indexList = generateList(x)
        questionNumber = random.choice(indexList)
        indexList.pop(indexList.index(questionNumber))

        if x == "math":

            if verifyNumber(myList["math"][questionNumber][0]) == myList["math"][questionNumber][1]:
                print("poprawna odpowiedź!")
                y += 1
            else:
                print("błąd! Poprawna odpowiedź to " + str(myList["math"][questionNumber][1]))

        else:
            answer = input(myList[x][questionNumber][0])

            if answer.lower() == myList[x][questionNumber][1]:
                print("poprawna odpowiedź!")
                y += 1
            else:
                print("błąd! Poprawna odpowiedź to " + str(myList[x][questionNumber][1]))

    print("uzyskałeś " + str(y) + " punktów")
    return y 
 
print("Witaj Użytkowniku!")

for i in range(4):

    while True:
        restart = False
        answer = input("podaj nazwę quizu który chcesz rozwiązać ")
        for i in myList:
            itemToPop = 0
            if answer.lower() == i:
                print (list(myList).index(i))
                points = points + quiz(i)
                itemToPop = i
                restart = True
            else:
                print ("podaj poprawną nazwę quizu!")

        if itemToPop != 0:
            myList.pop(itemToPop)

        if restart == True:
            break
    
print ("koniec quizów")
print ("uzyskałeś " +str(points) + "/8 punktow")
 
if points >=5:
    print ("zdałeś egzamin!")
else:
    print ("niestety nie udało ci się zdać, wróć w sierpniu")
 
input("press enter to exit")
