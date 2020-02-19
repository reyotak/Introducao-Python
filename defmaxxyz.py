# Maximo

def maximoxy(x,y):
    if ( x >= y):
        return (x)
    else:
        return (y)

def maximo(x,y,z):
    if ( z >= maximoxy(x,y)):
        return (z)
    else:
        return maximoxy(x,y)
    

    
