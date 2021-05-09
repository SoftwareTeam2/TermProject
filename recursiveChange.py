coin = [6,5,1]
def dpChange(money):
    dp = [i==6 or i==5 or i== 1 for i in range(money+1)]
    for i in range(1,money+1):
        if not dp[i]:
            if i<7:
                dp[i] = dp[i-1]+1
            else:
                dp[i] = min(dp[i-6]+1,dp[i-5]+1,dp[i-1]+1)
    return dp[money]

money = int(input())
print(dpChange(money))
