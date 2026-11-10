# Szymon Jaworski, zadanie nr 2 z listy 3

t = (*range(5),"pięć","sześć","siedem","osiem","dziewięć")  #krotka: 0,1,2,3,4 + 5 słów
print(t)                                       #wypisanie krotki

print(t[0:3])                                  #trzy pierwsze elementy
print(t[-2:])                                  #dwa ostatnie elementy
print(t[1::2])                                 #co drugi element, zaczynając od drugiego
print(len(t),len(t[-2]))                       #długość krotki i długość przedostatniego elementu

print("\n", t[:5] + (5, 6) + t[-3:])           #krotka niezagnieżdzona wszystkich podanych elementów
print(t[:5], (5, 6), t[-3:])                   #krotki z podanymi elementami
