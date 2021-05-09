def solution(food_times,k):
    l_list = [[i+1,food_times[i]] for i in range(len(food_times))]
    for i in range(len(food_times)):
        (l_list[i])[1] -= 1
        if (l_list[i])[1] == 0:
            l_list.pop(i)
    return l_list
print(solution([3,1,2],5))
