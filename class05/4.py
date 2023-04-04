import random

exlist = [0]*20

for k in range(20) :
    exlist[k] = random.randrange(0,51)

count = 1
exlist2 = []
while count < 20 :
    exlist2.append(exlist)
    count+=1

print(exlist2)