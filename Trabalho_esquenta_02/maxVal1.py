'''
    Autor: Iago Magalhães
'''

import time
import os, psutil
import pandas as pd
import functions as fct

process = psutil.Process()

caminhoNOrdenados = '../Trabalho_esquenta_01/Nao_ordenados/Nao_ordenados/'
numeroProcurado = 0
posicao = -1
media = []
memoria = []

#-----------------------------------------------
# INICIANDO ÁNALISE DO ALGORITMO
arquivosNOrdenadosLidos = fct.listFiles(caminhoNOrdenados)

def maxVal(A, n):
    max = A[0]
    for i in range(n):
        if(A[i] > max):
            max = A[i]
    return max

for arq in arquivosNOrdenadosLidos:
    print('Arquivo lido {}'.format(arq))
    if(
        arq == '../Trabalho_esquenta_01/Nao_ordenados/Nao_ordenados/1000000.txt'
        or arq == '../Trabalho_esquenta_01/Nao_ordenados/Nao_ordenados/5000000.txt'
        or arq == '../Trabalho_esquenta_01/Nao_ordenados/Nao_ordenados/10000000.txt'
        or arq == '../Trabalho_esquenta_01/Nao_ordenados/Nao_ordenados/100000000.txt'
    ):
        pass
    else:
        try:
            vet = fct.carregaArquivo(arq)
            # print(len(vet[0]))
            mediaTempo = 0
            for i in range(0,10):
                inicio = time.time()
                maximo = maxVal(vet[0], len(vet[0]))
                # print(maximo)
                fim = time.time()
                memoria.append(fct.memoryUse())
                tempo = fim - inicio
                tempo = float(tempo)
                mediaTempo = mediaTempo + tempo

            media.append(mediaTempo / 10)
        except:
            print('Erro de memória')


# FINAL DA ÁNALISE DO ALGORITMO
#-----------------------------------------------

print('Ánalise dos resultados')
print('Média de tempo: {}'.format(media))
print('Consumo de memória: {}'.format(memoria))

"""
[0.0, 0.0002499818801879883, 0.004066729545593261, 0.006930685043334961, 0.0, 0.00015957355499267577, 0.000507354736328125, 0.003972244262695312, 0.043287229537963864]
[54640640, 54640640, 54640640, 54640640, 54640640, 54640640, 54640640, 54640640, 54640640, 54640640, 54775808, 54775808, 54775808, 54775808, 54775808, 54775808, 54775808, 54775808, 54775808, 54775808, 56139776, 56139776, 56139776, 56139776, 56139776, 56139776, 56139776, 56139776, 56139776, 56139776, 63889408, 63889408, 63889408, 63889408, 63889408, 63889408, 63889408, 63889408, 63889408, 63889408, 58413056, 58413056, 58413056, 58413056, 58413056, 58413056, 58413056, 58413056, 58413056, 58413056, 57376768, 57376768, 57376768, 57376768, 57376768, 57376768, 57376768, 57376768, 57376768, 57376768, 57389056, 57389056, 57389056, 57389056, 57389056, 57389056, 57389056, 57389056, 57389056, 57389056, 59904000, 59904000, 59904000, 59904000, 59904000, 59904000, 59904000, 59904000, 59904000, 59904000, 79704064, 79704064, 79704064, 79704064, 79704064, 79704064, 79704064, 79704064, 79704064, 79704064]
"""