from searching_framework import Problem
from searching_framework.uninformed_search import *


def moveFootballer(x, y, bX, bY, direction, opponents):
    if direction == "up":
        if y + 1 < 8 and (x, y + 1) not in opponents \
                and (x, y + 1) != (bX, bY):
            y += 1

    elif direction == "down":
        if y - 1 >= 0 and (x, y - 1) not in opponents \
                and (x, y - 1) != (bX, bY):
            y -= 1

    elif direction == "right":
        if x + 1 < 6 and (x + 1, y) not in opponents \
                and (x + 1, y) != (bX, bY):
            x += 1

    elif direction == "up-right":
        if y + 1 < 8 and x + 1 < 6 and (x + 1, y + 1) not in opponents \
                and (x + 1, y + 1) != (bX, bY):
            x += 1
            y += 1
    else:  # Down right
        if y - 1 >= 0 and x + 1 < 6 and (x + 1, y - 1) not in opponents \
                and (x + 1, y - 1) != (bX, bY):
            x += 1
            y -= 1

    return x, y


def kickBall(x, y, bX, bY, direction, opponents):
    pass


class Footballer(Problem):
    def __init__(self, opponents, initial, goal=None):
        super().__init__(initial, goal)
        self.opponents = opponents

    def successor(self, state):
        successors = {}
        # State = ((x, y), (ballY, ballY))
        x, y = state[0][0], state[0][1]
        ballX, ballY = state[1][0], state[1][1]

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        ballPos = state[1]
        return (ballPos[0], ballPos[1]) == (7, 3) or \
            (ballPos[0], ballPos[1]) == (7, 4)


if __name__ == '__main__':
    man_pos = tuple(map(int, input().split(',')))
    ball_pos = tuple(map(int, input().split(',')))

    opponents = [(3, 3), (5, 4)]

    footballer = Footballer(opponents, (man_pos, ball_pos))