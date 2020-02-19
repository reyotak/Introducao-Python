#Verificador de primos

n = int(input("Digite um numero inteiro" ))

i = (n - 1)

if n==1:
    print("não primo")
else:
    while n % i != 0 and i - 2 > 0:
        i = i - 1

    if (n % i != 0 or n ==2):
        print("primo")
    else:
        print("não primo")

    
    

        
