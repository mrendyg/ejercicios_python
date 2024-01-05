#Ejercicio 5: Factorial
#Escribe un programa que calcule el factorial de un número ingresado por el usuario.

acumulador = 1

numero_ingresado = int(input("Ingresa un numero:\n"))

for i in range (1, numero_ingresado+1):
    acumulador = acumulador * i
 
print("El factorial de", numero_ingresado, "es:\n", acumulador)