x = input("Podaj liczby oddzielone przecinkami (,): ")

l = list(map(int, x.split(',')))
print(*l,sep=' + ', end='' )
print(f' = {sum(l)}')
