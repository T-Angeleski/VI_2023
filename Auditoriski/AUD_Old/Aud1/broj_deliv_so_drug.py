"""
Напишете програма која на влез прима два броја и
проверува дали првиот број е делив со вториот.
Да се испечати 'Deliv' ако е делив.
"""
if __name__ == '__main__':
    print("Vnesete dva broja:")
    num1 = int(input())
    num2 = int(input())
    if num1 % num2 == 0:
        print("Deliv")
