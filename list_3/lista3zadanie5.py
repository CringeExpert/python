# Szymon Jaworski, zadanie nr 5 z listy 3

x = input("Podaj liczbę: ")                    #pobranie ciągu znaków od użytkownika

if (x.isdigit()):                              #sprawdzenie, czy wszystkie znaki są cyframi (działa jak liczby naturalne -1 ma w sobie minus)
    print("Podano liczbę naturalną")           #komunikat: podano liczbę naturalną
else:
    print("Nie podano liczby naturalnej")      #komunikat: nie podano liczby naturalnej