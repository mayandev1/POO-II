with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

conteudo_substituido = conteudo.replace("Python", "Java")

with open("exemplo_substituido.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_substituido)

print("Substituição realizada. Resultado salvo em 'exemplo_substituido.txt'.")
