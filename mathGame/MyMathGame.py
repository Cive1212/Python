a = input("9 * 9=? ")
prawidlowa = 81
if a.isdigit():
    if float(a) == prawidlowa:
        print("poprawna odpowiedź! Gratulacje!")
    else:
        print("błąd! Poprawna odpowiedź to " + str(prawidlowa))
else:
    print("błąd podana odpowiedź nie jest liczbą!")