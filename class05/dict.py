mdict_list= {'햄버거' : 4000,'치즈버거' : 4500,'불고기버거' : 5000,'싸이버거' : 7000}

print(mdict_list)

mdict_list['새우버거'] = 5500

print(mdict_list)

mdict_list['불고기버거'] = mdict_list['불고기버거'] + 500

print(mdict_list)

del[mdict_list['햄버거']]

mdict_list['나이스버거'] = 2000

print(mdict_list)

for k in mdict_list.keys() :
    print(k ,':',mdict_list[k])
