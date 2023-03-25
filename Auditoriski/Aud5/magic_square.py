from constraint import *

if __name__ == '__main__':
	problem = Problem()

	variables = [num for num in range(16)]
	domain = range(1, 17)

	problem.addVariables(variables, domain)

	# Sum 34, different number every position
	problem.addConstraint(AllDifferentConstraint(), variables)

	# Rows  0123, 4567, 89..
	for row in range(4):
		toAdd = [row * 4 + i for i in range(4)]
		problem.addConstraint(ExactSumConstraint(34), toAdd)

	# Columns 0,4,8,12
	for col in range(4):
		toAdd = [col + 4 * i for i in range(4)]
		problem.addConstraint(ExactSumConstraint(34), toAdd)

	# Diagonals 0, 5, 10, 15
	problem.addConstraint(ExactSumConstraint(34), range(0, 16, 5))
	# 3,6,9,12
	problem.addConstraint(ExactSumConstraint(34), range(3, 13, 3))

	solution = problem.getSolution()
	for k, v in sorted(solution.items()):
		print(k, v)