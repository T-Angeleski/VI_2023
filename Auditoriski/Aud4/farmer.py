from searching_framework.utils import Problem
from searching_framework.informed_search import *


class Farmer(Problem):
	def __init__(self, initial, goal=None):
		super().__init__(initial, goal)

	def successor(self, state):
		succ = dict()

		# State = ("w","w","w","w") w/e side of river
		# Farmer, cabbage, goat, wolf

		newFarmer = "w" if state[0] == "e" else "e"
		cabbage, goat, wolf = state[1:]

		newState = (newFarmer, cabbage, goat, wolf)
		if Farmer.check_valid(newState):
			succ["Only farmer crosses"] = newState

		# Move farmer and cabbage
		newCabbage = "w" if state[1] == "e" else "e"
		newState = (newFarmer, newCabbage, goat, wolf)
		if Farmer.check_valid(newState):
			succ["Farmer and cabbage cross"] = newState

		# Move farmer and goat
		newGoat = "w" if state[2] == "e" else "e"
		newState = (newFarmer, cabbage, newGoat, wolf)
		if Farmer.check_valid(newState):
			succ["Farmer and goat cross"] = newState

		# Move farmer and wolf
		newWolf = "w" if state[3] == "e" else "e"
		newState = (newFarmer, cabbage, goat, newWolf)
		if Farmer.check_valid(newState):
			succ["Farmer and wolf cross"] = newState

		return succ

	@staticmethod
	def check_valid(state):
		farmer, cabbage, goat, wolf = state

		if goat == wolf and goat != farmer: return False
		if goat == cabbage and goat != farmer: return False
		return True

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		return self.successor(state)[action]

	def h(self, node):
		value = 0
		for x, y in zip(node.state, ("w", "w", "w", "w")):
			if x != y:
				value += 1

		return value


if __name__ == '__main__':
	start_state = ("e", "e", "e", "e")
	goal_state = ("w", "w", "w", "w")

	farmer = Farmer(start_state, goal_state)
	solve1 = astar_search(farmer)
	print(solve1.solve())
	for line in solve1.solution():
		print(line)