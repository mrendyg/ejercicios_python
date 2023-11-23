'''
Ejercicio 2: Verificación de número primo
Escribe un programa que verifique si un número ingresado por el usuario es primo o no.
'''

for i in range(2, 100):
    es_primo=True
    for j in range(2, i):
        if i % j == 0:
            es_primo=False
            break        
    if es_primo:
        print(i, "es primo")


