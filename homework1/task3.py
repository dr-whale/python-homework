""" 1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
 Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
Примеры/Тесты:
385916 >>> yes
123456 >>> no
(*) Усложнение. Вывод результат на экран сделайте одной строкой(только один print), для этого используйте тернарный оператор """

number = str(input('Введите номер билета: '))
first_side = int(number[0]) + int(number[1]) + int(number[2])
second_side = int(number[3]) + int(number[4]) + int(number[5])
print('YES') if first_side == second_side else print('NO')