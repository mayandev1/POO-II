with open("numeros.txt", "w", encoding="utf-8") as arquivo:
    for numero in range(1, 11):
        arquivo.write(f"{numero}\n")

print("Arquivo 'numeros.txt' criado com sucesso.")
