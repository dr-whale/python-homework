""" 6.2[32]: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)

	Напишите функцию
    - Аргументы: список чисел и границы диапазона
    - Возвращает: список индексов элементов (смотри условие)

	Примеры/Тесты:
    lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
    <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
    <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]

```(*)``` **Усложнение.**  Для формирования списка внутри функции используйте Comprehension
```(*)``` **Усложнение.**  Функция возвращает список кортежей вида: индекс, значение

	Примеры/Тесты:
    lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)] """

def in_range(original_list = list(), first_range = int(-100), second_range = int(100)):
    if first_range > second_range:
        first_range, second_range = second_range, first_range
    responce_list = [(i, original_list[i]) for i in range(len(original_list)) if first_range <= original_list[i] <= second_range]
    return responce_list

test_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

print(in_range(original_list = test_list, first_range = 2, second_range = 10))