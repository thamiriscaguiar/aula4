import random

def sorteio():
    numeros = [random.randint(1, 10) for _ in range(50)]  # 50 sorteios entre 1 e 10
    return numeros

def contar_ocorrencias(numeros, numero):
    return numeros.count(numero)

numeros_sorteados = sorteio()

numero_usuario = int(input("Escolha um número entre 1 e 10: "))

ocorrencias = contar_ocorrencias(numeros_sorteados, numero_usuario)

print(f"O número {numero_usuario} apareceu {ocorrencias} vezes nos sorteios.")
