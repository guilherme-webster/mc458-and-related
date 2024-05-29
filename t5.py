def minInterval(A, V):
    # primeiro devemos ordenar o array de intervalos pelo menor Li
    A.sort()

    # note que sem este elemento, se tivermos um membro da solucao otima que é último elemento de A
    # este não seria incluído na solução ótima na nossa implementação
    A.append((float('inf'), float('inf')))

    # começo do intervalo target 
    start =  0

    # final do intervalo target
    end = -1

    # contador do número de intervalos da sol. ótima
    counter = 0

    i = 0
    sols = []
    while i < len(A):
        # fazemos uma escolha gulosa buscando maximizar o tamanho do intervalo escolido
        if A[i][0] <= start:
            if A[i][1] > end:
                end = max(A[i][1], end)
                optimal_cadidate = i
            i += 1
        # quando achamos o maior end, dado um start, nós incluímos este intervalo na nossa solução
        else:

            start = end

            counter += 1
            sols.append(A[optimal_cadidate])

            # se end >= V ja percorremos os intervalos que irão cobrir [0, V]
            # senão, se o começo do intervalo atual for maior que o end, não temos como cobrir [0, V]
            if A[i][0] > end or end >= V:
                break
    # caso que não conseguimos cobrir o intervalo target
    if end < V:
        return 0, []
    
    return counter, sols
        
V = int(input())
n = int(input())
A = []
for _ in range(n):
    aux = list(map(int, input().strip().split()))
    A.append(aux)
num_intervals, sol_intervals =  minInterval(A, V)
print(num_intervals)
if(num_intervals != 0):
    for interval in sol_intervals:
        print(interval[0], interval[1])
