""" 1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
Например для числа 145 сумма цифр будет 10: 1 + 4 + 5

Примеры/Тесты:
123 >>> Сумма чисел числа 123 равна 6
100 >>> Сумма чисел числа 100 равна 1 """

number = str(input('Введите число: '))
answer = 0
for i in number:
    answer += int(i)
print(f'Сумма чисел числа {number} равна {answer}')