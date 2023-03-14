from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def moveRight(mainX, mainY, otherX1, otherY1, otherX2, otherY2, obstacles):
    while mainX < 8 and [mainX + 1, mainY] not in obstacles \
            and [mainX + 1, mainY] != [otherX1, otherY1] \
            and [mainX + 1, mainY] != [otherX2, otherY2]:
        mainX += 1
    return mainX


def moveLeft(mainX, mainY, otherX1, otherY1, otherX2, otherY2, obstacles):
    while mainX > 0 and [mainX - 1, mainY] not in obstacles \
            and [mainX - 1, mainY] != [otherX1, otherY1] \
            and [mainX - 1, mainY] != [otherX2, otherY2]:
        mainX -= 1
    return mainX


def moveUp(mainX, mainY, otherX1, otherY1, otherX2, otherY2, obstacles):
    while mainY < 6 and [mainX, mainY + 1] not in obstacles \
            and [mainX, mainY + 1] != [otherX1, otherY1] \
            and [mainX, mainY + 1] != [otherX2, otherY2]:
        mainY += 1
    return mainY


def moveDown(mainX, mainY, otherX1, otherY1, otherX2, otherY2, obstacles):
    while mainY > 0 and [mainX, mainY - 1] not in obstacles \
            and [mainX, mainY - 1] != [otherX1, otherY1] \
            and [mainX, mainY - 1] != [otherX2, otherY2]:
        mainY -= 1
    return mainY


class Molecule(Problem):
    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()

        # One atom can move per turn
        # Movement is until wall is hit
        h1X, h1Y = state[0], state[1]
        oX, oY = state[2], state[3]
        h2X, h2Y = state[4], state[5]

        # Moves for H1 atom

        # Try and move in every direction, if position changed, add to
        # possible states
        self.movesH1(h1X, h1Y, h2X, h2Y, oX, oY, successors)

        # Same moves for other atoms as well
        # O Atom
        self.movesO(h1X, h1Y, h2X, h2Y, oX, oY, successors)

        # H2 Atom
        self.movesH2(h1X, h1Y, h2X, h2Y, oX, oY, successors)

        return successors

    def movesH2(self, h1X, h1Y, h2X, h2Y, oX, oY, successors):
        newX = moveLeft(h2X, h2Y, h1X, h1Y, oX, oY, self.obstacles)
        if newX != h2X:
            successors["Push H2 Left"] = (h1X, h1Y, oX, oY, newX, h2Y)
        newX = moveRight(h2X, h2Y, h1X, h1Y, oX, oY, self.obstacles)
        if newX != h2X:
            successors["Push H2 Right"] = (h1X, h1Y, oX, oY, newX, h2Y)
        newY = moveUp(h2X, h2Y, h1X, h1Y, oX, oY, self.obstacles)
        if newY != h2Y:
            successors["Push H2 Up"] = (h1X, h1Y, oX, oY, h2X, newY)
        newY = moveDown(h2X, h2Y, h1X, h1Y, oX, oY, self.obstacles)
        if newY != h2Y:
            successors["Push H2 Down"] = (h1X, h1Y, oX, oY, h2X, newY)

    def movesO(self, h1X, h1Y, h2X, h2Y, oX, oY, successors):
        newX = moveLeft(oX, oY, h1X, h1Y, h2X, h2Y, self.obstacles)
        if newX != oX:
            successors["Push O Left"] = (h1X, h1Y, newX, oY, h2X, h2Y)
        newX = moveRight(oX, oY, h1X, h1Y, h2X, h2Y, self.obstacles)
        if newX != oX:
            successors["Push O Right"] = (h1X, h1Y, newX, oY, h2X, h2Y)
        newY = moveUp(oX, oY, h1X, h1Y, h2X, h2Y, self.obstacles)
        if newY != oY:
            successors["Push O Up"] = (h1X, h1Y, oX, newY, h2X, h2Y)
        newY = moveDown(oX, oY, h1X, h1Y, h2X, h2Y, self.obstacles)
        if newY != oY:
            successors["Push O Down"] = (h1X, h1Y, oX, newY, h2X, h2Y)

    def movesH1(self, h1X, h1Y, h2X, h2Y, oX, oY, successors):
        newX = moveLeft(h1X, h1Y, oX, oY, h2X, h2Y, self.obstacles)
        if newX != h1X:
            successors["Push H1 Left"] = (newX, h1Y, oX, oY, h2X, h2Y)
        newX = moveRight(h1X, h1Y, oX, oY, h2X, h2Y, self.obstacles)
        if newX != h1X:
            successors["Push H1 Right"] = (newX, h1Y, oX, oY, h2X, h2Y)
        newY = moveUp(h1X, h1Y, oX, oY, h2X, h2Y, self.obstacles)
        if newY != h1Y:
            successors["Push H1 Up"] = (h1X, newY, oX, oY, h2X, h2Y)
        newY = moveDown(h1X, h1Y, oX, oY, h2X, h2Y, self.obstacles)
        if newY != h1Y:
            successors["Push H1 Down"] = (h1X, newY, oX, oY, h2X, h2Y)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] == state[3] == state[5] \
            and state[0] + 1 == state[2] \
            and state[2] + 1 == state[4]


if __name__ == '__main__':
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]

    h1_position = [2, 1]  # ->
    h2_position = [2, 6]  # <-
    o_position = [7, 2]

    molecule = Molecule(obstacles_list,
                        (h1_position[0], h1_position[1],
                         o_position[0], o_position[1],
                         h2_position[0], h2_position[1]))

    result = breadth_first_graph_search(molecule)
    for solution in result.solution():
        print(solution)