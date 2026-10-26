n = int(input('Podaj n:'))

i = 0
i2 = 1
tmp = 1

while i <= n:
    print(i2,end=' ')
    i = i + tmp
    tmp = i2
    i2 = i
    
    