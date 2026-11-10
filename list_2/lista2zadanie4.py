# Szymon Jaworski, zadanie nr 4 z listy 2

text = input("Podaj napis: ")                       #pobranie napisu od użytkownika
print(text[0] + text[1:].replace(text[0], '$'))     #zamiana wszystkich poza pierwszym na $