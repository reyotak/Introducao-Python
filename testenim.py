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
        print("**** Rodada 1 ****""\n")
        partida()
        print("**** Final de Partida! ****""\n")
        print("Derrota!")
        main()

    if modo == 2:
        print("**** Rodada 1 ****")
        partida()
        print("**** Rodada 2 ****")
        partida()
        print("**** Rodada 3 ****")
        partida()
        print("**** Final do Campeonato! ****""\n")
        print( "Placar: Você 0 X 3 Computador")
        main()
        
    else:
        print("Modo inválido!!!")

def usuario_escolhe_jogada(n,m):

def computador_escolhe_jogada(n,m):

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
            ptc = 0
            ptp = 0
            ptp = int(input("Quantas peças você vai tirar? "))
            
            #Passagem anti roubo
            while ptp > m or ptp <=0:
                print("Voce so pode tirar de 1 a",m,"pecas")
                ptp = int(input("Quantas peças você vai tirar? "))
             #Fim do anti roubo   
            
            n = n - ptp
            print("Voce tirou",ptp,"peça(s).")
            print("Agora resta apenas",n,"peça no tabuleiro")
            ptc =(m + 1) - ptp
            n = n - ptc
            print("O computador tirou",ptc,"peça(s).")
            print("Agora resta apenas",n,"peça no tabuleiro")
        print("Fim do jogo! O computador ganhou!")

    #Computador comeca        
    else:
        print ("O computador começa! :DD")
        while n > 0:
            ptc = 0
            ptp = 0
            ptc = n % (m + 1)
            n = n - ptc
            print("O computador tirou",ptc,"peça(s).")
            print("Agora resta apenas",n,"peça no tabuleiro")
            if n >0:
                ptp = int(input("Quantas peças você vai tirar? "))
            
                #Passagem anti roubo
                while ptp > m or ptp <=0:
                    print("Voce so pode tirar de 1 a",m,"pecas")
                    ptp = int(input("Quantas peças você vai tirar? "))
                 #Fim do anti roubo   
            
                n = n - ptp
                print("Voce tirou",ptp,"peça(s).")
                print("Agora resta apenas",n,"peça no tabuleiro")
            else:
                print("Fim do jogo! O computador ganhou!")

main()


