from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def knight1(x, y, bx, by):
    # Up up left
    if 0 < x - 1 < 8 and 0 < y + 2 < 8 and [x - 1, y + 2] != [bx, by]:
        return x - 1, y + 2
    else:
        return x, y


def knight2(x, y, bx, by):
    # Up up right
    if 0 < x + 1 < 8 and 0 < y + 2 < 8 and [x + 1, y + 2] != [bx, by]:
        return x + 1, y + 2
    else:
        return x, y


def knight3(x, y, bx, by):
    # Right, Right Up
    if 0 < x + 2 < 8 and 0 < y + 1 < 8 and [x + 2, y + 1] != [bx, by]:
        return x + 2, y + 1
    else:
        return x, y


def knight4(x, y, bx, by):
    # Right, Right Down
    if 0 < x + 2 < 8 and 0 < y - 1 < 8 and [x + 2, y - 1] != [bx, by]:
        return x + 2, y - 1
    else:
        return x, y


def knight5(x, y, bx, by):
    # Down, Down, Right
    if 0 < x + 1 < 8 and 0 < y - 2 < 8 and [x + 1, y - 2] != [bx, by]:
        return x + 1, y - 2
    else:
        return x, y


def knight6(x, y, bx, by):
    # down, down, left
    if 0 < x + 1 < 8 and 0 < y - 2 < 8 and [x - 1, y - 2] != [bx, by]:
        return x - 1, y - 2
    else:
        return x, y


def knight7(x, y, bx, by):
    # Left, left, down
    if 0 < x - 2 < 8 and 0 < y - 1 < 8 and [x - 2, y - 1] != [bx, by]:
        return x - 2, y - 1
    else:
        return x, y


def knight8(x, y, bx, by):
    # Left, left, up
    if 0 < x - 2 < 8 and 0 < y + 1 < 8 and [x - 2, y + 2] != [bx, by]:
        return x - 2, y + 1
    else:
        return x, y


def bishop1(x, y, kx, ky):  # up left
    if 0 < x - 1 < 8 and 0 < y + 1 < 8 and [x - 1, y + 1] != [kx, ky]:
        return x - 1, y + 1
    else:
        return x, y


def bishop2(x, y, kx, ky):  # up right
    if 0 < x + 1 < 8 and 0 < y + 1 < 8 and [x + 1, y + 1] != [kx, ky]:
        return x + 1, y + 1
    else:
        return x, y


def bishop3(x, y, kx, ky):  # down left
    if 0 < x - 1 < 8 and 0 < y - 1 < 8 and [x - 1, y - 1] != [kx, ky]:
        return x - 1, y - 1
    else:
        return x, y


def bishop4(x, y, kx, ky):  # down right
    if 0 < x + 1 < 8 and 0 < y - 1 < 8 and [x + 1, y - 1] != [kx, ky]:
        return x + 1, y - 1
    else:
        return x, y


class Stars(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = {}

        knightX, knightY = state[0], state[1]
        bishopX, bishopY = state[2], state[3]
        current_stars = state[-1]

        # Check all moves for knight
        move = knight1(knightX, knightY, bishopX, bishopY)
        if move != [knightX, knightY]:
            successors["K Up Up Left"] = \
                (move[0], move[1], bishopX, bishopY,
                 tuple([s for s in current_stars if move[0] != s[0]
                        or move[1] != s[1]]))
        move = knight2(knightX, knightY, bishopX, bishopY)
        if move != [knightX, knightY]:
            successors["K Up Up Right"] = \
                (move[0], move[1], bishopX, bishopY,
                 tuple([s for s in current_stars if move[0] != s[0]
                        or move[1] != s[1]]))
        move = knight3(knightX, knightY, bishopX, bishopY)
        if move != [knightX, knightY]:
            successors["K Right Right Up"] = \
                (move[0], move[1], bishopX, bishopY,
                 tuple([s for s in current_stars if move[0] != s[0]
                        or move[1] != s[1]]))
        move = knight4(knightX, knightY, bishopX, bishopY)
        if move != [knightX, knightY]:
            successors["K Right Right Down"] = \
                (move[0], move[1], bishopX, bishopY,
                 tuple([s for s in current_stars if move[0] != s[0]
                        or move[1] != s[1]]))
        move = knight5(knightX, knightY, bishopX, bishopY)
        if move != [knightX, knightY]:
            successors["K Down Down Right"] = \
                (move[0], move[1], bishopX, bishopY,
                 tuple([s for s in current_stars if move[0] != s[0]
                        or move[1] != s[1]]))
        move = knight6(knightX, knightY, bishopX, bishopY)
        if move != [knightX, knightY]:
            successors["K Down Down Left"] = \
                (move[0], move[1], bishopX, bishopY,
                 tuple([s for s in current_stars if move[0] != s[0]
                        or move[1] != s[1]]))
        move = knight7(knightX, knightY, bishopX, bishopY)
        if move != [knightX, knightY]:
            successors["K Left Left Down"] = \
                (move[0], move[1], bishopX, bishopY,
                 tuple([s for s in current_stars if move[0] != s[0]
                        or move[1] != s[1]]))
        move = knight8(knightX, knightY, bishopX, bishopY)
        if move != [knightX, knightY]:
            successors["K Left Left Up"] = \
                (move[0], move[1], bishopX, bishopY,
                 tuple([s for s in current_stars if move[0] != s[0]
                        or move[1] != s[1]]))

        move = bishop1(bishopX, bishopY, knightX, knightY)
        if move != [bishopX, bishopY]:
            successors["B Up-Left"] = \
                (knightX, knightY, move[0], move[1],
                 tuple([s for s in current_stars if move[0] != s[0]
                        or move[1] != s[1]]))
        move = bishop2(bishopX, bishopY, knightX, knightY)
        if move != [bishopX, bishopY]:
            successors["B Up-Right"] = \
                (knightX, knightY, move[0], move[1],
                 tuple([s for s in current_stars if move[0] != s[0]
                        or move[1] != s[1]]))
        move = bishop3(bishopX, bishopY, knightX, knightY)
        if move != [bishopX, bishopY]:
            successors["B Down-Left"] = \
                (knightX, knightY, move[0], move[1],
                 tuple([s for s in current_stars if move[0] != s[0]
                        or move[1] != s[1]]))
        move = bishop4(bishopX, bishopY, knightX, knightY)
        if move != [bishopX, bishopY]:
            successors["B Down-Right"] = \
                (knightX, knightY, move[0], move[1],
                 tuple([s for s in current_stars if move[0] != s[0]
                        or move[1] != s[1]]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        # No more stars left to collect
        return len(state[-1]) == 0


if __name__ == '__main__':
    knight = [2, 5]
    bishop = [5, 1]
    stars_pos = ((1, 1), (4, 3), (6, 6))

    # TODO time taken
    problem = Stars((knight[0], knight[1], bishop[0], bishop[1],
                     stars_pos))
    result = breadth_first_graph_search(problem)

    for solution in result.solution():
        print(solution)