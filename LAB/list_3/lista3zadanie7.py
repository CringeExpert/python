# Szymon Jaworski, zadanie nr 7 z listy 3

import random
import string

l = int(input('Podaj liczbę n: '))             #pobranie liczby n
s = {}                                         #pusty słownik

chars = string.ascii_letters + string.digits   #zbiór dostępnych znaków

for i in range(1,l+1):                         #klucze od 1 do n
    s[i] = "".join(random.choices(chars,k=i))  #wartość: i losowych znaków

for i in s.items():
    print(i)                  #wypisanie par klucz-wartość

