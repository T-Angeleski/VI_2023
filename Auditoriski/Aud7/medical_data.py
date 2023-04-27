import csv
from sklearn.naive_bayes import GaussianNB


def readFile(fileName):
	with open(fileName) as doc:
		reader = csv.reader(doc, delimiter=",")
		dataset = list(reader)[1:]
	# Dataset is string
	dataToInt = []
	for row in dataset:
		rowInt = [int(element) for element in row]
		dataToInt.append(rowInt)
	return dataToInt


if __name__ == '__main__':
	dataset = readFile("medical_data.csv")

	trainSet = dataset[: int(0.8 * len(dataset))]
	testSet = dataset[int(0.8 * len(dataset)):]

	trainX = [row[:-1] for row in trainSet]
	trainY = [row[-1] for row in trainSet]

	testX = [row[:-1] for row in testSet]
	testY = [row[-1] for row in testSet]

	classifier = GaussianNB()
	classifier.fit(trainX, trainY)

	accuracy = 0
	for i in range(len(testSet)):
		predicted = classifier.predict([testX[i]])[0]
		true = testY[i]
		print(f"Predicted: {predicted}, true value is {true}")
		if predicted == true: accuracy += 1

	accuracy = accuracy / len(testSet)
	print(f"Accuracy is {accuracy:.2f}")