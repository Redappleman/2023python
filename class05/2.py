import random

exlist = [0]*20

for k in range(20) :
    
    exlist[k] = random.randrange(0,51)
    print('%d 번째 데이터 %d'%(k+1,exlist[k]))
    

print("가장 작은 수 : %d"%min(exlist))