import random

chars = "ABCDEFGHIJKLMNOPQRSTVWXYZabcdefghijklmnopqrstuvwxyz1234567890,.-;:_{[]}´+*?¡'¿"

password = ""

for i in range(20):
    password += random.choice(chars)

print(f"Your password is: {password}")