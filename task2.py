'''
Задача:
    Напишите функцию, которая принимает список не отрицательных целых чисел,
    упорядочивает их так, чтобы они составляли максимально возможное число.
    Например, [50, 2, 1, 9], наибольшее сформированное число равно 95021.
Рекурсивный алгоритм решения:
    1 get_max_number(arr, i) принимает список чисел и число i - наибольшая
      цифра, стоящая в начале элементов списка arr
    2 arr разбивается на 2 списка: i_num(числа, начинающиеся на i)
      и other_num(числа, начинающиеся не на i)
    3 для списка i_num составляются все возможные перествновки его элементов,
      после чего выводится на экран вариант с наибольшим получившимся значением
    4 для списка other_num рекурсивно вызывается функция get_max_number
    5 выход из рекурсии происходит тогда, когда i станет равно 0
'''

import itertools
import random

def get_max_number(arr, i):
    i_num = []
    other_num = []
    for elem in arr:
        if elem[0] == str(i):
            i_num.append(elem)
        else:
            other_num.append(elem)
    if i_num:
        permutations = list(map("".join, itertools.permutations(i_num)))
        print(max(permutations), end="")
    i -= 1
    if i > 0:
        get_max_number(other_num, i)

if __name__ == '__main__':
    #arr = [2, 1, 9, 50]
    arr = [random.randint(0,1000) for i in range(10)]
    arr_str = list(map(str, arr))
    i = 9

    get_max_number(arr_str, i)
