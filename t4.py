def max_tasks(n, x, s):

    # L é o nosso array que guarda a solção ótima considerando até o dia j, supondo que o último reboot não foi no dia j
    L = [0] * (n + 1)
    L[1] = min(s[0], x[0])

    # P é o nosso array que guarda o último dia do reboot de uma solução ótima, dado que consideramos até o dia j
    P = [0] * (n + 1)

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Queremos montar a tabela com os dados processados do dia i até o dia j, dado que o último reboot foi no dia i - 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            days_since_last_reboot = j - i
            dp[i][j] += dp[i][j - 1] + min(s[days_since_last_reboot], x[j - 1])

    # Agora, queremos construir nosso array L o qual deve armazenar a quantidade mámxima de dados processados até o dia j, dado que foi feito um reboot no dia k
    for j in range(2, n + 1):
        max = 0
        k_candidate = 0
        for k in range(j):
            if L[k - 1] + dp[k + 1][j] > max:
                max = L[k - 1] + dp[k + 1][j]
                k_candidate = k
        L[j] = max
        P[j] = k_candidate

    # Precisamos reconstruir nossa solução
    reboot_days = []
    idx = n
    while idx > 0:
        reboot_days.append(P[idx])
        idx = P[idx]

    '''# Imprimindo a tabela dp, para fins de debug
    for idx, row in enumerate(dp):
        print(f"Dia {idx}: {row}")'''

    return L[n], reboot_days

n = int(input())
x = list(map(int, input().strip().split()))
s = list(map(int, input().strip().split()))

max_data_processed, reboot_days = max_tasks(n, x, s)
print(max_data_processed)
for _ in range(len(reboot_days) - 1, 0, -1):
    print(reboot_days[_], end=" ")
print(reboot_days[0])
