list = [(2, 8), (5, 5), (9, 3), (1, 0), (3, 2), (6, 4), (1, 9), (10, 3), (2, 3), (1, 7)]
print(list)

#lambda to kompaktowa funkcja
list2 = sorted(list,key=lambda x: x[1])
print(list2)


#alternatywnie
def secondItem(x):
    return x[0]

list3 = sorted(list, key=secondItem)
print(list3)

