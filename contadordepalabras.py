mitexto = input("Ingrese un texto:\n")
palabras = mitexto.split()
j = 0

for i in palabras:
    i = i.strip('.,!?()[]{}"\'')
    i = i.lower()
    j += 1
print(j)