"""
Да се дефинира класа за Агент кој ја чува својата позиција
(координати x и y) во некој простор.
Да се дефинира метод кој го означува движењето на агентот во просторот.
Потоа да се дефинираат агенти кои имплементираат специфично движење
(лево, десно, горе, долу).
Извршете 5 движења за секој од агентите и
испечатете ја позицијата на агентот во секој чекор.
"""


class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        pass

    def __str__(self):
        return f"Position {self.x}, {self.y}"


class UpAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y += 1


class DownAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y -= 1


class LeftAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x += 1


class RightAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x -= 1


if __name__ == '__main__':
    startX = int(input("Enter starting x coordinate:"))
    startY = int(input("Enter starting x coordinate:"))

    up = UpAgent(startX, startY)
    down = DownAgent(startX, startY)
    left = LeftAgent(startX, startY)
    right = RightAgent(startX, startY)

    print(f"Starting positions for all agents ({startX}, {startY})")

    for i in range(5):
        up.move()
        print(f"Up Agent after move {i + 1}: {up}")

    print()

    for i in range(5):
        down.move()
        print(f"Up Agent after move {i + 1}: {down}")

    print()

    for i in range(5):
        left.move()
        print(f"Up Agent after move {i + 1}: {left}")

    print()

    for i in range(5):
        right.move()
        print(f"Up Agent after move {i + 1}: {right}")