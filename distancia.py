#Distancia entre dois pontos

import math

Xo = float(input("x1" ))
Yo = float(input("y1" ))

Xf = float(input("x2" ))
Yf = float(input("y2" ))

D = math.sqrt(((Xo-Xf)**2)+((Yo-Yf)**2))

if ( D >=10):
    print("longe")
else:
    print("perto")
