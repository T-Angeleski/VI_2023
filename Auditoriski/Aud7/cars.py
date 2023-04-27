import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB


def readFile(fileName):
	with open(fileName) as doc:
		csv_reader = csv.reader(doc, delimiter=",")
		dataset = list(csv_reader)[1:]

	return dataset


if __name__ == '__main__':
	dataset = readFile("car.csv")

	# Get all except last row
	encoder = OrdinalEncoder()
	# Encode all elements
	encoder.fit([row[:-1] for row in dataset])

	# Split dataset
	trainSet = dataset[:int(0.75 * len(dataset))]  # First 75%
	testSet = dataset[int(0.75 * len(dataset)):]

	# Train attributes and class
	trainX = [row[:-1] for row in trainSet]
	trainY = [row[-1] for row in trainSet]

	# attributes are string, need to encode
	trainX = encoder.transform(trainX)

	# Test
	testX = [row[:-1] for row in testSet]
	testY = [row[-1] for row in testSet]
	testX = encoder.transform(testX)

	# Classify
	classifier = CategoricalNB()
	classifier.fit(trainX, trainY)

	# Test accuracy
	correct = 0

	for i in range(len(testSet)):
		# f(x) = ?
		predictedClass = classifier.predict([testX[i]])[0]  # in list out list
		trueClass = testY[i]
		# print(predictedClass, trueClass)

		if predictedClass == trueClass: correct += 1

	accuracy = correct / len(testSet)
	print(f"Accuracy is {accuracy:.3f}")

	print()