# Escreva um programa que faça um cadastro de clientes. Seu programa deve:
# [Entrada]: receber os seguintes dados do usuário:
# 1) o nome completo; 2) o RG do cliente; 3) o CPF e; 4) o telefone do cliente.
# [Processamento]: Seu programa deve armazenar todos os dados em uma ÚNICA LISTA. [Saída]: AO FINAL, SOMENTE AO FINAL, Seu programa deve mostrar (um cliente por linha):
# a) o nome completo do paciente, b) O RG; c) o CPF e; d) o telefone do cliente.
# Obs: o usuário deve fazer esse procedimento para quantos clientes ELE QUISER.
# Exemplo de Entrada:
# Digite o nome completo do cliente (ou digite 'sair' para encerrar): Enilda Caceres
# Digite o RG do cliente: 5478
# Digite o CPF do cliente: 5588
# Digite o telefone do cliente: 5877
# Digite o nome completo do cliente (ou digite 'sair' para encerrar): sair
# Exemplo de Saída:
# Cadastro de Clientes:
# ====================
# Nome: Enilda Caceres, RG: 5478, CPF: 5588, Telefone: 5877

# def errouu ():
#     print("Opção invalida, digite conforme solicitado!!!!")
#     return

# lista_de_clientes = [["Paulo","0101","0202","0303"]]

# opcao = input ("Digite 1 - para cadastrar ou 2 - para sair e gerar a lista:\nEscolha aqui>>>> ")
# while opcao != "1" and opcao != "2":
#     errouu()
#     opcao = input ("Digite 1 - para cadastrar ou 2 - para sair e gerar a lista:\nEscolha aqui>>>> ")
# else:
#     while opcao != "2":
#         nome = input("Digite seu nome: ")
#         rg = int (input("Digite seu RG: "))
#         cpf = int (input("Digite seu CPF: "))
#         telefone = int (input("Digite seu Telefone: "))
#         lista_de_clientes.append([nome,rg,cpf,telefone])
#         opcao = input ("Digite 1 - para cadastrar ou 2 - para sair e gerar a lista:\nEscolha aqui>>>> ")
#     else:
#         print("Cadastro de Clientes:")
#         print("="*10)
#         for i in lista_de_clientes: 
#             print (f"Nome: {i[0]}, RG: {i[1]} , CPF: {i[2]} , Telefone: {i[3]}")

#################################################################################################################
# Gerenciador de Estoque de Supermercado:
# Você é o gerente de um supermercado e precisa criar um sistema para gerenciar o estoque de produtos. Desenvolva um programa em python utilizando listas que permita adicionar, remover e exibir os produtos em estoque.
# estoque = []
# def errouuu():
#     print("Você está no erro, tente novamente.")
# def exibir_estoque():
#     if not estoque:
#         print("O estoque está vazio.")
#     else:
#         for item in estoque:
#             print(f"Nome: {item[0]}, Preço: {item[1]}")
# escolha = input("Digite uma das opções desejadas:\n1 - Adicionar\n2 - Remover\n3 - Exibir\n9 - Sair\nEscolha Aqui>>>> ")
# while escolha != "9":
#     if escolha == "1":
#         nome = input("Digite o nome do produto: ")
#         preco = input("Digite o preço do produto: ")
#         estoque.append([nome, preco])
#     elif escolha == "2":
#         apagar = input("Digite o nome do produto que vai ser excluído: ")
#         produto_encontrado = False
#         for i, item in enumerate(estoque):
#             if item[0] == apagar:
#                 estoque.pop(i)
#                 produto_encontrado = True
#                 break
#         if not produto_encontrado:
#             errouuu()
#     elif escolha == "3":
#         busca = input("Digite o nome do produto para buscar: ")
#         produto_encontrado = False
#         for item in estoque:
#             if item[0] == busca:
#                 print(f"O item foi encontrado: Nome: {item[0]}, Preço: {item[1]}")
#                 produto_encontrado = True
#                 break
#         if not produto_encontrado:
#             errouuu()
#     else:
#         errouuu()    
#     escolha = input("Digite uma das opções desejadas:\n1 - Adicionar\n2 - Remover\n3 - Exibir\n9 - Sair\nEscolha Aqui>>>> ")
# print("Saindo .....")


#################################################################################################################
#  Crie um jogo de quiz com perguntas e respostas, onde o jogador acumula pontos ao acertar as respostas.
# Exemplo de Saída:
# Qual é a capital do Brasil?
# Sua resposta: Br
# Resposta incorreta.
# Quem escreveu 'Dom Quixote'?
# Sua resposta: n sei
# Resposta incorreta.
# Quanto é 2 + 2?
# Sua resposta: 4
# Resposta correta!
# Você fez 1 pontos.
