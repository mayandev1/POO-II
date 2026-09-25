VOGAIS = "aeiouAEIOU"

with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

vogais_encontradas = [caractere for caractere in conteudo if caractere in VOGAIS]

with open("vogais.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("".join(vogais_encontradas))

print("Vogais extraídas e salvas em 'vogais.txt'.")
