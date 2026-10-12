a = int(input('a: '))
b = int(input('b: '))

if b >= a:
    a,b = b,a

Z = a % b
print(Z)
Z *= Z + 3

print(Z)
