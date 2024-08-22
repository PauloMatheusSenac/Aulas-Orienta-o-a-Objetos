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
#Fatorial:
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
#Soma dos Dígitos:
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
#Média Aritmética:
# Crie um programa que pede ao usuário para digitar uma sequência de números e, em 
# seguida, calcula a média aritmética desses números.
# def media (numeros):
#     elemen = 0
#     for i in numeros:
#         elemen +=1
#     med = sum(numeros) / elemen
#     print(f"A media total é: {med}")

# numeros = []
# escolha = int (input("Digite a opção. 1 para digitar um numero para o calculo ou 2 para fazer a media com os digitados\nEscolha>>>") )
# while escolha == 1:
#     numero = int(input ("Digite o numero: "))
#     numeros.append(numero)
#     escolha = int (input("Digite a opção. 1 para digitar um numero para o calculo ou 2 para fazer a media com os digitados\nEscolha>>>") )
# else:
#     print(f"Os numero que serão calculados são: {numeros}")
# media(numeros)
########################################################################################################################################################################################
#Verificação de Palíndromo:
# Faça um programa que verifica se uma palavra ou frase é um palíndromo. Um palíndromo é 
# uma palavra ou frase que se lê da mesma forma de trás para frente. Por exemplo, “arara” é 
# um palíndromo.
# import string
# def palindromo (palavra):
#     if palavra == palavra[::-1]:
#         print("A palavra é um palíndromo")
#     else:
#         print("A palavra não é um palíndromo")
# palavra = input ("Digite a palavra: ")
# palindromo(palavra)
########################################################################################################################################################################################
# ****************************************************************************************************************************************************************************************
# def palindromo(palavra):
#     n = len(palavra)
#     for i in range(n // 2):
#         if palavra[i] != palavra[n - i - 1]:
#             print("A palavra não é um palíndromo")
#             return
#     print("A palavra é um palíndromo")

# palavra = input("Digite a palavra ou frase: ")
# palindromo(palavra)
########################################################################################################################################################################################
#Contagem de Vogais:
# Escreva uma função que recebe uma string e conta quantas vogais (a, e, i, o, u) ela contém.
# def vogal (palavra):
#     encontradas = []
#     vogais = ["a","e","i","o","u","A","E","I","O","U"]
#     for i in palavra:
#         if i in vogais:
#             encontradas.append(i)
#     print(f"A vogais encontradas foram: {encontradas}")
# palavra = input("Digite a palavra ou frase: ")
# vogal(palavra)
########################################################################################################################################################################################
# Conversão de Temperatura:
#  Crie um programa que converte uma temperatura em graus Celsius para Fahrenheit. A 
# fórmula de conversão é: F=59C+32
# def conversor(grau):
#     convertido = (grau * 9.0 / 5.0) + 32.0
#     print(f"{grau} graus Celsius é igual a {convertido} graus Fahrenheit")
# grau = float(input("Digite a temperatura em graus Celsius: "))
# conversor(grau)
########################################################################################################################################################################################
# Números Primos:
# Faça um programa que verifica se um número é primo. Um número é primo se ele não 
# possui divisores além de 1 e ele mesmo.
# def primos (numero):
#     cont = 0
#     for i in range (1,numero):
#         if numero % i == 0:
#             cont += 1
#     if cont > 2:
#         print(f"O numero {numero}, não é primo!!!")
#     else:
#         print(f"O numero {numero}, é primo!!!")
# numero = int(input ("Digite o numero: "))
# primos (numero)
########################################################################################################################################################################################
# Soma dos Números Pares:
# Escreva uma função que recebe um número inteiro positivo ‘n’ e retorna a soma de todos 
# os números pares de 1 até ‘n
# def soma_pares (numero):
#     soma = 0
#     for i in range (1,numero + 1) :
#         if i % 2 == 0:
#             soma += i
#     print(f"A soma dos pares de 1 até {numero} é: {soma}")
# numero = int(input ("Digite o numero: "))
# soma_pares (numero)
########################################################################################################################################################################################
# Sequência de Fibonacci:
# Crie um programa que gera os primeiros ‘n’ números da sequência de Fibonacci. A 
# sequência começa com 0 e 1, e cada número subsequente é a soma dos dois anteriores.
# def fibo(n):
#     fib_seq = [0, 1]
#     while len(fib_seq) < n:
#         seq = fib_seq[-1] + fib_seq[-2]
#         fib_seq.append(seq)
#     print(f"Sequência de Fibonacci: {fib_seq}")
# n = int(input("Digite o número da sequancia que deseja gerar: "))
# fibo(n)
########################################################################################################################################################################################
# Cálculo de Juros Compostos:
# Faça um programa que calcula o montante final de um investimento com juros compostos. 
# O usuário deve fornecer o capital inicial, a taxa de juros anual e o período de investimento 
# em anos.

# def montante(capital, taxa, periodo):
#     mont = capital * (1 + taxa) ** periodo
#     print(f"O montante é: {mont:.2f}")

# capital = float(input("Digite o valor inicial: "))
# taxa = float(input("Digite a taxa de juros anual (em decimal, por exemplo, 0.05 para 5%): "))
# periodo = int(input("Digite o período de investimento (em anos): "))
# montante(capital, taxa, periodo)
########################################################################################################################################################################################
# Validação de CPF:
# Implemente um programa que verifica se um número de CPF é válido. O CPF é composto 
# por 11 dígitos e possui um algoritmo de validação específico
# def calcular_digito_verificador(cpf, peso_inicial):
#     soma = 0
#     for i, digit in enumerate(cpf):
#         soma += int(digit) * (peso_inicial - i)
#     resto = soma % 11
#     digito = 11 - resto
#     return digito if digito < 10 else 0
# def validar_cpf(cpf):
#     cpf = ''.join(filter(str.isdigit, cpf))
#     if len(cpf) != 11:
#         return False
#     if cpf == cpf[0] * 11:
#         return False
#     digito1 = calcular_digito_verificador(cpf[:9], 10)
#     digito2 = calcular_digito_verificador(cpf[:9] + str(digito1), 11)
#     return cpf[-2:] == f"{digito1}{digito2}"
# cpf = input("Digite o número do CPF (formato XXX.XXX.XXX-YY): ")
# if validar_cpf(cpf):
#     print("O CPF é válido.")
# else:
#     print("O CPF é inválido.")
########################################################################################################################################################################################
# Conversão de Bases Numéricas:
# Crie um programa que converte um número decimal para binário, octal ou hexadecimal, 
# conforme a escolha do usuário.
# def decimal_binario(decimal_num):
#     return bin(decimal_num)[2:]

# def decimal_octal(decimal_num):
#     return oct(decimal_num)[2:]

# def decimal_hexa(decimal_num):
#     return hex(decimal_num)[2:].upper()


# decimal_num = int(input("Digite um número decimal: "))
# print("\nEscolha a base para conversão:")
# print("1 - Binário")
# print("2 - Octal")
# print("3 - Hexadecimal")
# escolha = int(input("Digite sua escolha (1/2/3): "))

# if escolha == 1:
#     result = decimal_binario(decimal_num)
#     print(f"\nO número decimal {decimal_num} em binário é: {result}")
# elif escolha == 2:
#     result = decimal_octal(decimal_num)
#     print(f"\nO número decimal {decimal_num} em octal é: {result}")
# elif escolha == 3:
#     result = decimal_hexa(decimal_num)
#     print(f"\nO número decimal {decimal_num} em hexadecimal é: {result}")
# else:
#     print("\nEscolha inválida. Por favor, escolha 1, 2 ou 3.")
########################################################################################################################################################################################
#Cálculo de Média Ponderada:
# def calcular_media(notas, pesos):
#     if len(notas) != len(pesos):
#         raise ValueError("As listas de notas e pesos devem ter o mesmo tamanho")
#     soma_notas = sum(notas[i] * pesos[i] for i in range(len(notas)))
#     soma_pesos = sum(pesos)
#     if soma_pesos == 0:
#         raise ValueError("A soma dos pesos não pode ser zero")
#     media_ponderada = soma_notas / soma_pesos
#     return media_ponderada
# num_disciplinas = int(input("Digite o número de disciplinas: "))
# notas = []
# pesos = []
# for i in range(num_disciplinas):
#     nota = float(input(f"Digite a nota da disciplina {i+1}: "))
#     peso = float(input(f"Digite o peso da disciplina {i+1}: "))
#     notas.append(nota)
#     pesos.append(peso)
# try:
#     media = calcular_media(notas, pesos)
#     print(f"\nA média ponderada das disciplinas é: {media:.2f}")
# except ValueError as ve:
#     print(f"\nErro ao calcular a média ponderada: {ve}")
########################################################################################################################################################################################
#Ordenação de Números:
# Implemente um algoritmo de ordenação (por exemplo, Bubble Sort, Selection Sort ou Quick 
# Sort) para ordenar um vetor de números inteiros.
# def bolha(arr):
#     n = len(arr)
#     for i in range(n):
#         # Flag para verificar se houve troca durante a passagem atual
#         swapped = False
#         # Últimos i elementos já estão no lugar correto
#         for j in range(0, n-i-1):
#             # Compara o elemento atual com o próximo
#             if arr[j] > arr[j+1]:
#                 # Troca os elementos
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 # Marca que houve troca
#                 swapped = True
#         if not swapped:
#             break
# vetor = [64, 34, 25, 12, 22, 11, 90]
# print("Vetor original:")
# print(vetor)
# bolha(vetor)
# print("\nVetor ordenado:")
# print(vetor)
########################################################################################################################################################################################
# Cálculo de Potência:
# Crie uma função que recebe a base e o expoente e calcula a potência. Por exemplo, 23=8
# def potencia(base, expoente):
#     return base ** expoente
# base = int(input("Digite a base da potência: "))
# expoente = int(input("Digite o expoente da potência: "))
# resultado = potencia(base, expoente)
# print(f"\n{base}^{expoente} = {resultado}")
########################################################################################################################################################################################
# Contagem de Caracteres:
# Escreva um programa que conta quantos caracteres (incluindo espaços) há em uma string.
# def contar_caracteres(string):
#     return len(string)
# texto = input("Digite uma string para contar os caracteres: ")
# total_caracteres = contar_caracteres(texto)
# print(f"\nA string '{texto}' possui {total_caracteres} caracteres (incluindo espaços).")
########################################################################################################################################################################################
#Cálculo de Média Harmônica:
#Calcule a média harmônica de um conjunto de números. A fórmula é: H=x11+x21+…+xn1n
# def calcular_media_harmonica(numeros):
#     soma_inversos = sum(1 / num for num in numeros if num != 0)
#     media_harmonica = len(numeros) / soma_inversos
#     return media_harmonica
# numeros = [2, 4, 5, 8, 10]
# media_harmonica = calcular_media_harmonica(numeros)
# print(f"A média harmônica dos números {numeros} é: {media_harmonica:.2f}")
########################################################################################################################################################################################
#Verificação de Anagramas:
# Faça um programa que verifica se duas palavras são anagramas (ou seja, possuem as 
# mesmas letras, mas em ordem diferente).
# def sao_anagramas(palavra1, palavra2):
#     palavra1 = palavra1.lower()
#     palavra2 = palavra2.lower()
    
#     palavra1_sorted = sorted(palavra1)
#     palavra2_sorted = sorted(palavra2)
    
#     if palavra1_sorted == palavra2_sorted:
#         return True
#     else:
#         return False
# palavra1 = input("Digite a primeira palavra: ")
# palavra2 = input("Digite a segunda palavra: ")

# if sao_anagramas(palavra1, palavra2):
#     print(f"\n'{palavra1}' e '{palavra2}' são anagramas.")
# else:
#     print(f"\n'{palavra1}' e '{palavra2}' não são anagramas.")
########################################################################################################################################################################################
# Conversão de Horas para Minutos:
# Escreva uma função que recebe um valor em horas e retorna o equivalente em minutos.
# def horas_para_minutos(horas):
#     minutos = horas * 60
#     return minutos
# horas = float(input("Digite um valor em horas: "))
# minutos = horas_para_minutos(horas)
# print(f"\n{horas} horas equivalem a {minutos} minutos.")
########################################################################################################################################################################################




















