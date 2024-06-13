from functools import cmp_to_key

class Job:

    def __init__(self, s, f, p):
        self.s = s
        self.f = f
        self.p = p

def jobComp(j1, j2):
    return j1.f < j2.f

def latestNonConflicting(arr, i):
    for j in range(i-1, -1, -1):
        if arr[j].f <= arr[i - 1].s:
            return j
        
    return -1

def maxProfit(arr, n):

    dp = [0] * n
    arr = sorted(arr, key=cmp_to_key(jobComp))

    # Base case
    dp[0] = arr[0].p

    for i in range(1, n):

        latestJob = latestNonConflicting(arr, i)
        includeJob = arr[i].p
        
        if latestJob != -1:
            includeJob += dp[latestJob]

        dp[i] = max(includeJob, dp[i - 1])

    return dp[n - 1]

# Driver code
values = [(3, 10, 20), (1, 2, 50),
          (6, 19, 100), (2, 100, 200)]
arr = []
for i in values:
    arr.append(Job(i[0], i[1], i[2]))
 
n = len(arr)
 
print("The optimal profit is", maxProfit(arr, n))
