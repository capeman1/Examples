#Напишите программу,
#  которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.
import random
a=random.randint(88,300)
list_1=list(range(1,a))
list_1.append(237)
random.shuffle(list_1)
print(list_1)

for i in list_1:
    if i % 2 ==0:
        print(i)
    elif i==237:
        print('237 The end!')
        break
