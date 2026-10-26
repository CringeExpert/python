n,m = list(map(int,input('Podaj i (po spacjach): ').split(' ')))
print()

tab = []

for i in range(0, n):
    tab.append([])
    for j in range(0,m):
        
        tab[i].append((i+1)*(j+1))

for i in tab:
    print(i)