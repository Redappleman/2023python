n=int(input('몇개의 데이터를 처리 ? :'))
listex = [0]*n
sum=0

print('%d 개의 데이터 입력 :' % n)
for k in range(n):
    #listex.append(int(input()))
    listex[k] = int(input())
    sum+=listex[k]

print('리스트 데이터의 합과 평균 : %d   %.2f'% (sum,sum/n))
min=listex[0]
max=listex[0]
for k in range(1,n):
    if(listex[k]>max):
        max=listex[k]
    elif(listex[k]<min):
        min=listex[k]

print('가장 큰 데이터 : %d  가장 작은 데이터 %d '%(max,min))


