##Hipotenusa


def soma_hipotenusas(n):
    cont = 0
    soma = 0
    while n > 4:
        cont = é_hipotenusa(n)
        n = n - 1
        soma = soma + cont
    return soma
        

def é_hipotenusa(n):
    eh_triang_ret = False
    existe = n
    n_existe = 0
    i = n - 1
    j = 1
    while i > 1:
        while j < n and eh_triang_ret == False:
            i2 = i**2
            j2 = j**2
            n2 = n**2
            if n2 == i2 + j2:
                eh_triang_ret = True
                return existe
            else:
                j = j + 1
        i = i - 1
        j = 1
    return n_existe
        
    
