# Szymon Jaworski, zadanie nr 6 z listy 4

n = int(input('Podaj n:'))                     #pobranie liczby wierszy

for i in range(1,n+1):                         #pętla po wierszach 1..n
    print(str(i)*i)                            #wypisanie cyfry i powtórzonej i razy