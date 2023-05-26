import random

#declarar matriz
matriz = [' '] * 9 # será uma lista simples
numero_de_jogadas = 0
valueUsuario, valueCPU = ['', '']
vencedor = ''

def escolherPeca():
    global valueUsuario
    global valueCPU

    options = ('X', 'O')
    while True:
        valueUsuario = str(input("Escolha a sua peça: ")).upper()
        if valueUsuario in options:
            break
    if valueUsuario == options[0]:
        valueCPU = options[1]
    else:
        valueCPU = options[0]
    
def desenharMatriz():
    for row in [matriz[i * 3 : (i + 1) * 3] for i in range (3)]:
        print('| ' + ' | '.join(row) + ' |')
    print("\n")

def jogar(linha, coluna, value):
    global matriz
    global numero_de_jogadas

    matriz[3 * linha + coluna] = value
    numero_de_jogadas += 1


def Usuario():
    global valueUsuario
    global numero_de_jogadas

    while True:
        linha = int(input("Escolha a linha: "))
        coluna = int(input("Escolha a coluna: "))
        print("\n")
        if 3 > linha >= 0 and 3 > coluna >= 0:
            if matriz[3 * linha + coluna] == ' ':
                jogar(linha, coluna, valueUsuario)
                break
            else:
                print("A posição já está ocupada!\n")
        else:
            print("Posição inválida!\n")


def CPU():
    global valueCPU
    global numero_de_jogadas

    while True:
        if numero_de_jogadas == 9:
            return False
        linha = random.randrange(3)
        coluna = random.randrange(3)

        if matriz[3 * linha + coluna] == ' ':
            jogar(linha, coluna, valueCPU)
            break


def verificarVitoria():
    global valueUsuario
    global valueCPU
    global vencedor
    #verificar linhas
    for row in [matriz[i * 3 : (i + 1) * 3] for i in range (3)]:
        if "".join(row) == "X" * 3 or "".join(row) == "O" * 3:
            vencedor = "Usuario" if valueUsuario in "".join(row) else "CPU"
            return True
        
    #verificar colunas
    for row in [matriz[i::3] for i in range(3)]:
        if "".join(row) == "X" * 3 or "".join(row) == "O" * 3:
            vencedor = "Usuario" if valueUsuario in "".join(row) else "CPU"
            return True
        
    #verificar diagonais
    for row in [matriz[i:9-i:4-i] for i in range(0,3,2)]:
        if "".join(row) == "X" * 3 or "".join(row) == "O" * 3:
            vencedor = "Usuario" if valueUsuario in "".join(row) else "CPU"
            return True
            
#falta melhorar a lógica do jogo a partir daqui
escolherPeca()
while True:
    Usuario()
    if verificarVitoria():
        print(f"{vencedor} ganhou!")
        break
    if numero_de_jogadas == 9:
        break
    CPU()
    print(f"Número de jogadas: {numero_de_jogadas}\n")
    if verificarVitoria():
        print(f"{vencedor} ganhou!")
        break    
    desenharMatriz()
