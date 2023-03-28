import random

answer = random.randrange(1,21)

user = 0
count = 1
while(True) :
   user = int(input('1~20 까지의 숫자 입력 : '))
   
   if(user == answer) :
      print('정답')
      break
   elif(user < answer) :
      print('High')
      count+=1
   else :
      print('low')

   

    
    
  
print('%d 회 만에 맞춤'% count)
    