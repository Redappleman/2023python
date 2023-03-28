suNo,quizNo = map(int,input().split())
numbers = list(map(int,input().split()))
psum = [0]
temp = 0

for i in numbers :
    temp = temp +i
    psum.append(temp)

print(psum)

for i in range(quizNo):
    s,e =map(int,input().split())
    print(psum[e]-psum[s-1])


    