"""
a -> lista;
n -> número;
s -> string (palavra);
b -> verdadeiro ou falso;
variável -> informação guardada;
função -> parte de codigo separada.
"""

#Adicionando funções.
from time import sleep
from random import randint 


while 1:
    #Definindo variáveis.
    sLetraDaPalavra = 0
    aLetrasCertas=[]
    aPalavras = ['internet', 'hacker', 'bug', 'cyberbullying', 'python', 'java', 'javascript', 'ip', 'linux', 'android', 'ios', 'windows', 'processador', 'browser', 'wifi']
    sPalavraSorteada = aPalavras[randint(0, 14)] #Sorteando uma palavra da lista.
    nTentativasRestantes = 10
    aLetrasUsadas = []
    aPontuacoes = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '¹', ']', '^', '_', '`', '{', '|', '}', '~', '²', '³', '£', '¢', '¬', '§', 'ª', 'º', '°', '\\']

    #Mostrando tela inicial.
    print('_ '*len(sPalavraSorteada))
    print(f'Letras Usadas: {aLetrasUsadas}')
    print(f'Tentativas Restantes: {nTentativasRestantes}')

    #Processo do jogo.
    while nTentativasRestantes != 0:
        
        #Definindo variáveis internas.
        sPontuacaoDeVerificacaoDePontuacoes = 0
        bPontuacaoOuNao = False
        sLetraDeVerificacaoDaPalavraSorteada = 0
        sLetraDeVerificacaoDasLetrasCertas = 0
        bUnderlineOuLetra = False
        sLetraDeVerificacaoSeJaFoiUsada = 0
        bEssaLetraJaFoiUsada = False
        sLetraDeVerificacaoSeJaFoiAcertada = 0
        bEssaLetraJaFoiAcertada = False
        bTodasAsLetrasForamDescobertas = True

        #Perguntando ao usuário.
        sLetraEntrada = input('Digite uma letra: ').lower()
        print()

        #Verrificando resposta.

        #Verrificando se a resposta é uma letra.
        if len(sLetraEntrada) != 1:
            print('ERRO: Digite somente uma letra!')
            print()
            nTentativasRestantes -= 1
            continue #Volta para o começo.
        try:
            TestesLetraEntrada=int(sLetraEntrada)
            print('ERRO: Digite somente uma letra!')
            print('')
            nTentativasRestantes -= 1
            continue #Volta para o começo.
        
        except:
            print('')

        while sPontuacaoDeVerificacaoDePontuacoes <= len(aPontuacoes)-1:
            if sLetraEntrada != aPontuacoes[sPontuacaoDeVerificacaoDePontuacoes]:
                sPontuacaoDeVerificacaoDePontuacoes += 1
            else:
                bPontuacaoOuNao = True
                sPontuacaoDeVerificacaoDePontuacoes += 1

        if bPontuacaoOuNao == True:
            print('ERRO: Digite somente uma letra!')
            print('')
            nTentativasRestantes -= 1
            continue #Volta para o começo.

        #Verrificando se a resposta é válida.
        if sPalavraSorteada.count(sLetraEntrada) < 1:
            bEssaLetraJaFoiUsada = False

            #Verrifica se a resposta já foi usada.
            while sLetraDeVerificacaoSeJaFoiUsada <= len(aLetrasUsadas)-1:
                if sLetraEntrada == aLetrasUsadas[sLetraDeVerificacaoSeJaFoiUsada]:
                    bEssaLetraJaFoiUsada = True
                sLetraDeVerificacaoSeJaFoiUsada += 1

            if bEssaLetraJaFoiUsada == False:
                aLetrasUsadas.append(sLetraEntrada)
                nTentativasRestantes -= 1
                
        #Verrifica se a resposta já foi acertada.
        else:
            bEssaLetraJaFoiAcertada = False
            while sLetraDeVerificacaoSeJaFoiAcertada <= len(aLetrasCertas)-1:
                if sLetraEntrada == aLetrasCertas[sLetraDeVerificacaoSeJaFoiAcertada]:
                    bEssaLetraJaFoiAcertada = True
                sLetraDeVerificacaoSeJaFoiAcertada += 1

            if bEssaLetraJaFoiAcertada == False:
                aLetrasCertas.append(sLetraEntrada)    

        bTodasLetrasForamDescobertas = True
        while sLetraDeVerificacaoDaPalavraSorteada <= len(sPalavraSorteada)-1:
            sLetraDeVerificacaoDasLetrasCertas = 0
            bUnderlineOuLetra = False
            while sLetraDeVerificacaoDasLetrasCertas <= len(aLetrasCertas)-1:
                if sPalavraSorteada[sLetraDeVerificacaoDaPalavraSorteada] == aLetrasCertas[sLetraDeVerificacaoDasLetrasCertas]:
                    print(sPalavraSorteada[sLetraDeVerificacaoDaPalavraSorteada],end=" ")
                    bUnderlineOuLetra = True

                sLetraDeVerificacaoDasLetrasCertas += 1
                

            if bUnderlineOuLetra == False:
                print('_',end=" ")
                bTodasLetrasForamDescobertas = False

        
            

            sLetraDeVerificacaoDaPalavraSorteada += 1
            
        print()
        print(f'Letras Usadas: {aLetrasUsadas}')
        print(f'Tentativas Restantes: {nTentativasRestantes}')

        #Verrifica se o usuário ganhou.
        if bTodasLetrasForamDescobertas == True:
            print('')
            print('Parabéns!!!')
            print('Você ganhou...')
            print('Obrigado por jogar!')
            if sPalavraSorteada == 'bug':
                sleep(2) #Espera dois segundos.
                for nContador in range(0, 44):
                    print('10101010101010101010101010010101010101001010101001010101001010101010010101010010101001010100101010010101010010101001010101001010100101010000000001111111001010101001010101010100101\n10101010100101001010101010010101010101001010101010100101010101010100010101010101010100101010100101010101001010101001010100101010010100101010010101001010000101011110100101001010100\n10101010010101010010101010100101010011010101000101001010010101010010010100101001010010100101010010100100000111111111100000000010101010010101010010101010010100101010100101010011111\n')
            break

    #Verrifica se o usuário perdeu.
    if nTentativasRestantes == 0:
        print('')
        print('Você perdeu!')
        print('Tente novamente!')

    sleep(2.5) #Espera dois segundos e meio.
    
    for nContador in range(0, 50):
        print()
    

 
 
 
 
 
 
 
"""
#Exemplo de funcionamento para 'bola'
_ _ _ _
letras usadas:
tentativas restantes: 10
 
f
 
_ _ _ _
letras usadas: [ f ]
tentativas restantes: 9
 
g
 
_ _ _ _
letras usadas: [ f, g ]
tentativas restantes: 8
 
b
 
b _ _ _
letras usadas: [ f, g ]
tentativas restantes: 8
"""
