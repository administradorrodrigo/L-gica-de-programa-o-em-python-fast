# def somar(a,b):
#     return(a+b)

# resultado = somar(2,4)
# print(resultado)


def calcular(operacao, numerador, denominador):
    if operacao == "somar":
        return numerador + denominador
    elif operacao == "subtrair":
        return numerador - denominador    
    elif operacao == "multiplicar":
        return numerador * denominador
    elif operacao == "dividir":        
        if denominador !=0:
            return numerador / denominador
    else:
        print("operação inválida")

#print(calcular("multiplicar",2,3))
controlador= 0
while True:
    controlador= int(input("1 Somar, 2 - Subtrair, 3- Multiplicar, 4 - Dividir, 5 - Sair "))
    if controlador < 0 or controlador >5:
        print("opção inexistente, escolha novamente")
        input("escoha qq tecla pra continuar")         
        continue
    if controlador == 5:
        break
    numerador = float(input("digite o primeiro numero"))
    denominador = float(input("digite o segundo numero"))
    if controlador == 1:
        print(calcular("somar", numerador, denominador))
    elif controlador == 1:
        print(calcular("subtrair", numerador, denominador))
    elif controlador == 1:
        print(calcular("multiplicar", numerador, denominador))
    elif controlador == 1:
        print(calcular("dividir", numerador, denominador))
    


    

    




