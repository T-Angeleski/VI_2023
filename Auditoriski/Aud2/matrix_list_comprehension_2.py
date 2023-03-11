"""
Задача 4 - Вгнездени list comprehension со проверки

Користејќи list comprehension дадена матрица составена од броеви
да се промени секој елемент така што
ако припаѓа во горната половина(индексот на редицата е помеѓу 0 и n/2)
треба да се помножи со 2 а ако припаѓа на
долната половина треба да се помножи со 3.
"""


def changeElement(elem, i, n):
    if i < n / 2:
        return elem * 2
    else:
        return elem * 3


if __name__ == '__main__':
    n = int(input("Enter num rows: "))
    m = int(input("Enter num columns: "))
    matrix = []

    for i in range(n):
        nums = input().split(" ")
        row = [int(elem) for elem in nums]
        matrix.append(row)

    result = [[changeElement(matrix[row][elem], row, n) for elem in range(m)]
              for row in range(n)]
    print(result)