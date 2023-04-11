oldlist = ['짜장면','탕수육','군만두']

newlist = oldlist
print(newlist)
oldlist[0] = '짬뽕'
oldlist.append('깐풍기')
print(newlist)

oldlist1 = ['좀비','스켈레톤','크리퍼']

newlist1 = oldlist1[:]
print(newlist1)
oldlist1[0] = '샌즈'
oldlist1.append('스파이더 맨')
print(oldlist1)
print(newlist1)