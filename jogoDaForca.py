import random, os

# Lista de palavras & dicas
palavras = [
    'Vermelho&Cor',
    'Canoas&Cidade',
    'Super-Homem&Herói'
]

# Selecionar PALAVRA e DICA da partida
n = random.randint(0, len(palavras)-1)
item = palavras[n].split('&')
palavra = item[0]
dica = item[1]

# Gerando o texto da forca
forca = []
for i in palavra:
    if(i == '-' or i == ' '):
        forca.append('-')
    else:
        forca.append('_')

# Configurando dificuldade
dif = input('[1] Fácil / [2] Normal / [3] Difícil : ')
if(dif == '1'):
    dif = 1
elif(dif == '2'):
    dif = 2
else:
    dif = 2
    dica = 'Não tem dica.'

# Montando etapas da arte da forca
arte = [
    '''
    ┌───┐    
    │
    │
    │
    ┴
    ''',
    '''
    ┌───┐    
    │   O
    │
    │
    ┴
    ''',
    '''
    ┌───┐    
    │   O
    │   |
    │
    ┴
    ''',
    '''
    ┌───┐    
    │   O
    │  /|
    │
    ┴
    ''',
    '''
    ┌───┐    
    │   O
    │  /|\\
    │
    ┴
    ''',
    '''
    ┌───┐    
    │   O
    │  /|\\
    │  /
    ┴
    ''',
    '''
    ┌───┐    
    │   O
    │  /|\\
    │  / \\
    ┴
    ''',
    ]

erros = ''
vida = 0

# Laço da partida
while True:
    os.system('cls')
    
    # Montando texto da forca
    texto = ''
    for i in forca:
        texto += i

    # Verificando vitória
    if(palavra == texto):
        os.system('cls')
        input('VOCÊ GANHOU!')
        break

    # Apresentando informações e pergutando ao jogador
    letra = input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dica}
    Erros: {erros}

    Escolha uma letra: ''')

    # Verificando acerto e atualizando a forca
    acerto = False
    for i in range(len(palavra)):
        if(letra.lower() == palavra[i].lower()):
            acerto = True
            forca[i] = palavra[i]
    if(acerto == False):
        vida += dif
        erros += letra.upper()

    # Verificando derrota
    if(vida >= 6):
        os.system('cls')
        input('VOCÊ PERDEU!')
        break
