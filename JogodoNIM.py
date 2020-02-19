#Jogo do NIM

def main():
    print("Bem vindo ao jogo do NIM! Escolha: ")
    print()
    print("1 - para jogar uma partida isolada")
    modo =int(input("2 - para jogar um campeonato""\n"))

    if modo == 1:
        print("**** Rodada 1 ****""\n")
        solo()
        print("**** Final de Partida! ****""\n")
        print("Derrota!")

    if modo == 2:
        print("**** Rodada 1 ****")
        solo()
        print("**** Rodada 2 ****")
        solo()
        print("**** Rodada 3 ****")
        solo()
        print("**** Final do Campeonato! ****""\n")
        print( "Placar: Você 0 X 3 Computador")
        main()
        
    else:
        print("Modo inválido!!!")




def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    #Condicao de inicio
    while (n <= 1 or n <=m or m<=0):
        print("Deve haver ao menos 2 peças inicialmente e ser retirado no máximo uma peça a menos do que o número de peás inicias!!!""\n")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
    #Fim da conddicao de inicio
    return n,m

    #Inicio do Jogador    
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
            
            pnm = pnm - ptp
            print("Voce tirou",ptp,"peça(s).")
            print("Agora resta apenas",pnm,"peça no tabuleiro")
            ptc =(m + 1) - ptp
            pnm = pnm - ptc
            print("O computador tirou",ptc,"peça(s).")
            print("Agora resta apenas",pnm,"peça no tabuleiro")
        print("Fim do jogo! O computador ganhou!")
            
    else:
        print ("O computador começa! :DD")
        while pnm > 0:
            ptc = 0
            ptp = 0
            ptc = pnm % (m + 1)
            pnm = pnm - ptc
            print("O computador tirou",ptc,"peça(s).")
            print("Agora resta apenas",pnm,"peça no tabuleiro")
            if pnm >0:
                ptp = int(input("Quantas peças você vai tirar? "))
            
                #Passagem anti roubo
                while ptp > m or ptp <=0:
                    print("Voce so pode tirar de 1 a",m,"pecas")
                    ptp = int(input("Quantas peças você vai tirar? "))
                 #Fim do anti roubo   
            
                pnm = pnm - ptp
                print("Voce tirou",ptp,"peça(s).")
                print("Agora resta apenas",pnm,"peça no tabuleiro")
            else:
                print("Fim do jogo! O computador ganhou!")

def  usuario_escolhe_jogada(n,m):
    def partida()
    

