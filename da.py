def fiboDP(x):
    print(x)
    fib[0] = 0; fib[1] = 1
    if fib[x]!=-1:
        return fib[x]
    else:
        fib[x]=fiboDP(x-1)+fiboDP(x-2)

fib = [-1 for _ in range(10001)]
print(fiboDP(5))