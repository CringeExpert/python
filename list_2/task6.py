list = ["Kasia","Basia","Marek","Darek"]
print(list)

list.append("Józek")
print(list)

persons1 = ["Ania","Basia"]
list.extend(persons1)
print(list)

list.sort()
print('\n',list)
print('ostatni: ', list[3])
print('dwóch pierwszych: ', list[:2])
print('dwóch ostatnich: ', list[-2:])

while "Basia" in list:
    list.remove("Basia")
print('\n',list)

print("ilość studentów", len(list))

list = tuple(list)
print(list)

