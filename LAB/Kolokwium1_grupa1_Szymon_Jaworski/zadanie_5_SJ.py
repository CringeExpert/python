#Szymon Jaworski, 367072, Grupa 1
#Zadanie 5
import string

napis = input("Podaj napis: ")

napis = napis.lower()

napis = "".join([c for c in napis if c not in string.punctuation])
wynik = napis.split()
