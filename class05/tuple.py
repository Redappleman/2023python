menu = ('햄버거','치즈버거','불고기버거','싸이버거')
price = (400,4500,5000,7000)

for k in range(len(menu)) : 
    print(k+1,' : ',menu[k],': ',price[k])

lmenu = list(menu)
lprice = list(price)
lmenu.append('새우버거')
lprice.append(5500)

menu = tuple(lmenu)
price = tuple(lprice)
print('메뉴 : ',menu)
print('가격 : ',price)