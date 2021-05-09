import sys
input = sys.stdin.readline

n = int(input())
warehouse = list(map(int,input().split()))

dp = [0]*(n+1)
dp[1]=warehouse[0]
dp[2]=warehouse[1]
for i in range(3,n+1):
    dp[i] = dp[i-2]+warehouse[i-1]
print(max(dp[n],dp[n-1]))