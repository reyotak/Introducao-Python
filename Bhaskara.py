#Calculadora de funcao de segundo grau

import math

A = float(input("Qual a constante a? "))

B = float(input("Qual a constante b? "))

C = float(input("Qual a constante c? "))

Delta = (B*B) - (4*A*C)

if (Delta > 0 and B + Delta > 0):
    R1 = ( -B + (math.sqrt(Delta))) / (2*A)
    R2 = ( -B - (math.sqrt(Delta))) / (2*A)
    print("as raízes da equação são",R2,"e",R1)
else:
    if(Delta > 0):
        R1 = ( -B + (math.sqrt(Delta))) / (2*A)
        R2 = ( -B - (math.sqrt(Delta))) / (2*A)
        print("as raízes da equação são",R1,"e",R2)
    else:

        if Delta == 0:
            R1 = ( -B + (math.sqrt(Delta))) / (2*A)
            print("a raiz desta equação é",R1)
        else:
            print("esta equação não possui raízes reais")
        
        
