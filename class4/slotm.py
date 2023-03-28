import random as r
import time as t
n = int(input("몇번 돌림? :"))
slot = [0]*3
for i in range(n) :
    for k in range(3) :
        slot[k] = r.randrange(7,10)
        print("%d " % slot[k],end = '')
        t.sleep(1)
    if slot[0] ==7 and slot[1] ==7 and  slot[2] == 7:
        print('Jackpot!')
    else:
        print('too close')
