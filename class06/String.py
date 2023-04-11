str = '문자열이리스트'

print(str[1:4])
print(str[4:])
print(str[:4])
print(str[:])
print(str[-1])
print(str[-6:-1])
print(str[4:7]*3)
#del(str[3])  del 사용 불가
st2 = '문자열'

for k in range(len(st2)) :
    print('< %s >' % st2[k])

for k in st2 :
    print('< %s >'%k)

if '문' in st2 :
    print('문 있음')
st1 = input('문자열 입력 : ')

for k in range(len(st1) -  1,-1,-1) :
    print(st1[k],end='')


