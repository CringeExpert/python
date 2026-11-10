# Szymon Jaworski, zadanie nr 6 z listy 1

import cmath                                   #import modułu do liczb zespolonych

def root(number,level):                        #funkcja licząca pierwiastek n-tego stopnia
    return number**(1/level)                   #pierwiastek = potęga 1/n

print(root(-17,2))                             #pierwiastek 2. stopnia z -17 (dla float daje liczbę zespoloną)

print(cmath.sqrt(-17))                         #pierwiastek z -17 z użyciem cmath = poprawna liczba zespolona