# Szymon Jaworski, zadanie nr 2 z listy 1

import math

def triangleArea(a,b,angle):                    #definicja funkcji
    radians = angle * (math.pi/180)             #zamiana stopni na radiany
    return 0.5 * a * b * math.sin(radians)      #wzór na pole

print(triangleArea(3,4,30))                     #2.9999999999999996

