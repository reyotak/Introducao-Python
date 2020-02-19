###

l=int(input("digite a largura"))
a=int(input("digite a altura"))
li = l
ai = a
while a == ai:
    while l > 0:
        print("#",end='')
        l = l -1
    l = li
    a = a - 1
    print()
while a >1 :
    print("#",end='')
    while l > 1:
        if l == 2:
            print("#",end='')
            l = l -1
        else:
            print(" ",end='')
            l = l -1
    l = li
    a = a - 1
    print()
while a > 0:
    while l > 0:
        print("#",end='')
        l = l -1
    l = li
    a = a - 1
    print()
       
