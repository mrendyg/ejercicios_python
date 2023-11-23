#Imprime numeros primos hasta el 100

for i in range(2, 100):
    es_primo=True
    for j in range(2, i):
        if i % j == 0:
            es_primo=False
            break        
    if es_primo:
        print(i, "es primo")


