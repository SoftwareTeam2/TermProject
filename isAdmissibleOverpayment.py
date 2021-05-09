import re
def isAdmissibleOverpayment(prices, notes, x):
    differ = [(re.findall('\d+[.]\d+|Same',stats)[0], "higher" in stats) for stats in notes]
    pay=[]
    for instore,(per,line) in zip(prices,differ):
        if per == 'Same':
            pay.append(0)
            continue
        if line == True:
            pay.append(instore - instore/(1+(float(per)/100)))
        elif line == False:
            pay.append(instore - instore/(1-(float(per)/100)))
    return sum(pay) - x <= abs(0.00000001)
        

print(isAdmissibleOverpayment([110, 95, 70],["10.0% higher than in-store", 
 "5.0% lower than in-store", 
 "Same as in-store"],5))