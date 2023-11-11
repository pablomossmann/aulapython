from os import system
import time, random

def main():
    while True:
        escolha = input('''
        Boas-vindas ao MemorEz!

        [1] Jogar
        [2] Sobre
        [3] Sair

        > ''')

        if escolha == '1':
            jogar()
        elif escolha == '2':
            sobre()
        elif escolha == '3':
            system('cls')
            print('\n\tObrigado por jogar!')
            time.sleep(3)
            break
        else:
            input('\n\tOpção inválida.')

        system('cls')

def jogar():
    caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    tamanho = 3
    tempo = 5.0
    fase = 1
    
    while True:
        system('cls')
        input(f'\n\tFase {fase}: [Enter]')
        codigo = ''
        for i in range(tamanho):
            codigo += random.choice(caracteres)
            
        system('cls')
        print(f'\n\tFase {fase}: {codigo}')
        time.sleep(tempo)
        system('cls')

        c = input(f'''
\tFase {fase}: {tamanho*"▓"}

\tInforme o código: ''')
        
        if(c == codigo):
            tamanho += 1
            tempo -= 0.2
            fase += 1
        else:
            input(f'''
\tVocê falhou na fase {fase}.
\tO código era "{codigo}"e apareceu por {tempo}s...''')
            break

def sobre():
    system('cls')
    input('''
    SOBRE:

    Seu objetivo é memorizar o código que
    aparecerá na tela e depois informa-lo.

    Porém à cada acerto fica mais difícil,
    aumentando o tamanho do código e
    diminuindo o tempo de memorização...

    O quão longe será que você consegue chegar?''')

main()
