# Требуется написать программу, которая выведет квадраты положительных элементов списка в обратном порядке. 
# решение должно быть написано в одну строку.
#sorted([-1,2,-3,4,0,-5,6], )

print(sorted([i**2 for i in [-1,2,-3,4,0,-5,6] if i > 0],reverse=True))

