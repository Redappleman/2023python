import random as r
tarot = ['Fool','magician','temperence','lovers','the high priestess'
         ,'chariot','hanged man','death','wheel of fortune',
         'the sun','justice','empress','emperor','the tower',
         'the star','strength','the devil','the moon','judgement'
         ,'hermit','hieropant','the world']

print('all tarot')
print(tarot)

for k in range(1,5):
    index = r.randrange(22)
    print('%d번째 타로는 %s'%(k+1,tarot[index]))
