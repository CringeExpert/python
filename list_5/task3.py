import math

def conv(value,type='deg'):
    if type == 'deg':
        return str(math.radians(value)/math.pi) + '\u03C0'
    else:
        return str(math.degrees(value*math.pi)) + '\u00B0'

print(conv(2,'rad'))