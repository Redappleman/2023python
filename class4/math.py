import random


tnum = 1
gd = 0

for i in range(5) :
    num1 = random.randrange(1,100)
    num2 = random.randrange(1,100)
    answer = num1+num2
    print('%d + %d = '% (num1,num2) ,end='')
    user = int(input())

    if(user == answer):
        print('correct')
        gd+=1
    else :
        print('incorrect')
        tnum+=1
    if (tnum >3):
        print('gameover')
        break
print('%d개 맞춤'% gd)


