n, m = map(int,input().split())

command=[]
for i in range(m):
    a,b,c=map(int,input().split())
    command.append((a,b,c))

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i]=i

for line in command:
    if line[0]==0:
        union_parent(parent,line[1],line[2])
    else:
        if find_parent(parent,line[1]) == find_parent(parent,line[2]):
            print('YES')
        else:
            print('NO')