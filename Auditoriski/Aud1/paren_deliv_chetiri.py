"""
Напишете програма каде корисникот внесува број и на
екран му се печати 'Paren' ако бројот е парен или
'Neparen' ако бројот е непарен.
Дополнително ако бројот е делив со 4 да се испечати 'Deliv so 4'
"""

if __name__ == '__main__':
    print("Vnesete broj:")
    number = int(input())
    if number % 2 == 0:
        print("Paren")
    else:
        print("Neparen")

    if (number % 10) % 4 == 0:
        print("Deliv so 4")
