print(('1234'.isdigit()))
print(('abcd'.isalpha()))
print(('abc1234'.isalnum()))
print(('abcd'.islower()))
print(('ABCD'.isupper()))
print((' '.isspace()))

upp,low,dig,pct = 0,0,0,0

pswd = input('암호 입력  : ')

if pswd.isalnum == False :
    pct = 1
for k in pswd :
    if k.isupper() : upp = 1
    elif k.islower() : low = 1
    elif k.isdigit() : dig = 1

if low+upp+dig+pct >= 3 :
    print('사용 가능')
else :
     print("사용불가")