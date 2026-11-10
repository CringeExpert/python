# Szymon Jaworski, zadanie nr 3 z listy 4

while(True):                                   #pętla do poprawnego pobrania danych (do while)
    try:
        a,b,c = [int(x) for x in input("Podaj a, b, c (po spacjach): ").split(" ")]  #pobranie trzech intów
        break                                  #przerwanie pętli po sukcesie
    except:
        print('Spróbuj ponownie!')             #komunikat o błędzie
        continue                               #kolejna iteracja

if a == 0:                                     #sprawdzenie czy a jest zerem (nie będzie to równanie kwadratowe)
    print('Nie jest to równanie kwadratowe')
    exit()                                       #wyjscie z programu
else:
    D = b**2 - 4 * a * c                       #obliczenie delty
    if D > 0:                                 #dwa lub jedno rozwiązanie
        x1 = (-b+D**0.5)/(2*a)                 #pierwszy pierwiastek
        x2 = (-b-D**0.5)/(2*a)                 #drugi pierwiastek
        print(f'x1 = {x1}, x2 = {x2}')
    elif D == 0:
        print(f'x = {(-b)/2*a}')                #jeden pierwiastek jeśli delta to 0
    else:
        print(f'Brak rozwiązania dla takich danych.')  #brak pierwiastków rzeczywistych