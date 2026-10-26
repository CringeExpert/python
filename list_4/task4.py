n = int(input('Podaj i: '))

for i in range(1, n+1):
    for j in range(1,11):
        print(f'{i*j:4}',end='')

    print("\n")
    