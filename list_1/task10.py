import cmath
import math

z = complex('1j')
sin = cmath.sin(z)
cos = cmath.cos(z)

print(z,sin,cos,'\n',sep='\n')
print((sin**2).real + (cos**2).real,sep='\n')
print((sin**2).imag + (cos**2).imag,sep='\n')