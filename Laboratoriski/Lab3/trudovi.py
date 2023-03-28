from constraint import *


def filterTerm(variables, subject):
	return [(k, v) for k, v in variables if v == subject]


def restrictDomain(*args):
	# Args -> current state
	terms = {"T1": 0, "T2": 0, "T3": 0, "T4": 0}
	for arg in args:
		terms[arg] += 1

	for item in terms.values():
		if item > 4: return False
	return True


def printSolution(solution):
	# (paper, subject) : term
	papers = sorted(solution)

	terms = []

	for value in papers:
		terms.append(solution[value])

	# P1 -> P10 -> P2  from sorting,  fix this
	print(f"{papers[0][0]} ({papers[0][1]}): {terms[0]}")
	for i in range(2, len(papers)):
		print(f"{papers[i][0]} ({papers[i][1]}): {terms[i]}")
	print(f"{papers[1][0]} ({papers[1][1]}): {terms[1]}")


if __name__ == '__main__':
	num = int(input())

	papers = dict()

	paper_info = input()
	while paper_info != 'end':
		title, topic = paper_info.split(' ')
		papers[title] = topic
		paper_info = input()

	# Tuka definirajte gi promenlivite
	variables = [item for item in papers.items()]

	domain = [f'T{i + 1}' for i in range(num)]

	problem = Problem(BacktrackingSolver())

	# Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
	problem.addVariables(variables, domain)

	# Tuka dodadete gi ogranichuvanjata
	listAI = filterTerm(variables, "AI")
	listML = filterTerm(variables, "ML")
	listNLP = filterTerm(variables, "NLP")

	# If all are <= 4 and non-empty
	if len(listAI) <= 4 and len(listAI) != 0:
		problem.addConstraint(AllEqualConstraint(), listAI)

	if len(listML) <= 4 and len(listML) != 0:
		problem.addConstraint(AllEqualConstraint(), listML)

	if len(listNLP) <= 4 and len(listNLP) != 0:
		problem.addConstraint(AllEqualConstraint(), listNLP)

	problem.addConstraint(restrictDomain, variables)

	result = problem.getSolution()

	# Tuka dodadete go kodot za pechatenje
	printSolution(result)