with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

linhas_ordenadas = sorted(linhas)

with open("ordenado.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(linhas_ordenadas)

print("Linhas ordenadas e salvas em 'ordenado.txt'.")
