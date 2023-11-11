import os
import random

# Iniciando variáveis
p1 = 0
j1 = ''
p2 = 0
j2 = ''
rodada = 0
cont = 0

# Menu
modo = int(input('''

    MODO DE JOGO

[1] Jogador vs Jogador (não implementado)
[2] Jogador vs PC

> '''))

if(modo == 1):
    print('')
elif(modo == 2):
    vez = random.randint(1,2)
    while True: # Inicio da rodada
        a = '[1]'
        b = '[2]'
        c = '[3]'
        d = '   '
        e = '\°/'
        f = '   '
        tela = f'''

    Jogador [{p1}]: {j1}
         PC [{p2}]: {j2}
         
             _____________
            | {a} {b} {c} |
            | {d} {e} {f} |
        '''
        if(vez == 1): #Vez do jogador 1 atacar
            chute = 0
            while(chute<1 or chute>3):
                os.system('cls')
                print(tela)
                chute = int(input('\tJogador chuta em > '))
            defesa = random.randint(1,3)
            vez = 2
        else: #Vez do jogador 2 atacar
            chute = random.randint(1,3)
            defesa = 0
            while(defesa<1 or defesa>3):
                os.system('cls')
                print(tela)
                defesa = int(input('\tJogador defende em > '))
            vez = 1

        # Posição do goleiro e bola (estética opcional)
        if(chute == 1):
            a = ' O '
            b = '   '
            c = '   '
        elif(chute == 2):
            a = '   '
            b = ' O '
            c = '   '
        else:
            a = '   '
            b = '   '
            c = ' O '

        if(defesa == 1):
            d = '\°/'
            e = '   '
            f = '   '
        elif(defesa == 2):
            d = '   '
            e = '\°/'
            f = '   '
        else:
            d = '   '
            e = '   '
            f = '\°/'

        tela = f'''

    Jogador [{p1}]: {j1}
         PC [{p2}]: {j2}
         
             _____________
            | {a} {b} {c} |
            | {d} {e} {f} |
        '''
            

        #Verificar as combinações para montar o resultado
        os.system('cls')
        print(tela)
        if (vez == 2):
            if(chute == defesa):
                print(f'\tJogador chutou no {chute} e PC... DEFENDEU!')
                j1 += '- '
            else:
                print(f'\tJogador chutou no {chute} e PC pulou no {defesa}, GOOOL!')
                p1 += 1
                j1 += 'O '
        else:
            if(chute == defesa):
                print(f'\tPC chutou no {chute} e Jogador... DEFENDEU!')
                j2 += '- '
            else:
                print(f'\tPC chutou no {chute} e Jogador pulou no {defesa}, GOOOL!')
                p2 += 1
                j2 += 'O '

        # Contagem das rodadas 
        if(cont == 1):
            cont = 0
            rodada += 1
        else:
            cont = 1

        # Verificando a condição de vitória
        if(rodada>=5 and cont == 0):
            if(p1!=p2):
                break
        else:
            if((p1 > p2+2) or (p2 > p1+2)):
                break
        input()
    
    print('ACABOOOU!')
    input()
