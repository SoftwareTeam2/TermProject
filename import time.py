import time
hour, min = map(int,input().split())
add = int(input())
tm = time.gmtime(hour*60*60+min*60+add*60)
print(tm.tm_hour,tm.tm_min)