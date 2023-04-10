import itertools

from constraint import *

# def getSum(list):
# 	sum = 0
# 	for val, name in list:
# 		sum += val
# 	return sum
#
#
# def findOptimal(leaders, members):
# 	# [(32.2, 'K'), (27.4, 'L'), (24.6, 'M'), (14.9, 'N'), (13.2, 'O')]
# 	allPossible = []
# 	sum = 0
# 	for val, name in leaders:
# 		sum = val
# 		newGroup = []
# 		for subset in itertools.combinations(members, 5):
# 			sum = val
# 			# ((20.3, 'F'), (15.5, 'G'), (14.1, 'H'), (12.5, 'I'), (11.5, 'J'))
# 			sum += getSum(subset)
# 			newGroup = list(subset)
#
# 			if sum <= 100:
# 				newGroup.append((val, name))
# 				allPossible.append(newGroup)
#
# 	result = findMax(allPossible)
# 	return result
#
#
# def findMax(possible):
# 	max = 0
# 	res = ...
# 	for combination in possible:
# 		sum = 0
# 		sum += getSum(combination)
# 		if sum > max:
# 			max = sum
# 			res = combination
# 	return res
#


if __name__ == '__main__':
	n = int(input())
	members = dict()
	domainMembers = list()
	for i in range(n):
		line = input().split(" ")
		weight, name = line[0], line[1]
		weightF = float(weight)
		members[weightF] = name
		domainMembers.append(weightF)

	m = int(input())
	leaders = dict()
	domainLeaders = list()
	for i in range(m):
		line = input().split(" ")
		weight, name = line[0], line[1]
		weightF = float(weight)
		leaders[weightF] = name
		domainLeaders.append(weightF)

	problem = Problem(BacktrackingSolver())
	varParticipants = ["1", "2", "3", "4", "5"]
	varLeader = ["Team leader"]

	problem.addVariables(varLeader, domainLeaders)
	problem.addVariables(varParticipants, domainMembers)

	problem.addConstraint(MaxSumConstraint(100))
	problem.addConstraint(AllDifferentConstraint())

	solutions = problem.getSolutions()
	# Printing
	solutions.sort(key=lambda x: sum(x.values()))
	solution = solutions[-1]

	totalScore = 0
	for name, val in solution.items():
		totalScore += val

	print(f"Total score: {round(totalScore, 1)}")
	print(f"Team leader: {leaders[solution['Team leader']]}")
	for i in range(5):
		print(f"Participant {i + 1}: {members[solution[str(i + 1)]]}")
# res = findOptimal(leaders, members)
#
# totalScore = getSum(res)
# leader = res[-1][1]
# print(f"Total score: {totalScore}")
# print(f"Team leader: {leader}")
# for i in range(5):
# 	print(f"Participant {i + 1}: {res[i][1]}")