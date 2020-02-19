#Algarismo Adjacentes

n = int(input("Digite um numero inteiro"))

ult = 0

ant = n

naoAdjacente = True

if n >9:
    while n > 0 and naoAdjacente:

        ult = n % 10
        if ult == ant:
            naoAdjacente = False
        n = n // 10
        if n > 0:
            ant = n % 10
            n = n // 10
        if ult == ant:
            naoAdjacente = False
    if not naoAdjacente:
        print("sim")
    else:
        print("não")
else:
    print("não")

