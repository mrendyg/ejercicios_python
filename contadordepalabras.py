''' 
Ejercicio 3: Contador de palabras
Escribe un programa que tome una cadena de texto como 
entrada y cuente el número de palabras en ella. Puedes asumir que las palabras están separadas por espacios.
'''


mitexto = input("Ingrese un texto:\n")
palabras = mitexto.split()
j = 0

for i in palabras:
    i = i.strip('.,!?()[]{}"\'')
    i = i.lower()
    j += 1
print(j)