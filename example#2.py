# Задача 2
# Даны списки:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

set_1=set(a)

set_2=set(b)

list_new=list(set.intersection(set_1,set_2))



print('Mission complate: ',list_new)