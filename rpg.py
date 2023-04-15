import random
import os
import time

p_nome = ''
p_vida = 10
p_dano = 0
p_classe = ''

m_vida = random.randint(8, 16)

menu = 0
jogo = 0

while menu != 3:
    while (menu < 1) or (menu  > 3):
        os.system('cls')
        menu = int(input('''

        ●▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬●
        ░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░GEEK░HERO░RPG░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░
        ●▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬●

                ●▬▬▬▬▬▬▬▬▬●
                |[1] Jogar|
                |▬▬▬▬▬▬▬▬▬|
                |[2] Sobre|
                |▬▬▬▬▬▬▬▬▬|
                |[3] Sair |
                ●▬▬▬▬▬▬▬▬▬●

                > '''))

    if menu == 1:
        if p_nome == '':
            os.system('cls')
            print('\n\tBoas-vindas jogador! Vamos montar sua ficha...')
            time.sleep(2)
            p_nome = input('''\n\tNome: ''')

        while jogo != 3:
            os.system('cls')
            jogo = int(input(f'''

                    {p_nome}, o que quer fazer?
        
                    ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
                    |[1] Explorar   |
                    |▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬|
                    |[2] Editar nome|
                    |▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬|
                    |[3] Sair       |
                    ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●

                    > '''))
            
            if jogo == 1:
                os.system('cls')
                print('\n\tVocê estava andando e encontrou um monstro...')
                time.sleep(3)
                os.system('cls')
                
                while True:
                    print('\n\t',p_nome)
                    print('\t',p_vida*"█")
                    print('\n\t Monstro')
                    print('\t',m_vida*"█")

                    acao = int(input('''

                        ●▬▬▬▬▬▬▬▬▬●
                        |[1] Bater|
                        |▬▬▬▬▬▬▬▬▬|
                        |[2] Fugir|
                        ●▬▬▬▬▬▬▬▬▬●

                        > '''))
                    if acao == 1:
                        dano = random.randint(1,4)
                        m_vida -= dano
                        print('\n\tVocê causou',dano,' de dano no monstro.')
                        time.sleep(3)
                    elif acao == 2:
                        print('\t',p_nome,'fugiu covardemente.')
                        time.sleep(3)
                        break
                    
                    dano = random.randint(1,4)
                    p_vida -= dano
                    print('\tO monstro causou',dano,' de dano em você.')
                    time.sleep(3)
                    os.system('cls')

            if jogo == 2:
                os.system('cls')
                p_nome = input('''\n\tNome: ''')

            if jogo == 3:
                print('\t',p_nome,'saiu do jogo.')
                time.sleep(3)
        
    elif menu == 2:
        print('\n\tEste é o jogo de RPG mais GEEK que verás.')
        time.sleep(3)
        
    elif menu == 3:
        break

    jogo = 0
    menu = 0

print('\n\tFim de jogo.')
time.sleep(3)

