import math

def triangleArea(a,b,angle):
    radians = angle * (math.pi/180)
    return 0.5 * a * b * math.sin(radians)

print(triangleArea(3,4,30))

# można użyć 
# import numpy as np
# math.sin(np.deg2rad(angle))
# można użyć 
# math.sin(math.radians(angle))