with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

quantidade = conteudo.lower().count("a")
print(f"A letra 'a' aparece {quantidade} vezes no arquivo.")
