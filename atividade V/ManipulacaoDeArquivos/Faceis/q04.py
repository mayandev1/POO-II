with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

print(f"Número total de linhas: {len(linhas)}")
