from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def move(block, pillars, index):
	pillars[index].append(block)
	return pillars


def check_valid(pillars):
	for pillar in pillars:
		for i in range(len(pillar) - 1):
			if pillar[i] < pillar[i + 1]: return False
	return True


def convertTuple(newState, num):
	group = []
	res = []
	for j in newState:
		for num in j:
			group.append(num)
		res.append(tuple(group))
		group.clear()
	tupleState = tuple(res)
	return tupleState


class Hanoi(Problem):

	def __init__(self, initial, goal=None):
		super().__init__(initial, goal)

	def successor(self, state):
		succ = dict()

		pillars = []
		for block in state:
			pillars.append(list(block))
		num = len(pillars)

		# Try and move top block from each pillar
		for i in range(num):
			if len(pillars[i]) != 0:
				for j in range(num):
					tmpPillars = list(state)  #TODO
					top = tmpPillars[i].pop()
					newState = move(top, tmpPillars, j)
					tupleState = convertTuple(newState, num)
					if tupleState != state and check_valid(newState):
						succ[f"MOVE TOP BLOCK FROM PILLAR " \
						     f"{i + 1} TO " \
						     f"PILLAR" \
						     f" {j + 1}."] = tupleState

		# for pillar in pillars:
		# 	if len(pillar) != 0:
		# 		for i in range(num):
		# 			tmpPillars = pillars.copy()
		# 			top = tmpPillars[tmpPillars.index(pillar)].pop()
		# 			newState = move(top, tmpPillars, i)
		# 			num, tupleState = convertTuple(newState, num)
		# 			print(f"Pillar {pillars.index(pillar) + 1}")
		# 			print(f"To {i + 1}")
		# 			if tupleState != state and check_valid(newState):
		# 				succ[f"MOVE TOP BLOCK FROM PILLAR " \
		# 				     f"{pillars.index(pillar) + 1} TO " \
		# 				     f"PILLAR" \
		# 				     f" {i + 1}."] = tupleState

		return succ

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		return self.successor(state)[action]


if __name__ == '__main__':
	starter = input().split(";")
	blocks = []
	group = []
	for block in starter:
		for num in block.split(","):
			if num != "":
				group.append(int(num))
		blocks.append(tuple(group))
		group.clear()

	goalInput = tuple(input().split(";"))
	goal = []
	for block in goalInput:
		for num in block.split(","):
			if num != "":
				group.append(int(num))
		goal.append(tuple(group))
		group.clear()

	problem = Hanoi(tuple(blocks), tuple(goal))
	solve = breadth_first_graph_search(problem).solve()
	print(solve)