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
# Crie um programa que converte uma temperatura em graus Celsius para Fahrenheit. A 
# fórmula de conversão é: F=59C+32
# def conversor(grau):
#     convertido = (grau * 9.0 / 5.0) + 32.0
#     print(f"{grau} graus Celsius é igual a {convertido} graus Fahrenheit")
# grau = float(input("Digite a temperatura em graus Celsius: "))
# conversor(grau)
########################################################################################################################################################################################
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


