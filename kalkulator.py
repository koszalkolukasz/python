zmienna1 = float(input("podaj pierwszą liczbę: "))
zmienna2 = float(input("Podaj drugą liczbę: "))

operacaje = input("Co chcesz zrobić:\n"
                  "1.dodać liczby\n"
                  "2.odjąć liczby\n"
                  "3.pomnożyć liczby\n"
                  "4.podzielić liczby\n")

if operacaje == "1":
    print("Wynik: " , zmienna1 + zmienna2)
elif operacaje == "2":
    print("Wynik: ", zmienna1 - zmienna2)
elif operacaje == "3":
    print("Wynik: ", zmienna1 * zmienna2)
elif operacaje == "4":
    if (zmienna2 == 0):
        print("pamiętaj cholero nie dziel przez zero")
    print("Wynik: ", zmienna1 / zmienna2)


