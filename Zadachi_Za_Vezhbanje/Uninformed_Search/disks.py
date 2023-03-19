from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class Disks(Problem):

	def __init__(self, size, initial, goal=None):
		super().__init__(initial, goal)
		self.size = size

	def successor(self, state):
		successors = dict()

		disks = state

		for i in range(self.size):
			# Move one right
			if disks[i] == 1000: continue
			if i + 1 < self.size and disks[i + 1] == 1000:
				newArr = list(disks)
				newArr[i + 1] = newArr[i]
				newArr[i] = 1000

				successors[f"D1: Disk {disks[i]}"] = \
					tuple(newArr)

			# Move two right
			if i + 2 < self.size and disks[i + 2] == 1000 \
					and disks[i + 1] != 1000:
				newArr = list(disks)
				newArr[i + 2] = newArr[i]
				newArr[i] = 1000

				successors[f"D2: Disk {disks[i]}"] = \
					tuple(newArr)

			# Move one left
			if i > 0 and disks[i - 1] == 1000:
				newArr = list(disks)
				newArr[i - 1] = newArr[i]
				newArr[i] = 1000

				successors[f"L1: Disk {disks[i]}"] = \
					tuple(newArr)

			# Move two left
			if i > 1 and disks[i - 2] == 1000 \
					and disks[i - 1] != 1000:
				newArr = list(disks)
				newArr[i - 2] = newArr[i]
				newArr[i] = 1000

				successors[f"L2: Disk {disks[i]}"] = \
					tuple(newArr)

		return successors

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		return self.successor(state)[action]


if __name__ == '__main__':
	numDisks = int(input())
	sizeBoard = int(input())
	disks = []

	for i in range(1, sizeBoard + 1):
		disks.append(i) if i <= numDisks else disks.append(1000)

	goalState = sorted(disks, reverse=True)

	problem = Disks(sizeBoard, tuple(disks), tuple(goalState))
	solution = breadth_first_graph_search(problem).solution()
	print(solution)