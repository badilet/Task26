# Напишите функцию которая подсчитает количество счетных и несчетных чисел в списке
# чисел.

num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
even = [x for x in num_list if x % 2 == 0]
print(len(even))

odd = [x for x in num_list if x % 2 != 0]
print(len(odd))
