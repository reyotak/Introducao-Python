#Divisivel poe 3 e 5:

def div35(n):

    nehdiv = False

    S3 = n % 3

    S5 = n % 5

    if ( S3 == 0 and S5 == 0):
        return True
    else:
        return False

#Divisivel poe 5:

def buzz(n):

    nehdiv = False

    Sim = n % 5

    if ( Sim == 0):
        return True
    else:
        return False

#Divisivel poe 3:

def fizz(n):

    nehdiv = False

    Sim = n % 3

    if ( Sim == 0):
        return True
    else:
        return False

def fizzbuzz(n):
    if div35(n) == True:
        return "FizzBuzz"
    else:
        if buzz(n) == True:
            return "Buzz"
        else:
            if fizz(n) == True:
                return "Fizz"
            else:
                return n
    

