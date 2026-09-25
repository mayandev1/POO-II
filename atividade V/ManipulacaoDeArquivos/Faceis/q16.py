"""
16. Encontre e imprima a linha mais longa (em caracteres) do arquivo
    "exemplo.txt".
"""

with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

linha_mais_longa = max(linhas, key=len)
print(f"Linha mais longa ({len(linha_mais_longa.rstrip())} caracteres):")
print(linha_mais_longa.strip())
