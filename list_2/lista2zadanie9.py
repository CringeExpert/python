# Szymon Jaworski, zadanie nr 9 z listy 2

from itertools import chain                    #import funkcji chain

listOg = [[1,2],[3,4]]                         #lista zagnieżdżona

print(list(chain(*listOg)))                    #spłaszczenie przez rozpakowanie (*) - działa

#alternatywnie
print(list(chain.from_iterable(listOg)))