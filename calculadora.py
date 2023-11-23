'''
Ejercicio 4: Calculadora simple
Crea una calculadora que pueda realizar operaciones básicas como suma, resta, multiplicación y división. 
El programa debe tomar como entrada dos números y la operación a realizar.
'''

def suma(num1, num2):
    suma = num1 + num2
    return suma

def resta(num1, num2):
    resta = num1 - num2
    return resta

def multiplicar(num1, num2):
    multiplicar = num1 * num2
    return multiplicar

def dividir(num1, num2):
    dividir = num1/num2
    return dividir

funcion = int(input("¿Que operacion deseas realizar?\n (1)suma, (2)resta, (3)multiplicacion, (4)Division\n"))

numero1 = int(input("Inserta un numero:\n"))
numero2 = int(input("Inserta un segundo numero:\n"))

if funcion == 1:
    resultado = suma(numero1, numero2)
    print("El resultado es: ", resultado)
elif funcion == 2:
    resultado = resta(numero1, numero2)
    print("El resultado es: ", resultado)
elif funcion == 3:
    resultado = multiplicar(numero1, numero2)
    print("El resultado es: ", resultado)
elif funcion == 4:
    resultado = dividir(numero1, numero2)
    print("El resultado es: ", resultado)
else:
    print("Lo siento no puedo ayudarte")
