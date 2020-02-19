#Jogo do NIM

# n == numero de pecas inicias
# m == numero max de pecas retiradas por rodada
#ptc == pecas tiradas computador
#ptp == pecas tiradas player

def main():
    print("Bem vindo ao jogo do NIM! Escolha: ")
    print()
    print("1 - para jogar uma partida isolada")
    modo =int(input("2 - para jogar um campeonato""\n"))

    if modo == 1:
        partida()
        print("**** Final de Partida! ****""\n")

    if modo == 2:
       campeonato()
        
    if modo !=1 and modo !=2:
        print("Modo inválido!!!")

def usuario_escolhe_jogada(n,m):
    ptp = int(input("Quantas peças você vai tirar?"))
    
    #Passagem anti roubo
    while ptp > m or ptp <=0:
        print("Oops! Jogada inválida! Tente de novo")
        ptp = int(input("Quantas peças você vai tirar? "))
    #Fim do anti roubo   
       
    print("Voce tirou",ptp,"peça(s).")
    n = n - ptp
    print("Agora resta apenas",n,"peça no tabuleiro")
    return ptp


def computador_escolhe_jogada(n,m):
    ptc = n % (m + 1)
    if ptc == 0:
        ptc = m    
    print("O computador tirou",ptc,"peça(s).")
    n = n - ptc
    print("Agora resta apenas",n,"peça no tabuleiro")
    return ptc


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while (n <= 1 or n <=m or m<=0):
        print("Deve haver ao menos 2 peças inicialmente e ser retirado no máximo uma peça a menos do que o número de peás inicias!!!""\n")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))

    #Player comeca
    if n % (m+1) == 0:
        print ("Voce começa! :DD")
        while n > 0:
            ptp = usuario_escolhe_jogada(n,m)
            n= n - ptp
        #Vez do PC
            ptc = computador_escolhe_jogada(n,m)
            n= n - ptc
                
        print("Fim do jogo! O computador ganhou!")

    #Computador comeca        
    else:
        print ("O computador começa! :DD")
        while n > 0:
            ptc = computador_escolhe_jogada(n,m)
            n = n - ptc
            if n >0:
                ptp = usuario_escolhe_jogada(n,m)
                n = n - ptp
            else:
                print("O computador ganhou!")


def campeonato():
    print("**** Rodada 1 ****")
    partida()
    print("**** Rodada 2 ****")
    partida()
    print("**** Rodada 3 ****")
    partida()
    print("**** Final do Campeonato! ****""\n")
    print( "Placar: Você 0 X 3 Computador")
    
main()





