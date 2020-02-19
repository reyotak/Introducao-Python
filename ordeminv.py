#Inv. Sequencia


n = int(input("Digite um número: "))
lista = []
y = -1
    
while n != 0:
    lista.append(n)
    n = int(input("Digite um número: "))
for x in lista:
    print (lista[y])
    y = y - 1

