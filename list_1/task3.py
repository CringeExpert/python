import math

def triangleArea(a,b,angle):
    radians = angle * (math.pi/180)
    return 0.5 * a * b * math.sin(radians)

a = int(input('podaj bok a: '))
b = int(input('podaj bok b: '))
angle = int(input('podaj kąt zawarty między bokami: '))

print(triangleArea(a,b,angle))