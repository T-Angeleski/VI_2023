"""
Напишете програма која од листа на броеви
(на пример, a=[5, 10, 15, 20])
ќе направи нова листа од само првиот и последниот елемент.
За вежбање кодот поставете го во функција.
"""


def get_first_and_last(list):
    result = [list[0], list[-1]]
    """
    result = []
    result.append(list[0])
    result.append(list[-1])
    """
    return result


if __name__ == '__main__':
    a = [5, 10, 15, 20]
    new_list = get_first_and_last(a)
    print(new_list)
