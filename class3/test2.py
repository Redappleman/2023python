import random

#choice =random.randrange(0,2) 
choice = bool(int(input('만날까 말까? 0/1 : ')))
print("오늘부터 1일 \n") if choice  else print('다음에\n')