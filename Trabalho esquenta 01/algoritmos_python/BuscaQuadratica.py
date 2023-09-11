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
numeroProcurado = 50
posicao = -1
entrou = False
contador = 0
media = []
memoria = []

#-----------------------------------------------
# INICIANDO ÁNALISE DO ALGORITMO

arquivosOrdenadosLidos = fct.listFiles(caminhoOrdenados)
arquivosNOrdenadosLidos = fct.listFiles(caminhoNOrdenados)

for arq in arquivosOrdenadosLidos:
    print('Arquivo lido {}'.format(arq))
    if(arq == '../ordenados/ordenados/10000000.txt' or arq == '../ordenados/ordenados/100000000.txt'):
        pass
    else:
        try:
            vet = fct.carregaArquivo(arq)
            # vet = [1,2,3,4,5,6,7,10,30,50]
            mediaTempo = 0
            for i in range(0,10):
                inicio = time.time()
                alg.buscaQuadratica(vet[0], posicao, entrou, contador, numeroProcurado)
                fim = time.time()
                memoria.append(fct.memoryUse())
                tempo = fim - inicio
                tempo = float(tempo)
                mediaTempo = mediaTempo + tempo
        except:
            print('Erro de memória')


# FINAL DA ÁNALISE DO ALGORITMO
#-----------------------------------------------

print('Ánalise dos resultados')
print('Média de tempo: {}'.format(media))
print('Consumo de memória: {}'.format(memoria))

'''
Resultados ordenados

Ánalise dos resultados
Média de tempo: [5.223751068115234e-05, 0.00012307167053222657, 0.0010198354721069336, 0.00034029483795166015, 0.0, 0.0002084016799926758, 0.0005432844161987304, 0.0001521587371826172, 0.00010154247283935546, 0.0, 0.0]
Consumo de memória: [55910400, 55910400, 55910400, 55910400, 55910400, 55910400, 55910400, 55910400, 55910400, 55910400, 56131584, 56131584, 56131584, 56131584, 56131584, 56131584, 56131584, 56131584, 56131584, 56131584, 57528320, 57528320, 57528320, 57528320, 57528320, 57528320, 57528320, 57528320, 57528320, 57528320, 64102400, 64102400, 64102400, 64102400, 64102400, 64102400, 64102400, 64102400, 64102400, 64102400, 103698432, 103698432, 103698432, 103698432, 103698432, 103698432, 103698432, 103698432, 103698432, 103698432, 62173184, 62173184, 62173184, 61583360, 61583360, 61583360, 61583360, 61583360, 61583360, 61583360, 61628416, 61628416, 61628416, 61628416, 61628416, 61628416, 61628416, 61628416, 61628416, 61628416, 61763584, 61763584, 61763584, 61763584, 61763584, 61763584, 61763584, 61763584, 61763584, 61763584, 63508480, 63508480, 63508480, 63508480, 63508480, 63508480, 63508480, 63508480, 63508480, 63508480, 83521536, 83521536, 83521536, 83521536, 83521536, 83521536, 83521536, 83521536, 83521536, 83521536, 265474048, 265474048, 265474048, 265474048, 265474048, 265474048, 265474048, 265474048, 265474048, 265474048]

'''

'''
Resultados não ordenados

Ánalise dos resultados
Média de tempo: [0.0005660057067871094, 0.0005017995834350586, 0.0, 0.0004510402679443359, 0.0003098726272583008, 0.0, 0.00037992000579833984, 0.00021452903747558593, 0.0005536794662475586, 0.00028290748596191404, 0.0011591196060180664]
Consumo de memória: [460353536, 460369920, 460369920, 460369920, 460369920, 460369920, 460369920, 460369920, 460369920, 460369920, 464613376, 464613376, 464613376, 464613376, 464613376, 464613376, 464613376, 464613376, 464613376, 464613376, 465747968, 465747968, 465747968, 465747968, 465747968, 465747968, 465747968, 465747968, 465747968, 465747968, 466821120, 466821120, 466821120, 466821120, 466821120, 466821120, 466821120, 466821120, 466821120, 466821120, 467816448, 467816448, 467816448, 467816448, 467816448, 467816448, 467816448, 467816448, 467816448, 467816448, 459550720, 459550720, 459550720, 458514432, 458514432, 458514432, 458514432, 458514432, 458514432, 458514432, 459812864, 459812864, 459812864, 459812864, 459812864, 459812864, 459812864, 459812864, 459812864, 459812864, 460996608, 460996608, 460996608, 460996608, 460996608, 460996608, 460996608, 460996608, 460996608, 460996608, 462041088, 462041088, 462041088, 462041088, 462041088, 462041088, 462041088, 462041088, 462041088, 462041088, 463142912, 463142912, 463142912, 463142912, 463142912, 463142912, 463142912, 463142912, 463142912, 463142912, 463343616, 463343616, 463343616, 463343616, 463343616, 463343616, 463343616, 463343616, 463343616, 463343616]

'''