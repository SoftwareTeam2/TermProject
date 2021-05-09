n = int(input())
dp=[0]*(n+1)
dp[1]=1
dp[2]=2
for i in range(3,n+1):
    if i%2==0:
        dp[i] = (dp[i-2]+2)%10007
    else:
        dp[i] = (dp[i-1]+1)%10007
print(dp[n])