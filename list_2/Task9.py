from itertools import chain

listOg = [[1,2],[3,4]]

print(list(chain(*listOg)))

#alternatywnie
print(list(chain.from_iterable(listOg)))
