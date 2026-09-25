with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

linhas_nao_vazias = [linha for linha in linhas if linha.strip() != ""]

with open("limpo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(linhas_nao_vazias)

print("Linhas vazias removidas. Resultado salvo em 'limpo.txt'.")
