#jogo da forca
import random
import os
palavra = ["computador", "cachorro", "mulher", "brasil", "parede"]

palavra = random.choice(palavra)
tentativas = 0
chances = 5
letras_escolhidas = []
estado_atual = ["__"] * len(palavra)

print("Seja bem vindo ao jogo da forca.")
print("O seu objetivo é acertar a palavra secreta.")

def escolherNivel():
    print("1. Fácil\n2. Intermediário\n3.Difícil")
    while True:
        escolha = int(input("Escolha o número correspondente ao nível preferível: "))
        if escolha == 1:
            break
        elif escolha == 2:
            chances -= 2
            break
        elif escolha == 3:
            chances -= 3
            break
        else:
            print("Escolha inválida!\n")
def verificar(s, letra):
    global palavra
    for i in range (s, len(palavra)): #para economizar tempo, faço com que a iteração comece na primeira ocorrência da letra
        if letra == palavra[i]:
            estado_atual[i] = letra
def jogar():
    global tentativas
    global chances
    while tentativas < chances: #completar
        if("".join(estado_atual) == palavra):
            break
        #os.system('clear')
        #qual o estado atual da palavra
        print(" ".join(estado_atual))
        while True:
            letra = str(input("Insira uma letra: "))
            if not letra in letras_escolhidas:
                break
            else:
                print("Essa letra já foi escolhida!\n")
        letras_escolhidas.append(letra)

        if letra in palavra:
            print("Parabéns, você acertou a letra!\n")
            verificar(palavra.index(letra), letra)
            #completar
        else:
            print("Que pena, você errou!\n")
            tentativas += 1
        #quantas tentativas ainda faltam
        print(f"Você já fez {tentativas} tentativas erradas e ainda tem {chances - tentativas} tentativas")
        #quais as letras já foram usadas
        print(f"As letras que você já tentou são:\n {letras_escolhidas}\n")
    if tentativas == chances:
        print("Você perdeu!")
    else:
        print("Parabéns! Você ganhou!")
        print(f"A palavra correta era {palavra}!")
jogar()
