#nprimos

def n_primos(n):
    div = n - 1
    resto = 0
    numerodeprimos = 1
    ehprimo = True
    
    while n > 2:
        while div > 1 and ehprimo==True:
            resto = n % div
            if resto == 0:
                ehprimo = False
            if div == 2 and ehprimo==True:
                numerodeprimos = numerodeprimos + 1
            div = div - 1
        n = n - 1
        div = n - 1
        ehprimo = True

    return numerodeprimos
        
