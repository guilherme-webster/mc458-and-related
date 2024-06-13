def custo_minimo(n, M, s, p):
    # Inicialização das tabelas de DP
    dp_SL = [0] * (n + 1)
    dp_PA = [0] * (n + 1)
    C = [0] * (n + 1)
    # Tabela que efeitvamente irá guardar os locais
    locais_otimos = [0] * (n + 1)
    
    # Inicialização para o mês 1
    dp_SL[1] = s[0]
    dp_PA[1] = p[0]
    if dp_PA[1] < dp_SL[1]:
        C[1] = dp_PA[1]
        locais_otimos[1] = "PA"
    else:
        C[1] = dp_SL[1]
        locais_otimos[1] = "SL"

    
    # Preenchendo as tabelas dp_SL e dp_PA para cada mês
    for i in range(2, n + 1):
        dp_SL[i] = min(dp_SL[i-1], dp_PA[i-1] + M) + s[i-1]
        dp_PA[i] = min(dp_PA[i-1], dp_SL[i-1] + M) + p[i-1]
        if dp_PA[i] < dp_SL[i]:
            C[i] = dp_PA[i]
            locais_otimos[i] = "PA"
        else:
            C[i] = dp_SL[i]
            locais_otimos[i] = "SL"
    
    # O custo mínimo será o menor valor entre terminar em SL ou PA no mês n
    return C[n], locais_otimos

# Exemplo de uso
n = 4
M = 10
s = [1, 3, 20, 40]
p = [50, 20, 2, 4]
"""s = [2, 3, 4, 4]
p = [3, 2, 5, 5]"""

custo, locais = custo_minimo(n, M, s, p)
print("Custo mínimo:", custo)
for _ in range(1, len(locais) - 1):
    print(locais[_], end=" ")
print(locais[len(locais) - 1])
