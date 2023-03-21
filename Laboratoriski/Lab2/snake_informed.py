from searching_framework.utils import Problem
from searching_framework.informed_search import *


def checkEatenApple(snakeHead, greenApples):  # (x, y), [(x,y)...]
	return snakeHead in greenApples


def moveForward(body, head, greenApples):
	direction = head[2]
	afterMove = []
	if direction == "up":
		afterMove = [head[0], head[1] + 1]

	elif direction == "down":
		afterMove = [head[0], head[1] - 1]

	elif direction == "left":
		afterMove = [head[0] - 1, head[1]]

	elif direction == "right":
		afterMove = [head[0] + 1, head[1]]

	if checkEatenApple(tuple(afterMove), tuple(greenApples)):
		greenApples.remove(tuple(afterMove))
	else:
		body.pop(0)

	body.insert(-1, (head[0], head[1]))
	head = (afterMove[0], afterMove[1], direction)
	return body, head, greenApples


def turnLeft(body, head, greenApples):
	direction = head[2]

	if direction == "up":
		return moveForward(body, (head[0], head[1], "left"), greenApples)
	elif direction == "left":
		return moveForward(body, (head[0], head[1], "down"), greenApples)
	elif direction == "down":
		return moveForward(body, (head[0], head[1], "right"), greenApples)
	elif direction == "right":
		return moveForward(body, (head[0], head[1], "up"), greenApples)

	return body, head, greenApples


def turnRight(body, head, greenApples):
	direction = head[2]

	if direction == "up":
		return moveForward(body, (head[0], head[1], "right"), greenApples)
	elif direction == "left":
		return moveForward(body, (head[0], head[1], "up"), greenApples)
	elif direction == "down":
		return moveForward(body, (head[0], head[1], "left"), greenApples)
	elif direction == "right":
		return moveForward(body, (head[0], head[1], "down"), greenApples)
	return body, head, greenApples


def check_valid(state):
	body, head = state[0], state[1]

	if head[0] < 0 or head[0] > 9: return False
	if head[1] < 0 or head[1] > 9: return False
	if head in body: return False

	return True


def manhattan_distance(head, apple):
	return abs(head[0] - apple[0]) + abs(head[1] - apple[1])


class Snake(Problem):

	def __init__(self, initial, goal=None):
		super().__init__(initial, goal)

	def successor(self, state):
		succ = dict()

		body, head, apples = state

		newState = moveForward(list(body), list(head), list(apples))
		if check_valid(newState):
			succ["ProdolzhiPravo"] = \
				(tuple(newState[0]), tuple(newState[1]), tuple(newState[2]))

		newState = turnRight(list(body), list(head), list(apples))
		if check_valid(newState):
			succ["SvrtiDesno"] = \
				(tuple(newState[0]), tuple(newState[1]), tuple(newState[2]))

		newState = turnLeft(list(body), list(head), list(apples))
		if check_valid(newState):
			succ["SvrtiLevo"] = \
				(tuple(newState[0]), tuple(newState[1]), tuple(newState[2]))

		return succ

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		return self.successor(state)[action]

	def goal_test(self, state):
		return len(state[2]) == 0

	def h(self, node):
		head, apples = node.state[1], node.state[2]
		value = 0

		# Get manhattan for all apples on board
		for x, y in apples:
			value += manhattan_distance(head, (x, y))

		return value


if __name__ == '__main__':
	snakeHead = (0, 7, "down")
	snakeBody = ((0, 9), (0, 8))

	n = int(input())
	apples = []
	for i in range(n):
		apples.append(tuple(map(int, input().split(","))))

	problem = Snake((snakeBody, snakeHead, tuple(apples)))
	solve = astar_search(problem).solution()
	print(solve)