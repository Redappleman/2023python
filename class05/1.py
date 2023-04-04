import random

exlist = [0]*20

for k in range(20) :
    exlist[k] = random.randrange(0,101)
    print('%d 번째 데이터 %d'%(k+1,exlist[k]))
    

for k in range(20) : 
    exlist.sort()
    print("sorted data : %d"%exlist[k])
