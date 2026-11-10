# Szymon Jaworski, zadanie nr 4 z listy 4

i = int(input('Podaj i: '))                    #pobranie liczby i od użytkownika

for j in range(1,11):                          #j = 1..10
    print(f'{i*j:^4}')                         #wypisanie iloczynu wyśrodkowanego w polu 4 znaków