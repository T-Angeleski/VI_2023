from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def block_movement(block, gridY):
    if block[2] == 1:  # Up
        if block[1] == gridY - 1:  # If at ceiling
            block[2] = 0  # Switch to down movement
            block[1] -= 1
        else:
            block[1] += 1
    else:  # Down
        if block[1] == 0:
            block[2] = 1
            block[1] += 1
        else:
            block[1] -= 1


class Explorer(Problem):

    def __init__(self, blocks, initial, goal=None):
        super().__init__(initial, goal)
        self.block1 = blocks[0]
        self.block2 = blocks[1]
        self.grid_size = (8, 6)

    def successor(self, state):
        """
        :param state: Given state
        :return: {action: state} available from given state
        :rtype: dict
        """

        successors = {}

        manX = state[0]
        manY = state[1]

        gridX = self.grid_size[0]
        gridY = self.grid_size[1]

        block_movement(block1, gridY)
        block_movement(block2, gridY)

        blocks = [[self.block1[0], self.block1[1], self.block1[2]],
                  [self.block2[0], self.block2[1], self.block2[2]]]

        # Actions
        # Right movement
        if manX < gridX - 1 and [manX + 1, manY] not in blocks:
            successors["Move Right"] = (manX + 1, manY)

        # Left
        if manX > 0 and [manX - 1, manY] not in blocks:
            successors["Move Left"] = (manX - 1, manY)

        # Up
        if manY < gridY - 1 and [manX, manY + 1] not in blocks:
            successors["Move Up"] = (manX, manY + 1)

        # Down
        if manY > 0 and [manX, manY - 1] not in blocks:
            successors["Move Down"] = (manX, manY - 1)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return (state[0], state[1]) == goalState


if __name__ == '__main__':
    goalState = (7, 4)  # House
    startState = (0, 2)  # Explorer
    block1 = [2, 5, 0]  # 0 Down movement
    block2 = [5, 0, 1]  # 1 Up movement

    explorer = Explorer([block1, block2], (startState[0], startState[1]),
                        goalState)

    print(breadth_first_graph_search(explorer).solution())
    print(breadth_first_graph_search(explorer).solve())