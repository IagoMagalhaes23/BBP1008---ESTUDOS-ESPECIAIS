'''
    Autor: Iago Magalhães
'''

import time
import os, psutil
import pandas as pd
import functions as fct

process = psutil.Process()

caminhoNOrdenados = '../Trabalho_esquenta_01/Nao_ordenados/Nao_ordenados/'
media = []
memoria = []

#-----------------------------------------------
# INICIANDO ÁNALISE DO ALGORITMO
arquivosNOrdenadosLidos = fct.listFiles(caminhoNOrdenados)

def maxVal(A, init, end):
    print(len(A))
    print(init)
    print(end)
    if((end - init) <= 1):
        return max(A[init], A[end])
    else:
        m = (init + end) // 2
        v1 = maxVal(A, init, m)
        v2 = maxVal(A, m+1, end)
        return max(v1, v2)

for arq in arquivosNOrdenadosLidos:
    print('Arquivo lido {}'.format(arq))
    if(
        arq == '../Trabalho_esquenta_01/Nao_ordenados/Na0_ordenados/1000000.txt'
        or arq == '../Trabalho_esquenta_01/Nao_ordenados/Na0_ordenados/5000000.txt'
        or arq == '../Trabalho_esquenta_01/Nao_ordenados/Na0_ordenados/10000000.txt'
        or arq == '../Trabalho_esquenta_01/Nao_ordenados/Na0_ordenados/100000000.txt'
    ):
        pass
    else:
        try:
            vet = fct.carregaArquivo(arq)
            vetor = vet[0]
            mediaTempo = 0
            print(len(vetor))
            for i in range(0,10):
                inicio = time.time()
                maximo = maxVal(vetor, vetor[0], vetor[-1])
                print(maximo)
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

"""