m = int(input('몇으로 나누기? :'))
print("%d 로 나누어지는 가장 가까운 수 답하기 : \n"%m)

for k in range(5):
    
    num = int(input('Call Number : '))
    answer = num / m
    if(answer < num ) :
        answer = num - (num %m)
    else :
        answer = num + (num/m)
    
    print('The answer is %d'% answer)

    