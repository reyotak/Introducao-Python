#dimensoes matriz


    
def dimensoes(minha_matriz):
    i = 0
    j = 0
    for linhas in minha_matriz:
        for colunas in minha_matriz[i]:
            j = j + 1
        i = i + 1

    j = j // i

    return print(i,j,sep='X')

