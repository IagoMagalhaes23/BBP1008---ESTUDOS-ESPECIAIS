'''
    Autor: Iago Magalhães
'''
import os
import psutil

def memoryUse():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss

def listFiles(caminho):
    '''
        Função para ler e listar arquivos de uma pasta
        :param caminho: recebe o endereço do diretório
        :param return: lista com endereço e nome dos arquivos
    '''
    nomes = []
    for diretorio, subpastas, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            nomes.append(os.path.join(diretorio, arquivo))
    return nomes

def carregaArquivo(arquivo):
    '''
        Função para ler arquivos txt
        :param arquivos: lista com endereço e nome dos arquivos
        :param return: lista com os valores lidos nos arquivos no formato inteiro
    '''
    valores = []

    instancia = open(arquivo, 'r')
    instancia = instancia.readlines()
    list(instancia)

    result = [item.split(',') for item in instancia]
    result = [value for value in result if value != " \n"]
    result_flat = []

    for l in result:
        for item in l:
            item  = ''.join(item.splitlines())
            item = item.replace(" ", "")
            result_flat.append(int(item))
        
    valores.append(result_flat)

    return valores