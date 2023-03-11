"""
Напишете програма која бара од корисникот да внесе име и
години и потоа пресметува во која година тој ќе има 100 години.
Испечатете го неговото име и годината добиена.
"""
if __name__ == '__main__':
    currentYear = 2023
    print("Vnesete ime i godini:")
    name = input()
    age = int(input())

    birthYear = currentYear - age

    print(f"{name} ke ima 100 godini vo {birthYear + 100}")
