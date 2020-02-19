#dimensoes matriz


    
def dimensoes_matriz(minha_matriz):
    i = 0
    j = 0
    for linhas in minha_matriz:
        for colunas in minha_matriz[i]:
            j = j + 1
        i = i + 1
    if j % i == 0:
        j = j // i
        return [i,j]
    else:
        return "Matriz invalida"


def soma_matrizes(m1,m2):
    dm1 = dimensoes_matriz(m1)
    dm2 = dimensoes_matriz(m2)
    if dm1 != dm2:
        return False
    else:
        i = 0
        j = 0
        lista_soma = []
        matriz_soma = []
        for lista in m1:
            j = 0
            for numero in lista:
                soma = numero + m2[i][j]
                lista_soma.append(soma)
                j = j + 1
            i = i + 1
            matriz_soma.append(lista_soma)
            lista_soma = []

    return matriz_soma

        
    
