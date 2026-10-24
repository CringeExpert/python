import random
import string

l = int(input('Podaj liczbę n: '))
s = {}

chars = string.ascii_letters + string.digits

for i in range(1,l+1):
    s[i] = "".join([random.choice(chars) for x in range(i)])

[print(x) for x in s.items()]