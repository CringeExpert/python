# Szymon Jaworski, zadanie nr 3 z listy 1

import math                                    #import modułu matematycznego

def triangleArea(a,b,angle):                   #funkcja licząca pole trójkąta
    radians = angle * (math.pi/180)            #zamiana stopni na radiany
    return 0.5 * a * b * math.sin(radians)     #wzór na pole

a = int(input('podaj bok a: '))                #pobranie boku a
b = int(input('podaj bok b: '))                #pobranie boku b
angle = int(input('podaj kąt zawarty między bokami: '))  #pobranie kąta

print(triangleArea(a,b,angle))                 #wypisanie pola