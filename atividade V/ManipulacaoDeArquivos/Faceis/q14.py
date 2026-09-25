with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

linhas_invertidas = linhas[::-1]

with open("invertido.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(linhas_invertidas)

print("Linhas invertidas e salvas em 'invertido.txt'.")
