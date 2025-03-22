import os
import math


valor1 = int(input("Coloque o primeiro número: "))
operação = input("Escolha a operação: ")
valor2 = int(input("Coloque o segundo número: "))


try:
    if operação == "+":
        print(valor1 + valor2)

    elif operação == "-":
        print(valor1 - valor2)

    elif operação =="*":
        print(valor1 * valor2)

    elif operação == "/":
        print(valor1 / valor2)

    elif operação != ["/", "+", "-", "*"]:
        print("Selecione uma operação valida: ")

except ZeroDivisionError:
    print("Não é possível dividir por zero")