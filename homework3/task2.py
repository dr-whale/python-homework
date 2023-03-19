""" 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
Пользователь вводит это число с клавиатуры, список можно считать заданным. 
Введенное число не обязательно содержится в списке.
Примеры/Тесты:
Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
Output: 2
Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
Output: 10 """

number = int(input('Введите число X: '))
num_list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
different = abs(num_list[0] - number)
near = 0
for i in range(len(num_list)):
    temp = abs(num_list[i] - number)
    if temp < different:
        different = temp
        near = i
print(num_list[near])