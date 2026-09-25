with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

palavras = conteudo.split()
print(f"Número total de palavras: {len(palavras)}")
