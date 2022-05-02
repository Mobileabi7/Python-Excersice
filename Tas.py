#tas
#test commiit
#test commit 1
# اگر همه مردم  دنیا تاس بندازند / میانگین اینکه دفعه چندم شش اومده چیست ؟
import random

lst= []
count = 0
for i in range (1000000) :
    count +=1
    tas = random.randint(1,6)

    if tas == 6 :
        lst.append(count)
        count = 0
# print(lst)
print(sum(lst)/len(lst))
