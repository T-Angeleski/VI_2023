"""
Користејќи list comprehension дадена матрица составена од броеви
да се промени секој елемент така што ќе се помножи со 2.
Секој елемент на матрицата се чита од тастатура така што прво се
читаат N и M (број на редици и колони) а потоа
во секој ред се читаат елементите одделени со празно место
"""

if __name__ == '__main__':
    n = int(input("Enter num rows: "))
    m = int(input("Enter num columns: "))
    matrix = []

    # Create matrix
    for i in range(n):
        rowElems = input("Enter element of row separated by empty space:")
        matrixRow = [int(elem) for elem in rowElems.split(" ")]
        matrix.append(matrixRow)

    # Multiply every element by 2
    newMatrix = [elem * 2 for row in matrix for elem in row]
    print(newMatrix)