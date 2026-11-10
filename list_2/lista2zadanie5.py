# Szymon Jaworski, zadanie nr 5 z listy 2

outside = input("Podaj zewnętrzny napis: ")    #pobranie napisu zewnętrznego
inside = input("Podaj środek: ")               #pobranie napisu do wstawienia

middle = len(outside) // 2                     #obliczenie środka napisu
left, right = outside[:middle], outside[middle:]  #podział na lewą i prawą część

result = left + inside + right                 #wstawienie napisu w środek

print(result)                                  #wypisanie wyniku