# Szymon Jaworski, zadanie nr 3 z listy 5

import math

def conv(value,type='rad'):
    if type == 'rad':                          #radiany na stopnie
        return str(math.degrees(value)) + '\u00B0'        
    else:                                      #stopnie na radiany
        return str(math.radians(value)/math.pi) + '\u03C0'  #wynik jako ułamek π
        

print(conv(180))                         #180° to 1.0pi