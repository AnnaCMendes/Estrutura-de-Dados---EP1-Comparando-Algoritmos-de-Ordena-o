import time
import timeit
from heapq import heappush, heappop



def selecao(v):
    resp = []
    while len(v) > 0:
        m = min(v)
        resp.append(m)
        v.remove(m)
    return resp


def nolenmerge(array1,array2):
    merged_array=[]
    while array1 or array2:
        if not array1:
            merged_array.append(array2.pop(0))
        elif (not array2) or array1[0] < array2[0]:
            merged_array.append(array1.pop(0))
        else:
            merged_array.append(array2.pop(0))
    return merged_array

def nolenmergeSort(array):
    n  = len(array)
    if n <= 1:
        return array
    left = array[:int(n/2)]
    right = array[int(n/2):]
    return nolenmerge(nolenmergeSort(left),nolenmergeSort(right))

def heapsort(v):
  h = []
  for x in v:
    heappush(h, x)
  return [heappop(h) for i in range(len(h))]

def quicksort(v):
    if len(v) <= 1: 
        return v
    
    pivô = v[0]
    iguais  = [x for x in v if x == pivô]
    menores = [x for x in v if x <  pivô]
    maiores = [x for x in v if x >  pivô]
    return quicksort(menores) + iguais + quicksort(maiores)

def gera_linha():
    for i in range(30):
        print('-', end = '')
    print('')

from random import shuffle

tamanhos_vetores = [5000,10000,15000,20000,25000]
tempo_por_tamanho_vetores = []

gera_linha()
print ("EP1 - Vale a pena ordenar?")
gera_linha()
print ("Por: Anna Carolina de Oliveira Vale Mendes ")
gera_linha()
print ("Prof: Fernando Masanori")
gera_linha()
print('          |               Time(segundos) - 30s                |')
gera_linha()
print('          |  Mergesort  Quicksort   Seleção    Nativo    |')

for j in tamanhos_vetores:

    vetor_auxiliar = []
    
    vetor = list(range(j))
    shuffle(vetor)

    inicio = timeit.default_timer()
    auxiliar = nolenmergeSort(vetor)
    fim = timeit.default_timer()
    vetor_auxiliar.append( round(float(fim - inicio),2) )



    inicio = timeit.default_timer()
    auxiliar = quicksort(vetor)
    fim = timeit.default_timer()
    vetor_auxiliar.append( round(float(fim - inicio),2) )


    inicio = timeit.default_timer()
    auxiliar = selecao(vetor)
    fim = timeit.default_timer()
    vetor_auxiliar.append( round(float(fim - inicio),2) )

    inicio = timeit.default_timer()
    auxiliar = sorted(vetor)
    fim = timeit.default_timer()
    vetor_auxiliar.append( round(float(fim - inicio),2) )

    tempo_por_tamanho_vetores.append( vetor_auxiliar )

for i in range(int(len(tamanhos_vetores))):
    if( tamanhos_vetores[i] < 10000 ):
        print(' {0}     |'.format(tamanhos_vetores[i]), end = '' )
        for j in range(int(len(tempo_por_tamanho_vetores[i]))):
            if( tempo_por_tamanho_vetores[i][j] >= 30 ):
                print('   %2.2f   ' %tempo_por_tamanho_vetores[i][j] , end = '')
            else:
                print('    %2.2f   ' %tempo_por_tamanho_vetores[i][j] , end = '')
    else:
        print(' {0}    |'.format(tamanhos_vetores[i]), end = '' )
        for j in range(int(len(tempo_por_tamanho_vetores[i]))):
            if( tempo_por_tamanho_vetores[i][j] >= 30 ):
                print('   %2.2f   ' %tempo_por_tamanho_vetores[i][j] , end = '')
            else:
                print('    %2.2f   ' %tempo_por_tamanho_vetores[i][j] , end = '')
    print('  | ')
gera_linha()
