def fastLIS(ary):
    dp = [[0 for _ in range(len(ary)+1)] for _ in range(len(ary)+1)]
    dp[0][0] = -1
    for i in range(len(ary)+1):
        dp[i][len(ary)] = 0
    for j in range(len(ary),-1,-1):
        for i in range(0,j-1):
            keep = 1+dp[j][j+1]
            skip = dp[i][j+1]
            dp[i][j] = max(keep,skip)
    return dp[i][j]