numeroProcurado = 100
posicao = -1
entrou = False
contador = 0
vet = [2,3,4,5,10,11,13]

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