#Maior Primo

    
def verf_primo(n):
    div = n - 1
    while (n % div != 0):
        div = div - 1
    if div > 1:
        naoehPrimo = True
    else:
        naoehPrimo = False
    return naoehPrimo

def maior_primo(n):
    while verf_primo(n) == True:
        n = n - 1
    return(n)
        
