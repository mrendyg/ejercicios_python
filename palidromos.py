def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    rev = texto[::-1]
    return rev == texto

if __name__ == '__main__':
    print("Escribe un texto")
    texto = input()

    if es_palindromo(texto):
        print("¡Enhorabuena, tu texto es un palíndromo!")
    else:
        print("Tu texto no es un palíndromo.")
