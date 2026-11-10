# Szymon Jaworski, zadanie nr 4 z listy 5

def geo(n,a1=1,q=2):                           
    return a1*q**(n-1)                         #wzór: a_n = a1 * q^(n-1)

print(geo(3,3,3))                              #przykład