from searching_framework.utils import Problem
from searching_framework.informed_search import *
from searching_framework.uninformed_search import *


def moveBlock(block):
	direction = block[2]

	if direction == "up":
		if block[1] == 5:
			block[2] = "down"
			block[1] -= 1
		else:
			block[1] += 1
	else:
		if block[1] == 0:
			block[2] = "up"
			block[1] += 1
		else:
			block[1] -= 1
	return block


def moveExplorer(x, y, direction):
	newPos = None
	if direction == "up":
		newPos = (x, y + 1)
	elif direction == "down":
		newPos = (x, y - 1)
	elif direction == "right":
		newPos = (x + 1, y)
	elif direction == "left":
		newPos = (x - 1, y)

	return newPos


def check_valid(state, blocks):
	x, y = state[0], state[1]
	block1 = (blocks[0][0], blocks[0][1])
	block2 = (blocks[1][0], blocks[1][1])

	if x < 0 or x > 7: return False
	if y < 0 or y > 5: return False
	if state == block1: return False
	if state == block2: return False

	return True


class Explorer(Problem):

	def __init__(self, blocks, initial, goal=None):
		super().__init__(initial, goal)
		self.blocks = blocks

	def successor(self, state):
		succ = dict()

		# Blocks move every turn, regardless of state
		block1, block2 = self.blocks
		block1 = moveBlock(list(block1))
		block2 = moveBlock(list(block2))

		x, y = state

		afterMove = moveExplorer(x, y, "up")
		if check_valid(afterMove, (block1, block2)):
			succ["Move up"] = afterMove

		afterMove = moveExplorer(x, y, "down")
		if check_valid(afterMove, (block1, block2)):
			succ["Move down"] = afterMove

		afterMove = moveExplorer(x, y, "right")
		if check_valid(afterMove, (block1, block2)):
			succ["Move right"] = afterMove

		afterMove = moveExplorer(x, y, "left")
		if check_valid(afterMove, (block1, block2)):
			succ["Move left"] = afterMove

		return succ

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		return self.successor(state)[action]

	def h(self, node):
		x, y = node.state
		goalX, goalY = self.goal

		return abs(x - goalX) + abs(y - goalY)


if __name__ == '__main__':
	explorer = (2, 3)
	house = (7, 4)
	block1 = (2, 5, "down")
	block2 = (5, 0, "up")
	blocks = (block1, block2)

	problem = Explorer(blocks, explorer, house)
	solution = astar_search(problem).solution()
	print(solution)