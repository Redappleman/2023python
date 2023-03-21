digit=2
sum=0
n=int(input("정수 입력 : "))
for digit in range(2,n+1,2):
    sum+=digit
print('1부터 ',n,'까지의 합 :',sum)