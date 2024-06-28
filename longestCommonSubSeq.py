def LCS(s1, s2, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    sol = [[0, 0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    """for j in range(n + 1):
        dp[0][j] = 0

    for i in range(m + 1):
        dp[i][0] = 0"""
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                sol[i][j] = [-1, 1]
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    sol[i][j] = [0, 1]
                else:
                    dp[i][j] = dp[i][j - 1]
                    sol[i][j] = [-1, 0]

    return dp[m][n], sol

def printSol(sol, s1, i, j):
    if(i > 0 and j > 0):
        if sol[i][j] == [-1, 1]:
            printSol(sol, s1, i - 1, j - 1)
            print(s1[i - 1], end="")
        else:
            if sol[i][j] == [0, 1]:
                printSol(sol, s1, i - 1, j)
            else:
                printSol(sol, s1, i, j - 1)

s1 = "abcb"
s2 = "bdcab"
m = 4
n = 5

maxLenght, solutionArr = LCS(s1, s2, m, n)

print(maxLenght)
printSol(solutionArr, s1, m, n)
print()