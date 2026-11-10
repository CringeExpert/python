# Szymon Jaworski, zadanie nr 5 z listy 4

n = int(input('Podaj n:'))                     #pobranie N

i1,i2 = 0,1                                    #dwa pierwsze wyrazy: 0 i 1

while i1 <= n:                                 #dopóki wyraz <= N
    print(i1, end=' ')                         #wypisanie wyrazu
    i1, i2 = i2, i1+i2                         #aktualizacja: wyraz 1 zamienia się na wyraz 2, i w tym samym czasie (na starych wartościach, stąd brak potrzeby trzeciej zmiennej) druga wartość to suma 2 wyrazów
    