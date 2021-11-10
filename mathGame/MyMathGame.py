import random
 
myList = {}
 
mathList = [
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
engList = [
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
plList = [
                ["czym jest synonim? a. wyrazem podobnym b. wyrazem o przeciwnym znaczeniu c. dlugim wyrazem ", "a"],
                ["w którym roku odbył się chrzest Polski? a. 1042 b. 966 c.894 d. 1410 ", "b"],
                ["w którym roku odbyła się bitwa pod Grunwaldem? a. 1240 b. 1410 c.1330 d. 1505 ", "b"],
                ["'pies' to: a. rzeczownik b. czasownik c. przymiotnik ", "a"],
                ["kiedy obchodzimy świeto niepodległości? a. 11.11 b 12. 11 c 07.13 d 09.15 ", "a"], 
                ["jakie zwierzęta są symbolem białowieskiego parku narodowego? a. żubr b. bizon c. dzięciął d. krokodyl ", "a"],
            ]
healthList = [
                ["ktore owoce maja duzo witaminy c? a. jabłko b. kiwi c.cytryny d.arbuzy ", "bc"],
                ["które produkty maja wysoki indeks glikemiczny? a. ryż b. jabłko c.frytki d. płatki owsiane ", "acd"],
                ["na czym można smażyć? a.olej b.masło c.ocet d.bulion ", "ab"],
                ["ktore ryby sa slodkowodne? a. karp b. ukleja c. węgorz d. lin ", "abd"],
                ["które tłuszcze mają wysoki punkt dymienia? a. masło b. masło klarowane c. olej lniany d. łój  ", "bd"], 
                ["które z podanych to akcesoria kuchenne? a. salamandra b. wilk c. tygrys d. kot ", "ab"],
                ["które produkty mają dobry cholesterol? a. frytki b. oliwa z oliwek c. łosoś d. wino ", "bcd"],
            ]
 
myList["matematyka"] = mathList
myList["angielski"] = engList
myList["polski"] = plList
myList["zywienie"] = healthList
points = 0

def verifyNumber(x):
    while True:
        answer = input(x)
 
        if answer.isdigit():
            return int(answer)
        else:
            print("błąd podana odpowiedź nie jest liczbą, podaj liczbę!")

def quiz(x):
    y = 0
    indexList = list(range(0,len(myList[x])))

    for i in range(4):
        questionNumber = random.choice(indexList)
        indexList.pop(indexList.index(questionNumber))

        if x == "matematyka":
            if verifyNumber(myList["matematyka"][questionNumber][0]) == myList["matematyka"][questionNumber][1]:
                print("poprawna odpowiedź!")
                y += 1
            else:
                print("błąd! Poprawna odpowiedź to " + str(myList["matematyka"][questionNumber][1]))
        else:
            answer = input(myList[x][questionNumber][0])
            fixed_answer = "".join(filter(str.isalnum, answer))

            if fixed_answer.lower() == myList[x][questionNumber][1]:
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
        print (list(myList))
        answer = input("podaj nazwę quizu który chcesz rozwiązać i upewnij się, że jest poprawna! ")

        for i in myList:
            itemToPop = 0

            if answer.lower() == i:
                points = points + quiz(i)
                itemToPop = i
                restart = True

            if itemToPop != 0:
                myList.pop(itemToPop)
                break

        if restart == True:
            break
    
print ("koniec quizów")
print ("uzyskałeś " +str(points) + "/16 punktow")
 
if points >=10:
    print ("zdałeś egzamin!")
else:
    print ("niestety nie udało ci się zdać, wróć w sierpniu")
 
input("press enter to exit")
