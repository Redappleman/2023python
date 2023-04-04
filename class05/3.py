import random

exlist = [0]*20

for k in range(20) :
    
    exlist[k] = random.randrange(0,100)

print(exlist)
k = int(input("몇번째 데이터를 검색? : "))
print('%d 번쨰의 데이터 :  %d'%(k,exlist[k]))