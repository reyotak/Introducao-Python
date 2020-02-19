#Divisivel poe 3:

N = int(input("Numero ?"))

S3 = N % 3

S5 = N % 5

if ( S3 == 0 and S5 == 0):
    print("FizzBuzz")
else:
    print(N)

