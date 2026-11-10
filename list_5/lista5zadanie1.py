# Szymon Jaworski, zadanie nr 1 z listy 5

import math

lst = [1,2,3,4,5]                             #lsta wejściowa (uważaj na nazwę lst)

print(sum(lst),math.prod(lst))               #suma i iloczyn z użyciem math.prod

#alternatywnie
iloczyn = 1                                    #zerowy iloczyn
for i in lst:                                 #pętla po elementach
    iloczyn *= i                               #mnożenie kolejnych elementów

print(sum(lst),iloczyn)                       #suma i iloczyn bez math.prod