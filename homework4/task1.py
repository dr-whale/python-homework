""" 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
Если таких чисел нет - выдать внятное диагностическое сообщение
Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры
    
	Примеры/Тесты:
    Input1: 2 4 6 8 10 12 10 8 6 4 2
    Input2: 3 6 9 12 15 18
    Output: 6 12     Обратите внимание: Без скобочек, в одну строку

    Input1: 2 4 6 8 10 10 8 6 4 2
    Input2: 3 9 12 15 18
    Output: Повторяющихся чисел нет """

first_list = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
second_list = [3, 6, 9, 12, 15, 18]
#first_list = [2, 4, 6, 8, 10, 10, 8, 6, 4, 2]
#second_list = [3, 9, 12, 15, 18]
first_set = set(first_list)
second_set = set(second_list)
answer = sorted(list(first_set & second_set))
[print(i, end=' ') for i in answer] if len(answer) > 0 else print('Повторяющихся чисел нет')
