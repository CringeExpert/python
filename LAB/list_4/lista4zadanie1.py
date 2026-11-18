# Szymon Jaworski, zadanie nr 1 z listy 4

import string

vowels = ('a','A','e','E','i','I','o','O','u','U','y','Y')  #krotka samogłosek

letters = string.ascii_letters                 #zmienna nieużywana w kodzie

l = input("Podaj literę: ")                    #pobranie litery od użytkownika

if l in vowels:                                #sprawdzenie czy samogłoska
    print(f"{l} jest samogłoską")              #komunikat: samogłoska
else:
    print(f"{l} jest spółgoską")              #komunikat: spółgłoska