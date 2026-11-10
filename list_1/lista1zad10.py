# Szymon Jaworski, zadanie nr 10 z listy 1

import cmath                                   #moduł do liczb zespolonych

z = complex('1j')                              #liczba zespolona z = i
sin_z = cmath.sin(z)                           #sin(z)
cos_z = cmath.cos(z)                           #cos(z)
result = sin_z**2 + cos_z**2                   #sprawdzenie sin**2(z) + cos**2(z)

print(result)                                  #wynik ≈ (1+0j), czyli warunek spełniony