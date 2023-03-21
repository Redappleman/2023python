select = int(input('1.입력한 수식 계산   2. 두 수 사이의 합계 : '))

if select == 1 :
    nexp=input('수식 입력 :: ')
    answer = eval(nexp)
    print('%s 결과는  %5.1f '%(nexp,answer))

elif select == 2 :
    num1 = int(input('첫번째 수 입력 :'))
    num2 = int(input('두번째 수 입력 :'))
    answer = 0
    c=num1
    for i in range(num1,num2+1) :
        answer = answer+c
        c+=1
        
    print('%d + ... +%d 는 %d'%(num1,num2,answer))