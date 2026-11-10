# Szymon Jaworski, zadanie nr 8 z listy 4

numbers = []                                   #lista wyników

for i in range(100,401):                       #przedział 100-400
    number = ''                                #bufor na cyfry parzyste

    for j in str(i):                           #iteracja po cyfrach liczby

        if int(j) % 2 == 0:                    #jeśli cyfra parzysta
            number += j                        #dopisanie do bufora

        else:                                  #jeśli cyfra nieparzysta
            number = None                      #oznaczenie odrzucenia
            break                              #przerwanie pętli

    if number:                                 #dodanie tylko jeśli number niepusty/nie None
        numbers.append(int(number))            #konwersja na int i dodanie

print(numbers)                                 #wypisanie listy