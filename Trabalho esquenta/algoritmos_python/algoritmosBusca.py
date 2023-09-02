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
                print(vet[i])
                if(entrou == False):
                    posicao = i
                    if(vet[j] == numeroProcurado):
                        contador = contador + 1
            j = j + 1
        if(contador > 0):
            entrou = True
    if(entrou):
        return print('Posição: {} - contador de repetição: {}'.format(posicao, contador))


def buscaSequencial():
    '''
    
    '''
    pass

def buscaTernaria():
    '''
    
    '''
    pass

def pesquisaBinaria():
    '''
    
    '''
    pass