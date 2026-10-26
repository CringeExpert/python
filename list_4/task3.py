while(True):
    try:
        a,b,c = [int(x) for x in input("Podaj a, b, c (po spacjach): ").split(" ")]
        break
    except:
        print('Spróbuj ponownie!')
        continue

if not(a):
    print('Nie jest to równanie kwadratowe')
    exit
else:
    D = b**2 - 4 * a * c
    if D >= 0:
        x1 = (-b+D**0.5)/(2*a)
        x2 = (-b-D**0.5)/(2*a)
        print(f'x1 = {x1}, x2 = {x2}')
    else:
        print(f'Brak rozwiązania dla takich danych.')