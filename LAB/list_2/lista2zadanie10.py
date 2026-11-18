# Szymon Jaworski, zadanie nr 10 z listy 2

list1 = [x for x in range(3,100,3)]            #lista wielokrotności 3 mniejszych od 100
print(list1)                                   #wypisanie listy

del list1[4::3]                                #usunięcie co trzeciego elementu, zaczynając od indeksu 4 (piąty element)

print(sum(list1)/len(list1))                   #średnia arytmetyczna (suma / liczba elementów)