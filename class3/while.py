import random
c=0

while(True) :
    user = int(input('가위0 바위1 보2  : '))
    com = random.randrange(3)
    print('com 이 낸 것 :%d '%com)
    if user == com : print("비겼음")
    elif (user == 0 and com == 2)or (user == 1 and com ==0) or (user ==2 and com ==1):
        print('user 승리')
    elif(com == 0 and user == 2) or (com == 1 and user == 0) or (com == 2 and user == 1):
        print('com의 승리')
    else : 
        print('종료   =====총 %d 회 가위바위보 함===='%c)
        break
    c+=1
   

   
    
 



    
    