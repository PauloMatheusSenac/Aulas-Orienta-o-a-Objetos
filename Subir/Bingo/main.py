from random import *
from roleta import*
from cartela import*

print("Quantas pessoas irão jogar?")
num_pessoas = int(input("Digite aqui>>>>"))

jogadores = []

for i in range(1, num_pessoas + 1):
    name = input(f"Digite o Nome da {i}ª pessoa:")
    player = Cartela(name)
    player.imprimedados()
    jogadores.append(player)

####################################################################################################################################################################################################################################
roleta = Roleta()

print("\nVai começar o BINGO!")

numeros_sorteados = []

for r in range(75):  
    input("Pressione Enter para gerar o próximo número!")
    numeroroleta = roleta.confere()
    print(f"Número Sorteado: {numeroroleta}")
    numeros_sorteados.append(numeroroleta)

    for player in jogadores:
        if player.verifica_vitoria(numeros_sorteados):
            print(f"Parabéns, {player.nome}! Você venceu o Bingo!")
            exit()

print("Não houve vencedor neste jogo de Bingo.")




