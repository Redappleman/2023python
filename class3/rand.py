import random
rnum=random.randrange(0,4)
if rnum==0 :
    print("제주도로 감")
elif rnum == 1 :
    print('사이판으로 감')
else :
    print('하와이로 감')

user = int(input('가위 0  바위 1  보 2 : '))
com = random.randrange(3)
print('com 이 낸 것 : %d'%com)
if user == com : print("비겼음")

elif(user == 0 and com == 2)or (user == 1 and com ==0) or (user ==2 and com ==1):
    print("user 승리")
else :
    print('com 승리')