# Szymon Jaworski, zadanie nr 6 z listy 2

lista = ["Kasia","Basia","Marek","Darek"]      #lista studentów
print(lista)                                   #wypisanie listy

lista.append("Józek")                          #dodanie Józka na koniec
print(lista)                                   #wypisanie listy

persons1 = ["Ania","Basia"]                    #lista dodatkowych osób
lista.extend(persons1)                         #dodanie Ani i Basi
print(lista)                                   #wypisanie listy

lista.sort()                                   #sortowanie alfabetyczne
print('\n',lista)                              #wypisanie posortowanej listy
print('czwarty: ', lista[3])                   #czwarty student
print('dwóch pierwszych: ', lista[:2])         #dwóch pierwszych studentów
print('dwóch ostatnich: ', lista[-2:])         #dwóch ostatnich studentów

while "Basia" in lista:                        #usuwanie wszystkich Basi
    lista.remove("Basia")
print('\n',lista)                              #wypisanie listy po usunięciu

print("ilość studentów", len(lista))           #liczba studentów

lista = tuple(lista)                           #zamiana listy na krotkę
print(lista)                                   #wypisanie krotki