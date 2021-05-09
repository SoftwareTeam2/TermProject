import pandas as pd
def makeOne(n):
    if n==1:
        return 0
    if n<4:
        return 1
    dp = [0 for _ in range(n+1)]
    dp[2] = 1
    dp[3] = 1
    for i in range(4,n+1):
        if not dp[i]:
            if i%3==0 and i%2==0:
                dp[i] = min(dp[i//3]+1,dp[i//2]+1,dp[i-1]+1)
            elif i%3 == 0:
                dp[i] = min(dp[i//3]+1,dp[i-1]+1)
            elif i%2==0:
                dp[i] = min(dp[i//2]+1,dp[i-1]+1)
            else:
                dp[i] = dp[i-1]+1
    pd.set_option('display.max_row', 500)
    pd.set_option('display.max_columns', 100)   
    sr1=pd.Series(dp)
    return sr1
n = int(input())
print(makeOne(n))
