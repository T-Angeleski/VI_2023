""" Даден е робот кој се движи во рамнина почнувајќи од позицијата
(0,0). Роботот може да се движи ГОРЕ, ДОЛУ, ЛЕВО и ДЕСНО во дадена рамнина.
Патеката на движење на роботот е дадена на следниот начин:

    UP 5
    DOWN 3
    LEFT 3
    RIGHT 2

Ова означува дека роботот се движел 5 чекори во насока горе, 3 чекори во насока долу, 3 чекори во насока лево и 2 чекори во насока десно.

Потребно е да се пресмета Евклидово и Менхетен растојание на моменталната позиција на роботот по движењето и почетната позиција.

Пример: Ако дадените торки се дадени како влез на програмата: UP 5 DOWN 3 LEFT 3 RIGHT 2 , тогаш излезот на програмата треба да биде 2.24 за евклидовото растојание и 3 за менхетен растојанието (моменталната позиција на роботот е (-1, 2))."""

from math import sqrt

if __name__ == '__main__':
    robot = [0, 0]  # Start position

    while True:  # Enter # to stop commands
        command = input("Enter command: ")
        if command == "#": break
        commandParts = command.split(" ")

        if commandParts[0] == "UP":
            robot[1] += int(commandParts[1])  # y coordinate movement
        elif commandParts[0] == "DOWN":
            robot[1] -= int(commandParts[1])
        elif commandParts[0] == "LEFT":
            robot[0] -= int(commandParts[1])  # x coordinate movement
        elif commandParts[0] == "RIGHT":
            robot[0] += int(commandParts[1])

        print(f"CURRENT POSITION: {robot}")

        euclidean = sqrt((0 - robot[0]) ** 2 + (0 - robot[1]) ** 2)
        manhattan = abs(0 - robot[0]) + abs(0 - robot[1])

        print(f"MANHATTAN DISTANCE FROM (0, 0): {manhattan}")
        print(f"EUCLIDEAN DISTANCE FROM (0, 0): {euclidean:.2f}")