with open("entrada.txt", "r", encoding="utf-8") as arquivo_entrada:
    conteudo = arquivo_entrada.read()

with open("copia.txt", "w", encoding="utf-8") as arquivo_copia:
    arquivo_copia.write(conteudo)

print("Conteúdo copiado para 'copia.txt' com sucesso.")
