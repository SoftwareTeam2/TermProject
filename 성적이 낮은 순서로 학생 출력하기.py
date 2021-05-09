import operator
num = int(input('학생 명수  :'))
s_dict = {}
for i in range(num):
    name, score = map(str,input().split())
    s_dict[name]=int(score)
s_dict = dict(sorted(s_dict.items(), key=operator.itemgetter(1)))
print(s_dict.keys())