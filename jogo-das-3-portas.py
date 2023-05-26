#jogo das 3 portas
#há três portas
#atrás de duas delas há um carro, e nas outras duas uma cabra
#o usuário escolhe uma porta
#o apresentador, que sabe onde está o carro, abre uma outra porta onde está uma cabra
#o usuário tem a opção de manter a escolha ou mudar de porta

import random
lista = [False] * 3

while True:
    escolha_usr = int(input("Escolha uma porta: "))
    if escolha_usr in [1, 2, 3]:
        break

# a porta que contém o carro é escolhida aleatoriamente
porta_carro = random.randint(1, 3)
lista[porta_carro - 1] = True
#a porta que o apresentador abre deve ser uma que não tenha sido escolhida pelo usuário e também que não contenha o carro

porta_aberta = random.choice([p for p in [1, 2, 3] if p != escolha_usr and p != porta_carro])
print(f"O apresentador abriu a porta {porta_aberta},  atrás da qual está uma cabra.")


#o usuário deve decidir se mantém a porta ou se muda de decisão
decisao_final = str(input("Você deseja manter a escolha? ('S'/'N') ")).upper()

escolha_final = escolha_usr

if decisao_final == 'N':
    escolha_final = random.choice([p for p in [1, 2, 3] if p != escolha_usr and p != porta_aberta])

print(f"\nO carro estava na porta {porta_carro}...")
print(f"Você abriu a porta {escolha_final}...")

if escolha_final == porta_carro:
    print("Portanto você ganhou!")
else:
    print("Portanto você perdeu!")

