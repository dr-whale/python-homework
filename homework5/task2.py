""" 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
    
	Примеры/Тесты:
    <function_name>(0,0) -> 0
    <function_name>(0,2) -> 2
    <function_name>(3,0) -> 3 """
# sum - стандартная функция, сменил название на loop_sum

def loop_sum (a = int(), b = int()):
    if b > 0:
        return loop_sum(a, b - 1) + 1
    return a

a = int(input("Input A: "))
b = int(input("Input B: "))

print(loop_sum(a, b))