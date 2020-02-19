#removelistarepetidos

def remove_repetidos(lista):
    lista.sort()
    lista_unica = []
    for n in lista:
        if n not in lista_unica:
            lista_unica.append(n)

    return lista_unica
            
