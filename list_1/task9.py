import cmath
import math
import numpy
z = complex('4+3j')
z = complex(input("Podaj liczbę zespoloną: "))
modul = abs(z)
argument = math.degrees(cmath.phase(z))
con = numpy.conjugate(z)


print(z,modul,argument,con,sep='\n')
