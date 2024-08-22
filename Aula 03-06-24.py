# def funcao ():
#     print("testando")

# funcao()
########################################################################################################################################################################################
# def area (base,altura):
#     area = base * altura
#     biscoito = 1
#     return area,biscoito
    

# base = float (input ("Digite a Base:"))
# altura = float (input ("Digite a Altura:"))
# result,bis = area(base,altura)

# print (result , "and" , bis)
########################################################################################################################################################################################
# def func(parametro):
#     while parametro > 0:
#         print ("Teste")
#         parametro -= 1
# func(10)
########################################################################################################################################################################################
# def ex1 (arg1,arg2,arg3):
#     print(f"Os valores digitados são: primeiro:{arg1}, segundo:{arg2}, tereceiro{arg3}")
# arg1 = input("Digite o primeiro valor:")
# arg2 = input("Digite o segundo valor:")
# arg3 = input("Digite o terceiro valor:")
# ex1 (arg1,arg2,arg3)
########################################################################################################################################################################################
# Hipotenusa de um Triângulo Retângulo:
# Crie um programa que recebe os dois lados menores de um triângulo retângulo e uma 
# função retorna o valor da hipotenusa.
# def hipotenusa (lado1,lado2):
#     result = (lado1*lado1)+(lado2*lado2) 
#     result = result**0.5
#     print(f"O valor da hipotenusa é: {result}  ")
# lado1 = float (input ("Digite o primeiro lado: "))
# lado2 = float (input ("Digite o segundo lado: "))
# hipotenusa (lado1,lado2)
# ########################################################################################################################################################################################
# Existência de um Triângulo:
# Crie um programa que recebe os três lados de um triângulo e passa esses valores para uma 
# função que verifica se esse triângulo existe ou não. Para que um triângulo exista, cada lado 
# deve ser maior que o módulo da subtração dos outros dois lados e menor que a soma dos 
# outros dois lados.
# def triangulo(a, b, c):
#     if (a - b < c < a + b) and (a - c < b < a + c) and (b - c < a < b + c):
#         print("O triângulo existe.")
#     else:
#         print("O triângulo não existe.")
# lado1 = float(input("Digite o lado 1: "))
# lado2 = float(input("Digite o lado 2: "))
# lado3 = float(input("Digite o lado 3: "))
# triangulo(lado1, lado2, lado3)
    


# def verifica_triangulo(a, b, c):
#     if (a + b > c) and (a + c > b) and (b + c > a):
#         print("Os lados formam um triângulo.")
#     else:
#         print("Os lados não formam um triângulo.")

# lado1 = float(input("Digite o lado 1: "))
# lado2 = float(input("Digite o lado 2: "))
# lado3 = float(input("Digite o lado 3: "))

# if lado1 > 0 and lado2 > 0 and lado3 > 0:  
#     verifica_triangulo(lado1, lado2, lado3)
# else:
#     print("Digite valores válidos!")



########################################################################################################################################################################################
# Faça um programa que peça um número inteiro positivo ‘n’ ao usuário e imprima um 
# quadrado de lado ‘n’ preenchido com hashtags. Por exemplo, para n=4, o resultado seria:
# def imprime (numero):
#     limit = numero
#     i = 0
#     while i <= limit:
#         print(limit*"#")
#         i +=1
# numero = int (input("Digite o numero: "))
# imprime (numero)
########################################################################################################################################################################################
# Maior e Menor Número:
# Programe um software que recebe três números e cria duas funções: uma que retorna o 
# 1
# maior número e outra que retorna o menor número.
# def maior (num1,num2,num3):
#     if num1>num2 and num1>num3:
#         print (f"O primeiro numero: {num1} é o maior numero!")
#     elif num2>num1 and num2>num3:
#         print (f"O segundo numero: {num2} é o maior numero!")
#     else:
#         print (f"O terceiro numero: {num3} é o maior numero!")

# def menor(num1,num2,num3):
#     if num1<num2 and num1<num3:
#         print (f"O primeiro numero: {num1} é o menor numero!")
#     elif num2<num1 and num2<num3:
#         print (f"O segundo numero: {num2} é o menor numero!")
#     else:
#         print (f"O terceiro numero: {num3} é o menor numero!")    

# num1 = input("Digite o numero 1: ")
# num2 = input("Digite o numero 2: ")
# num3 = input("Digite o numero 3: ")

# maior(num1,num2,num3)
# menor(num1,num2,num3)
########################################################################################################################################################################################
# Número Perfeito:
# Um número é dito ser perfeito quando ele é igual à soma de seus divisores. Por exemplo, o 
# seis é perfeito, pois: 6=1+2+3
# Crie um programa que pede um número ao usuário e diga se ele é perfeito ou não
# def perfeito(numero):
#     soma = 0
#     for i in range(1, numero):
#         if numero % i == 0:
#             soma += i
#     return soma == numero
# numero = int(input("Digite um número: "))
# if perfeito(numero):
#     print(f"{numero} é um número perfeito.")
# else:
#     print(f"{numero} não é um número perfeito.")

########################################################################################################################################################################################
# Número Invertido:
# Crie um software que recebe um número do usuário, passa esse valor para uma função e ela 
# retorna o número escrito ao inverso. Por exemplo, se o usuário der o valor 1234, a função 
# deve retornar 4321. Dica: primeiro, crie uma função que conta quantos dígitos tem um 
# número.
# def invertido(numero):
#     invertendo = []
#     while numero > 0:
#         digit = numero % 10
#         invertendo.append(digit)
#         numero //= 10
#     print(invertendo)

# numero = int(input("Digite um número: "))
# invertido(numero)
# def contar(numero):
#     count = 0
#     while numero > 0:
#         count += 1
#         numero //= 10
#     return count
# def inverção(numero):
#     inverted = 0
#     while numero > 0:
#         digit = numero % 10
#         inverted = inverted * 10 + digit
#         numero //= 10
#     return inverted
# numero = int(input("Digite um número: "))
# inverted_number = inverção(numero)
# print("O número invertido é:", inverted_number)
# ***************************************************************************************************************************************************************************************
# lista = []
# nome = input("teste >>>")
# for i in nome:
#     lista.append(i)
# print (lista)
# lista.reverse()
# print (lista)
########################################################################################################################################################################################
# Lançamento de Moedas:
# Faça um programa para lançar uma moeda. Quando chamamos uma função, ela deve 
# retornar “cara” ou “coroa”. Em outra função, faça ‘n’ lançamentos de moedas (onde ‘n’ é o 
# valor que o usuário quiser) e mostre a porcentagem de vezes que deu cara e coroa. O que 
# tende a acontecer se você jogar a moeda 10, 100, 1000 ou um milhão de vezes?
# import random
# def lancar_moeda():
#     if random.randint(0, 1) == 0:
#         return "cara"
#     else:
#         return "coroa"
# def lancamentos_moedas(n):
#     caras = 0
#     coroas = 0
#     for _ in range(n):
#         resultado = lancar_moeda()
#         if resultado == "cara":
#             caras += 1
#         else:
#             coroas += 1
#     porcentagem_cara = (caras / n) * 100
#     porcentagem_coroa = (coroas / n) * 100
#     print(f"Porcentagem de caras: {porcentagem_cara}%")
#     print(f"Porcentagem de coroas: {porcentagem_coroa}%")
# lancamentos = int(input("Quantas vezes deseja lançar a moeda? "))
# lancamentos_moedas(lancamentos)
########################################################################################################################################################################################
# Dado Aleatório:
# Crie um dado em C++. A função deve sortear um número aleatório de 1 até 6. Agora, faça 
# com que o dado seja lançado 100 vezes, mil vezes e 1 milhão de vezes. Armazene o valor 
# que ele forneceu em cada lançamento e mostre quantas vezes cada número foi sorteado. 
# Compare os resultados com a estatística.
# import random
# def sortear(vezes):
#     for i in range(vezes):
#         result = random.randint(1, 6)
#         print(result)
# sortear(100)
# def sortear(vezes):
#     if vezes == 100:
#         resultados = [0, 0, 0, 0, 0, 0] 
#         for i in range(vezes):
#             result = random.randint(1, 6)
#             resultados[result - 1] += 1 
#         print(f"Resultados após 100 lançamentos: O numero 1 foi sorteado {resultados[0]}, O numero 2 foi sorteado {resultados[1]}, O numero 3 foi sorteado {resultados[2]}, O numero 4 foi sorteado {resultados[3]}, O numero 5 foi sorteado {resultados[4]}, O numero 6 foi sorteado {resultados[5]}")
#     elif vezes == 1000:
#         resultados = [0, 0, 0, 0, 0, 0] 
#         for i in range(vezes):
#             result = random.randint(1, 6)
#             resultados[result - 1] += 1 
#         print(f"Resultados após 1000 lançamentos: O numero 1 foi sorteado {resultados[0]}, O numero 2 foi sorteado {resultados[1]}, O numero 3 foi sorteado {resultados[2]}, O numero 4 foi sorteado {resultados[3]}, O numero 5 foi sorteado {resultados[4]}, O numero 6 foi sorteado {resultados[5]}")
#     elif vezes == 1000000:
#         resultados = [0, 0, 0, 0, 0, 0] 
#         for i in range(vezes):
#             result = random.randint(1, 6)
#             resultados[result - 1] += 1 
#         print(f"Resultados após 1000000 lançamentos: O numero 1 foi sorteado {resultados[0]}, O numero 2 foi sorteado {resultados[1]}, O numero 3 foi sorteado {resultados[2]}, O numero 4 foi sorteado {resultados[3]}, O numero 5 foi sorteado {resultados[4]}, O numero 6 foi sorteado {resultados[5]}")    
# sortear(100)
# sortear(1000)
# sortear(1000000)
########################################################################################################################################################################################
# Jogo de Par ou Ímpar:
# Escolha 0 para par ou 1 para ímpar. Em seguida, forneça um número. Crie um programa que 
# determine se a soma do número escolhido com um número aleatório é par ou ímpar.
# def soma (numero):
#     aleatorio = random.randint(0,1)
#     somando = numero + aleatorio
#     if somando % 2 == 0:
#         print(f"O numero aleatorio é {aleatorio}")
#         print("A soma é par!!!!")
#     else:
#         print(f"O numero aleatorio é {aleatorio}")
#         print("A soma é impar!!!!")
# numero = int(input("Digite um número: "))
# soma(numero)
########################################################################################################################################################################################
# Crie um programa que recebe um número inteiro positivo ‘n’ e calcula o fatorial desse 
# número. O fatorial de ‘n’ é o produto de todos os números inteiros positivos de 1 até ‘n’. 
# Por exemplo, 5!=5⋅4⋅3⋅2⋅1=120
# def fatorial (numero):
#     result = 1
#     for i in range (1, numero + 1):
#         result =  i*result
#     print(f"O resultado é: {result}")
# numero = int(input("Digite um número: "))
# if numero > 0:
#     fatorial(numero)
# else: 
#     print("Digite um numero valido!!!!")
########################################################################################################################################################################################
# Escreva uma função que recebe um número inteiro e retorna a soma de seus dígitos. Por 
# exemplo, se o número for 123, a função deve retornar 6 (1 + 2 + 3).
# def soma_digito(numero):
#     soma = 0
#     for i in str (numero):
#         soma += int (i)
#     print(f"A soma dos dígitos de {numero} é {soma}")

# numero = int(input ("Digite o numero: "))
# soma_digito(numero)
########################################################################################################################################################################################










