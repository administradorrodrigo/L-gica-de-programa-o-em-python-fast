# def calcular(operacao, numerador, denominador):
#     if operacao == "somar":
#         return numerador + denominador
#     elif operacao == "subtrair":
#         return numerador - denominador    
#     elif operacao == "multiplicar":
#         return numerador * denominador
#     elif operacao == "dividir":        
#         if denominador !=0:
#             return numerador / denominador
#     else:
#         print("operação inválida")

# #print(calcular("multiplicar",2,3))
# controlador= 0
# while True:
#     controlador= int(input("1 Somar, 2 - Subtrair, 3- Multiplicar, 4 - Dividir, 5 - Sair "))
#     if controlador < 0 or controlador >5:
#         print("opção inexistente, escolha novamente")
#         input("escoha qq tecla pra continuar")         
#         continue
#     if controlador == 5:
#         break
#     numerador = float(input("digite o primeiro numero"))
#     denominador = float(input("digite o segundo numero"))
#     if controlador == 1:
#         print(calcular("somar", numerador, denominador))
#     elif controlador == 1:
#         print(calcular("subtrair", numerador, denominador))
#     elif controlador == 1:
#         print(calcular("multiplicar", numerador, denominador))
#     elif controlador == 1:
#         print(calcular("dividir", numerador, denominador))

# def par_impar(x):
#     if x %2==0:
#         print("PAR")
#     else:
#         print("IMPAR")
# par_impar(10)

# def multi_3(y):
#     if y %3==0:
#         print("multiplo")
#     else:
#         print("não é multiplo")
# multi_3(17)

# Exercício: Conversor de Temperatura
# O objetivo é criar uma função que converta uma temperatura de graus Celsius para graus Fahrenheit.
# A fórmula para a conversão é: F=C *  9/5 +32 # Onde C é a temperatura em Celsius e F é a temperatura em Fahrenheit.
# Sua tarefa é criar uma função em Python chamada celsius_para_fahrenheit que: # Receba um único argumento: celsius (float).
# Calcule a temperatura equivalente em Fahrenheit usando a fórmula fornecida.
# Retorne o valor da temperatura em Fahrenheit.
# Depois de definir a função, você pode testá-la com alguns valores, como 0, 25 e 100 graus Celsius, para verificar se o resultado está correto.
# Tente escrever o código por conta própria. Se precisar de ajuda, estou aqui para orientá-lo!

# def c_f(y):
#    y = y * (9 / 5) + 32
#    print(f'{y} Fahrenheit')
# c_f(0)

#O objetivo é criar uma função que conte o número de vogais em uma string (cadeia de caracteres) fornecida. Para este exercício, considere as vogais como 'a', 'e', 'i', 'o', 'u', tanto em minúsculas quanto em maiúsculas.

# def cont_vog(x):
#     y = "aeiou".upper()
#     contador = 0
#     for z in x:
#         if z.upper() in y:
#             contador+=1              
    
#     print(contador)

# cont_vog("rodrigo")

# O objetivo é criar uma função que determine se um número inteiro é um número primo. 
# Um número primo é um número natural maior que 1 que não pode ser formado pela multiplicação de dois números naturais menores.

def nu_primo(x)
    if x %3 == 0 or
