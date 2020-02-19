#anti copia



import re

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    texto_mais_provavel = avalia_textos(textos, ass_cp)
    print("O autor do texto",texto_mais_provavel," está infectado com COH-PIAH")
    
        
    
    

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def n_de_letras(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de caracteres'''
    n_de_caract = 0
    for palavra in lista_palavras:
         n_de_caract = n_de_caract + len(palavra)

    return n_de_caract
    

def compara_assinatura(as_a, as_b):
    grupo_comparado = []
    elementosgrupo = 0
    n = 0
    similaridade = 0
    
    while n <= 5:
        if as_a[n] > as_b[n]:
            elementosgrupo = as_a[n] - as_b[n]
        else:
            elementosgrupo = as_b[n] - as_a[n]
            
        grupo_comparado.append(elementosgrupo)
        n = n + 1

    for parametro in grupo_comparado:
        similaridade = similaridade + parametro
    similaridade = similaridade / 6
        
    
    return similaridade
            
        

def calcula_assinatura(texto):
    calculado_ass = []
    sentencas_no_texto = separa_sentencas(texto)
    frases_no_texto = []
    palavras_no_texto = []
    
    for sentenca in sentencas_no_texto:
        frases = separa_frases(sentenca)
        frases_no_texto = frases + frases_no_texto
        for frase in frases:
            palavras = separa_palavras(frase)
            palavras_no_texto = palavras_no_texto + palavras
        
    palavras_unicas_no_testo = n_palavras_unicas(palavras_no_texto)
    palavras_diferentes_no_texto = n_palavras_diferentes(palavras_no_texto)
    total_letras = n_de_letras(palavras_no_texto)
    total_caract = len(texto)

    wal = total_letras / len(palavras_no_texto)
    ttr = palavras_diferentes_no_texto / len(palavras_no_texto)
    hlr = palavras_unicas_no_testo / len(palavras_no_texto)
    sal = (total_caract - len(sentencas_no_texto) ) / len(sentencas_no_texto)
    sac = len(frases_no_texto) / len(sentencas_no_texto)
    pal = (total_caract - len(frases_no_texto))  / len(frases_no_texto)

    return [wal,ttr,hlr,sal,sac,pal]
    

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    n = 0
    maior_texto = 0
    similaridade = 0
    maior_similaridade = 999
    
    while n < len (textos) :
        ass_texto = calcula_assinatura(textos[n])
        
        similaridade = compara_assinatura(ass_texto,ass_cp)
        if similaridade < maior_similaridade:
            maior_texto = n + 1
            maior_similaridade = similaridade
        n = n + 1
        similaridade = 0

    return maior_texto







###TESTES####

def test_main():
    ass_cp = test_le_assinatura()
    textos = test_le_textos()
    texto_mais_provavel = avalia_textos(textos, ass_cp)
    if texto_mais_provavel != 2:
        print("O texto mais provavel deu ",texto_mais_provavel,"a resposta certa era 2")

def test_le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''

    wal = 4.79
    ttr = 0.72
    hlr = 0.56
    sal = 80.5
    sac = 2.5
    pal = 31.6

    grupotest = [wal, ttr, hlr, sal, sac, pal]

    print(grupotest)

    return [wal, ttr, hlr, sal, sac, pal]

def test_le_textos():
    textos = ["Navegadores antigos tinham uma frase gloriosa:Navegar é preciso; viver não é preciso. Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.", "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.","NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."]

    return textos
        
        
        

