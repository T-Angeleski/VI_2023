"""
Да се напише функција која за дадена листа од торки во облик
[('a', 1), ('b', 2), ('c', 3)] ќе направи swap на
елементите во торките така што
елементот на позиција 0 ќе биде елемент на позиција 1 и обратно.
Да се користи list comprehension.
"""


def swapTuple(tup):
    return [(y, x) for (x, y) in tup]


if __name__ == '__main__':
    tuple1 = [('a', 1), ('b', 2), ('c', 3)]
    tuple2 = [(10, 20), (30, 40), (50, 60)]

    print(swapTuple(tuple1))
    print(swapTuple(tuple2))