def conta_as(texto):
    return texto.lower().count('a')

texto = input("Digite um texto: ")
print(f"A letra 'a' aparece {conta_as(texto)} vezes no texto.")