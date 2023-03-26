from constraint import *


def filterLessThanTerm(variables, subject):
	return [(k, v) for k, v in variables if v == subject]


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
	AI, ML, NLP = 0, 0, 0
	for k, v in variables:
		if v == "AI": AI += 1
		if v == "ML": ML += 1
		if v == "NLP": NLP += 1

	if AI <= num:
		filtered = filterLessThanTerm(variables, "AI")
		problem.addConstraint(AllEqualConstraint(), filtered)

	if ML <= num:
		filtered = filterLessThanTerm(variables, "ML")
		problem.addConstraint(AllEqualConstraint(), filtered)

	if NLP <= num:
		filtered = filterLessThanTerm(variables, "NLP")
		problem.addConstraint(AllEqualConstraint(), filtered)

	result = problem.getSolution()
	for k, v in result.items():
		print(k, v)
# Tuka dodadete go kodot za pechatenje