from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def moveSnake(snakeHead, snakeBody, redApples, greenApples, direction):
    # head = [x,y,direction]
    if direction == "north" and snakeHead[2] != "south":
        if snakeHead[1] + 1 < 10 \
                and (snakeHead[0], snakeHead[1] + 1) not in redApples \
                and (snakeHead[0], snakeHead[1] + 1) not in snakeBody:
            # Valid move
            # Check if on green apple
            if checkGreenApple([snakeHead[0], snakeHead[1] + 1], greenApples):
                snakeBody.insert(-1, (snakeHead[0], snakeHead[1]))
                snakeHead = [snakeHead[0], snakeHead[1] + 1, direction]
                greenApples.remove((snakeHead[0], snakeHead[1]))
                return snakeBody, snakeHead, greenApples
            else:
                snakeBody.pop(0)
                snakeBody.insert(-1, (snakeHead[0], snakeHead[1]))
                snakeHead = [snakeHead[0], snakeHead[1] + 1, direction]
                return snakeBody, snakeHead, greenApples
        else:
            return snakeBody, snakeHead, greenApples

    elif direction == "east" and snakeHead[2] != "west":
        if snakeHead[0] + 1 < 10 \
                and (snakeHead[0] + 1, snakeHead[1]) not in redApples \
                and (snakeHead[0] + 1, snakeHead[1]) not in snakeBody:
            if checkGreenApple([snakeHead[0] + 1, snakeHead[1]], greenApples):
                snakeBody.insert(-1, (snakeHead[0], snakeHead[1]))
                snakeHead = [snakeHead[0] + 1, snakeHead[1], direction]
                greenApples.remove((snakeHead[0], snakeHead[1]))
                return snakeBody, snakeHead, greenApples
            else:
                snakeBody.pop(0)
                snakeBody.insert(-1, (snakeHead[0], snakeHead[1]))
                snakeHead = [snakeHead[0] + 1, snakeHead[1], direction]
                return snakeBody, snakeHead, greenApples
        else:
            return snakeBody, snakeHead, greenApples

    elif direction == "south" and snakeHead[2] != "north":
        if snakeHead[1] - 1 < 10 \
                and (snakeHead[0], snakeHead[1] - 1) not in redApples \
                and (snakeHead[0], snakeHead[1] - 1) not in snakeBody:
            if checkGreenApple([snakeHead[0], snakeHead[1] - 1], greenApples):
                snakeBody.insert(-1, (snakeHead[0], snakeHead[1]))
                snakeHead = [snakeHead[0], snakeHead[1] - 1, direction]
                greenApples.remove((snakeHead[0], snakeHead[1]))
                return snakeBody, snakeHead, greenApples
            else:
                snakeBody.pop(0)
                snakeBody.insert(-1, (snakeHead[0], snakeHead[1]))
                snakeHead = [snakeHead[0], snakeHead[1] - 1, direction]
                return snakeBody, snakeHead, greenApples
        else:
            return snakeBody, snakeHead, greenApples

    elif direction == "west" and snakeHead[2] != "east":
        if snakeHead[0] - 1 >= 0 \
                and (snakeHead[0] - 1, snakeHead[1]) not in redApples \
                and (snakeHead[0] - 1, snakeHead[1]) not in snakeBody:
            if checkGreenApple([snakeHead[0] - 1, snakeHead[1]], greenApples):
                snakeBody.insert(-1, (snakeHead[0], snakeHead[1]))
                snakeHead = [snakeHead[0] - 1, snakeHead[1], direction]
                greenApples.remove((snakeHead[0], snakeHead[1]))
                return snakeBody, snakeHead, greenApples
            else:
                snakeBody.pop(0)
                snakeBody.insert(-1, (snakeHead[0], snakeHead[1]))
                snakeHead = [snakeHead[0] - 1, snakeHead[1], direction]
                return snakeBody, snakeHead, greenApples
        else:
            return snakeBody, snakeHead, greenApples

    return snakeBody, snakeHead, greenApples


def checkGreenApple(snakeHead, greenApples):
    return (snakeHead[0], snakeHead[1]) in greenApples


class Snake(Problem):
    def __init__(self, redApples, initial, goal=None):
        super().__init__(initial, goal)
        self.redApples = redApples

    def successor(self, state):
        successors = {}
        # state = (snakeBody, snakeHead, greenApples)
        # Initialize current values
        snake_body = list(state[0])
        snake_head = list(state[1])
        green_apples = list(state[2])

        # Possible moves for snake: Go forward, turn right(and move), turn left
        # Moves for north facing
        if snake_head[2] == "north":
            # Turn left
            newPos = moveSnake(snake_head, snake_body,
                               self.redApples,
                               green_apples, "west")
            if newPos[1] != snake_head:
                successors["Turn left"] = (tuple(newPos[0]), tuple(newPos[1]),
                                           tuple(newPos[2]))

            # Forward
            newPos = moveSnake(snake_head, snake_body,
                               self.redApples,
                               green_apples, "north")
            if newPos[1] != snake_head:
                successors["Go forward"] = (tuple(newPos[0]), tuple(newPos[1]),
                                            tuple(newPos[2]))
            # Turn right
            newPos = moveSnake(snake_head, snake_body,
                               self.redApples,
                               green_apples, "east")
            if newPos[1] != snake_head:
                successors["Turn right"] = (tuple(newPos[0]), tuple(newPos[1]),
                                            tuple(newPos[2]))

        if snake_head[2] == "east":
            # Turn left
            newPos = moveSnake(snake_head, snake_body,
                               self.redApples,
                               green_apples, "north")
            if newPos[1] != snake_head:
                successors["Turn left"] = (tuple(newPos[0]), tuple(newPos[1]),
                                           tuple(newPos[2]))

            # Forward
            newPos = moveSnake(snake_head, snake_body,
                               self.redApples,
                               green_apples, "east")
            if newPos[1] != snake_head:
                successors["Go forward"] = (tuple(newPos[0]), tuple(newPos[1]),
                                            tuple(newPos[2]))

            # Turn right
            newPos = moveSnake(snake_head, snake_body,
                               self.redApples,
                               green_apples, "south")
            if newPos[1] != snake_head:
                successors["Turn right"] = (tuple(newPos[0]), tuple(newPos[1]),
                                            tuple(newPos[2]))
        if snake_head[2] == "south":
            # Turn left
            newPos = moveSnake(snake_head, snake_body,
                               self.redApples,
                               green_apples, "east")
            if newPos[1] != snake_head:
                successors["Turn left"] = (tuple(newPos[0]), tuple(newPos[1]),
                                           tuple(newPos[2]))

            # Forward
            newPos = moveSnake(snake_head, snake_body,
                               self.redApples,
                               green_apples, "south")
            if newPos[1] != snake_head:
                successors["Go forward"] = (tuple(newPos[0]), tuple(newPos[1]),
                                            tuple(newPos[2]))

            # Turn right
            newPos = moveSnake(snake_head, snake_body,
                               self.redApples,
                               green_apples, "west")
            if newPos[1] != snake_head:
                successors["Turn right"] = (tuple(newPos[0]), tuple(newPos[1]),
                                            tuple(newPos[2]))

        if snake_head[2] == "west":
            # Turn left
            newPos = moveSnake(snake_head, snake_body,
                               self.redApples,
                               green_apples, "south")
            if newPos[1] != snake_head:
                successors["Turn left"] = (tuple(newPos[0]), tuple(newPos[1]),
                                           tuple(newPos[2]))

            # Forward
            newPos = moveSnake(snake_head, snake_body,
                               self.redApples,
                               green_apples, "west")
            if newPos[1] != snake_head:
                successors["Go forward"] = (tuple(newPos[0]), tuple(newPos[1]),
                                            tuple(newPos[2]))

            # Turn right
            newPos = moveSnake(snake_head, snake_body,
                               self.redApples,
                               green_apples, "north")
            if newPos[1] != snake_head:
                successors["Turn right"] = (tuple(newPos[0]), tuple(newPos[1]),
                                            tuple(newPos[2]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0


if __name__ == '__main__':
    """ Input:        
    5         Green Apples
    6,9
    2,7
    9,5
    2,3
    4,3
    4         Red apples
    4,6
    6,5
    3,3
    6,8
    """
    snakeBody = ((0, 9), (0, 8))
    snakeHead = (0, 7, "south")  # Facing direction

    numGreen = int(input())
    greenApples = []
    redApples = []
    for line in range(numGreen):
        greenApples.append(tuple(map(int, input().split(","))))

    numRed = int(input())
    for line in range(numRed):
        redApples.append(tuple(map(int, input().split(","))))

    problem = Snake(redApples, (snakeBody, snakeHead, tuple(greenApples)))
    solve = breadth_first_graph_search(problem)

    solution = "['SvrtiLevo', 'ProdolzhiPravo', 'SvrtiDesno', " \
               "'ProdolzhiPravo', " \
               "'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', " \
               "'SvrtiLevo', " \
               "'ProdolzhiPravo', 'Svrti Levo', 'ProdolzhiPravo', " \
               "'SvrtiDesno', " \
               "'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', " \
               "'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', " \
               "'ProdolzhiPravo', " \
               "'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', " \
               "'ProdolzhiPravo', " \
               "'ProdolzhiPravo']"

    for move in solve.solution():
        print(move)