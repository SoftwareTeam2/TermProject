import sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)

for i in range(1,n+1):
    if dp[i]==0:
        if dp[i]%5==0:
            if dp[i//5]<dp[i-1]:
                dp[i]=dp[i//5]+1
            else:
                dp[i]=dp[i-1]+1
        if dp[i]%3==0:
            if dp[i//3]<dp[i-1]:
                dp[i]=dp[i//3]+1
            else:
                dp[i]=dp[i-1]+1
        if dp[i]%2==0:
            if dp[i//2]<dp[i-1]:
                dp[i]=dp[i//2]+1
            else:
                dp[i]=dp[i-1]+1
print(dp[n])