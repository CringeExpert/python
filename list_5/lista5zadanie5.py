# Szymon Jaworski, zadanie nr 5 z listy 5

def factorial(n):                              #funkcja licząca silnię
    result = 1                                 #iloczyn startowy
    for i in range(1,n+1):                     #pętla 1..n
        result *= i                            #mnożenie kolejnych liczb
    return result                              #zwrot wyniku

def binomial_coefficient(n,k):                 #funkcja licząca symbol Newtona
    return factorial(n)//(factorial(k)*factorial(n-k))  #wzór: n! / (k! * (n-k)!) z dzieleniem całkowitym


def pascal(n):                                 #funkcja wypisująca trójkąt Pascala
    for i in range(0,n+1):                     #pętla po wierszach
        tab = []                               #pusta lista na wartości wiersza
        for j in range(0,i+1):                 #pętla po elementach wiersza
            tab.append(str(binomial_coefficient(i,j)))  #obliczenie i dodanie jako string
        print("{:^100}".format(' '.join(tab))) #wypisanie wiersza wyśrodkowanego w polu o 100 znakach

pascal(5)                                      #wywołanie dla n=5