# Szymon Jaworski, zadanie nr 8 z listy 1

a = int(input('a: '))                          #pobranie liczby a
b = int(input('b: '))                          #pobranie liczby b

if b >= a:                                     #sprawdzenie czy b >= a
    a,b = b,a                                  #zamiana wartości, aby a > b

Z = a % b                                      #reszta z dzielenia a przez b
print(Z)                                       #wypisanie reszty

Z *= Z + 3                                     #Z = Z * (Z + 3) - mnożenie przez Z+3 bez nawiasów
print(Z)                                       #wypisanie wyniku