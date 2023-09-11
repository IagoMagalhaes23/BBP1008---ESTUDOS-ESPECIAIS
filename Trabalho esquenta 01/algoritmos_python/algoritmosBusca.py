'''
    Autor: Iago Magalhães
'''

def buscaCubica(vet, posicao, numeroProcurado):
    '''
        Função que realiza a busca cúbica
        :param vet: parâmetro que recebe um array com os dados para realizar a busca
        :param posicao: parâmetro com o valor a ser pesquisado
    '''

    for i in range(len(vet)):
        for j in range(len(vet)):
            for k in range(len(vet)):
                if(vet[i] == numeroProcurado and vet[j] == numeroProcurado and vet[k] == numeroProcurado):
                    posicao = i

    if(posicao != -1):
        print('Posição: {}'.format(posicao))
    else:
        print('Valor não encontrado')

def buscaQuadratica(vet, posicao, entrou, contador, numeroProcurado):
    '''
        Função que realiza a busca quadratica
        :param vet: parâmetro que recebe um array com os dados para realizar a busca
        :param posicao: parâmetro com o valor a ser pesquisado
    '''
    for i in range(len(vet)):
        j = i
        while(j < len(vet)):
            if(vet[i] == numeroProcurado):
                if(entrou == False):
                    posicao = i
                    if(vet[j] == numeroProcurado):
                        contador = contador + 1
            j = j + 1
        if(contador > 0):
            entrou = True
    if(entrou):
        print('Posição: {} - contador de repetição: {}'.format(posicao, contador))


def buscaSequencialv1(vet, numeroProcurado):
    '''
    
    '''
    indice = -1
    for i in range(len(vet)):
        if(vet[i] == numeroProcurado):
            indice = i
    return indice

def buscaSequencialv2(vet, numeroProcurado):
    '''
    
    '''
    indice = -1
    for i in range(len(vet)):
        if(vet[i] == numeroProcurado):
            return i
    return -1

def buscaTernaria(vet, numeroProcurado, n):
    '''
    
    '''
    inicio = 0
    fim = n -1
    print(inicio)
    print(fim)
    while(inicio <= fim):
        meio_esquerdo = inicio + (fim + inicio) / 3
        meio_direito = fim - (fim - inicio) / 3
        meio_esquerdo = int(meio_esquerdo)
        meio_direito = int(meio_direito)
        print(meio_direito)
        print(meio_esquerdo)

        if(vet[meio_esquerdo] == numeroProcurado):
            return meio_esquerdo
        elif(vet[meio_direito] == meio_direito):
            return meio_direito
        elif(vet[meio_esquerdo] > numeroProcurado):
            fim = meio_esquerdo - 1
        else:
            inicio = meio_esquerdo + 1
            fim = meio_direito - 1
    
    return -1

def pesquisaBinaria(vet, numeroProcurado, e, d):
    '''
    
    '''
    meio = (e + d) // 2
    # meio = int(meio)
    if(vet[meio] == numeroProcurado):
        return meio
    if(e >= d):
        return -1
    elif(vet[meio] < numeroProcurado):
        return pesquisaBinaria(vet, numeroProcurado, meio + 1, d)
    else:
        return pesquisaBinaria(vet, numeroProcurado, e, meio - 1)