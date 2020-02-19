#Soma dos algarismos

n = int(input("Digite um numero inteiro"))

soma = 0

ref = 10

while ( (n // ref) >0):
    soma = (n % ref) + soma
    n = n - (n % ref)
    n = n // 10
    
Final = soma + n

print(Final)

