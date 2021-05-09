import time

n = int(input('n : '))
count=0
sec=n*60*60+59*60+59

for i in range(sec+1):
    tm=time.gmtime(i)
    hour = str(tm.tm_hour)
    mins = str(tm.tm_min)
    secs = str(tm.tm_sec)
    if(hour.find('3')!=-1 or mins.find('3')!=-1 or secs.find('3')!=-1):
        count+=1
print(count)
