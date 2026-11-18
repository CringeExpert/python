# Szymon Jaworski, zadanie nr 7 z listy 5

def factorial(n):                              #funkcja licząca silnię
    result = 1                                 #iloczyn startowy
    for i in range(1,n+1):                     #pętla 1..n
        result *= i                            #mnożenie kolejnych liczb
    return result                              #zwrot wyniku

print([factorial(x) for x in range(1,10)])     #silnie dla liczb 1..9