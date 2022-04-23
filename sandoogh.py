#dandoogh

import time
import random


lst = []
n = int(input('Number of members ? : '))
for i in range(1,n+1) :
    n = input(f'Ozve {i} ra vared konid: ')
    lst.append(n)
winner =random.choice(lst)
print(40*'-')
print("ghoreh kashi bad az shomaresh makoos shroo mishavad")
for i in range (1,6):
    time.sleep(1)
    print(i,'...')

print(40*'*')
for i in winner :
    # if __name__ =='__main__':


    #     time.sleep(0.5)
        print ('Lucky Winner is : ', winner)
print(40*'*')
input(' press Enter to exit')

