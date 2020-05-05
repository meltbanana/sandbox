# Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке,
# как показано в примере (здесь n=5):
#
# Sample Input:
# 5

# Sample Output:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

import numpy as np

def wrap(A):
    #текущее минимальное значение
    m = A[0][0]

    #поворачиваем матрицу на 90 градусов = транспонирование и отражение по горизонтали
    B = np.array(A)
    B = B.transpose().tolist()
    B = [list(reversed(i)) for i in B]

    #вставляем верхнюю строку
    newline = [m-i-1 for i in reversed(range(len(B[0])))]
    B.insert(0, newline)
    return B


try:
    n = int(input("Введите ширину квадрата (например - 5) :"))

    #начинаем с середины (наибольшего значения)
    #и катаем снеговика вокруг него, пока не дойдём до 1 (единицы)
    #для наглядности - откоменируй первую строку в цикле

    A = [[n*n]]
    while A[0][0] > 1:
        #print(np.array(A), "\nwrap")
        A = wrap(A)

    print(np.array(A))

except ValueError:
    print("Ошибка, нужно было ввести целое число, попробуйте еще раз.")
