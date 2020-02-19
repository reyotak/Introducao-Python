#Calculo Fatorial

n = int(input("Digite o valor de n "))
Fat = 1
while ( n > 1):
    Fat = Fat*(n*(n-1))
    n = n-2
print(Fat)
