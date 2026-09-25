import os

if os.path.exists("exemplo.txt"):
    print("O arquivo 'exemplo.txt' existe.")
    with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
else:
    print("O arquivo 'exemplo.txt' não existe.")
