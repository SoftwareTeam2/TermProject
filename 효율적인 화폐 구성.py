n, goal = map(int, input().split())
dp = [0]*(goal+1)
coins = []
count = 0
for i in range(n):
    coins.append(int(input()))
for i in range(goal+1):
    if i < coins[0]:
        dp[i] = -1
    if i in coins:
        dp[i] = 1
for i in range(coins[0]+1, goal+1):
    tempCoin = 0
    if dp[i] == 0:
        for coin in coins:
            if coin == coins[0]:
                tempCoin = coin
                continue
            if dp[i-coin] == -1 and dp[i-tempCoin] != -1:
                dp[i] = dp[i-tempCoin]+1
            elif dp[i-coin] != -1 and dp[i-tempCoin] == -1:
                dp[i] = dp[i-coin]+1
            elif dp[i-coin] == -1 and dp[i-tempCoin] == -1:
                dp[i] = -1
            else:
                if dp[i-coin] < dp[i-tempCoin]:
                    dp[i] = dp[i-coin]+1
                    break
                else:
                    dp[i] = dp[i-tempCoin]+1
                    break
        if dp[i] == 0:
            dp[i] = -1
print(dp[goal])