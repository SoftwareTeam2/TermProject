foodWarehouse = list(map(int,input().split()))
foodSum=0
foodSum+=max(foodWarehouse[0],foodWarehouse[1])
i=foodWarehouse.index(foodSum)
while i<=len(foodWarehouse)-3:
    if i == len(foodWarehouse)-3:
        foodSum+=foodWarehouse[len(foodWarehouse)-1]
        break
    if foodWarehouse[i+2]>foodWarehouse[i+3]:
        foodSum+=foodWarehouse[i+2]
        i+=2
    elif foodWarehouse[i+2]<foodWarehouse[i+3]:
        foodSum+=foodWarehouse[i+3]
        i+=3
    else:
        foodSum+=foodWarehouse[i+2]
        i+=2
print(foodSum)
