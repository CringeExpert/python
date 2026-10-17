import random
import string

l = int(input('Podaj liczbę n: '))
s = {}

alphabet = string.ascii_letters

for i in range(1,l+1):
    s[i] = "".join([random.choice(alphabet) for x in range(i)])

[print(x) for x in s.items()]