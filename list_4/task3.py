a,b,c = [int(x) for x in input("Podaj a, b, c (po spacjach): ").split(" ")]

if a == 0:
    print('Nie jest to równanie kwadratowe')
    exit
else:
    D = b**2 - 4 * a * c
    x1 = (-b+D**0.5)/(2*a)
    x2 = (-b-D**0.5)/(2*a)

    print(f'{x1} ')