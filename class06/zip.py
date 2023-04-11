menulist = ['기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거']
pricelist = [4000, 4500, 5000, 7000]
#xlist = zip(menulist,pricelist)
#print(xlist)
tlist = list(zip(menulist, pricelist))
dlist = dict(zip(menulist, pricelist))

print('튜플 = ',tlist)
print('딕셔너리 = ',dlist)