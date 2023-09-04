'''
    Autor: Iago Magalhães
'''

import time
import os, psutil
import pandas as pd
import functions as fct
import algoritmosBusca as alg

process = psutil.Process()

caminhoOrdenados = '../ordenados/ordenados/'
caminhoNOrdenados = '../Nao_ordenados/Nao_ordenados/'
numeroProcurado = 0
posicao = -1
media = []
memoria = []

#-----------------------------------------------
# INICIANDO ÁNALISE DO ALGORITMO

arquivosOrdenadosLidos = fct.listFiles(caminhoOrdenados)
arquivosNOrdenadosLidos = fct.listFiles(caminhoNOrdenados)

for arq in arquivosOrdenadosLidos:
    print('Arquivo lido {}'.format(arq))
    if(arq == '../ordenados/ordenados/1000000.txt' or arq == '../ordenados/ordenados/5000000.txt' or arq == '../ordenados/ordenados/10000000.txt' or arq == '../ordenados/ordenados/100000000.txt'):
        pass
    else:
        try:
            vet = fct.carregaArquivo(arq)
            mediaTempo = 0
            for i in range(0,2):
                inicio = time.time()
                a = alg.buscaSequencialv2(vet[0], numeroProcurado)
                fim = time.time()
                memoria.append(fct.memoryUse())
                tempo = fim - inicio
                tempo = float(tempo)
                mediaTempo = mediaTempo + tempo

            # print(mediaTempo)
            media.append(mediaTempo / 10)
            # df = pd.DataFrame({
            #     'tempo de processamento': media,
            #     'memoria': memoria,
            #     'arquivo': arq
            # })
            # df.to_csv('{}.csv'.format(arq))
        except:
            print('Erro de memória')


# FINAL DA ÁNALISE DO ALGORITMO
#-----------------------------------------------

print('Ánalise dos resultados')
print('Média de tempo: {}'.format(media))
print('Consumo de memória: {}'.format(memoria))

'''
Resultados ordenados


'''

'''
Resultados não ordenados


'''