# smart_task

Задача 2:

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
