# Szymon Jaworski, zadanie nr 6 z listy 5

def harmonic_series(n):                        #funkcja licząca sumę szeregu harmonicznego
    total = 0                                    #suma startowa
    for i in range(1,n+1):                     #pętla 1..n
        total += 1/i                             #dodanie kolejnego wyrazu 1/i
    return total                                 #zwrot sumy

print(harmonic_series(2))                      #wywołanie dla n=2, wynik 1.5