# Szymon Jaworski, zadanie nr 3 z listy 3

slubowanie = '''wstępując do wspólnoty akademickiej Uniwersytetu Wrocławskiego, ślubuję uroczyście:
- zdobywać wiedzę i umiejętności,
- postępować zgodnie z prawem, tradycji i dobrymi obyczajami akademickimi,
- dbać o dobre imię Uniwersytetu Wrocławskiego i godność studenta.'''

slubowanie2 = slubowanie[0].upper() + slubowanie[1:]  #pierwsza litera wielka


print(slubowanie2)                             #wypisanie poprawionego tekstu
print(slubowanie2.count(" i "))                #zliczenie wystąpień spójnika " i "
print(slubowanie2.count("i"))                  #zliczenie wystąpień litery "i"
print("Uniwersytet" in slubowanie2)            #sprawdzenie czy słowo występuje

words = slubowanie2.split()                    #podział na wyrazy po spacji
print(len(words), words)                       #liczba wyrazów i ich lista

rows = slubowanie2.split("\n")                 #podział na linie
print(len(rows),rows)                          #liczba linii i ich lista