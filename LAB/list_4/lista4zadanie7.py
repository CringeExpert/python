# Szymon Jaworski, zadanie nr 7 z listy 4

n,m = (int(x) for x in input("Podaj n oraz m (po spacji)").split())  #pobranie n i m

tab = [[i*j for j in range(1,m+1)] for i in range(1, n+1)]  #tablica: i*j dla i=1..n, j=1..m

for i in tab:                                  #wypisanie każdego wiersza
    print(i)

#alternatywnie
tab = []                                       #pusta tablica
for i in range(0, n):                          #pętla po wierszach
    tab.append([])                             #dodanie pustego wiersza
    for j in range(0,m):                       #pętla po kolumnach
        tab[i].append((i+1)*(j+1))             #element (i+1)*(j+1)

print()
for i in tab:                                  #wypisanie każdego wiersza
    print(i)