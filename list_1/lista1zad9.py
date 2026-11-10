# Szymon Jaworski, zadanie nr 9 z listy 1

import cmath                                   #moduł do liczb zespolonych
import math                                    #moduł matematyczny

z = complex(input("Podaj liczbę zespoloną: ")) #pobranie liczby zespolonej od użytkownika
modul = abs(z)                                 #moduł |z|
argument = math.degrees(cmath.phase(z))        #argument w stopniach (cmath.phase zwraca radiany)
con = z.conjugate()                            #sprzężenie

print(z,modul,argument,con,sep='\n')           #wypisanie wyników w nowych liniach