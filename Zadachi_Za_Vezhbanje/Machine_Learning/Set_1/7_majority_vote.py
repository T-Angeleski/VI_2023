from sklearn.tree import DecisionTreeClassifier

dataset = [[6.3, 2.3, 4.4, 1.3, 2],
           [6.4, 2.8, 5.6, 2.1, 0],
           [5.1, 3.3, 1.7, 0.5, 1],
           [5.1, 3.5, 1.4, 0.2, 1],
           [4.6, 3.1, 1.5, 0.2, 1],
           [5.8, 2.7, 5.1, 1.9, 0],
           [5.5, 3.5, 1.3, 0.2, 1],
           [5.7, 2.6, 3.5, 1.0, 2],
           [5.0, 3.5, 1.3, 0.3, 1],
           [6.3, 2.5, 5.0, 1.9, 0],
           [6.2, 2.2, 4.5, 1.5, 2],
           [5.0, 3.4, 1.6, 0.4, 1],
           [5.7, 4.4, 1.5, 0.4, 1],
           [4.9, 2.4, 3.3, 1.0, 2],
           [4.4, 2.9, 1.4, 0.2, 1],
           [5.5, 2.4, 3.7, 1.0, 2],
           [5.6, 2.5, 3.9, 1.1, 2],
           [5.6, 2.8, 4.9, 2.0, 0],
           [4.8, 3.4, 1.6, 0.2, 1],
           [5.6, 3.0, 4.5, 1.5, 2],
           [6.0, 3.0, 4.8, 1.8, 0],
           [6.3, 3.3, 4.7, 1.6, 2],
           [4.8, 3.0, 1.4, 0.1, 1],
           [7.9, 3.8, 6.4, 2.0, 0],
           [4.9, 3.0, 1.4, 0.2, 1],
           [4.3, 3.0, 1.1, 0.1, 1],
           [6.8, 3.2, 5.9, 2.3, 0],
           [5.6, 2.7, 4.2, 1.3, 2],
           [5.2, 4.1, 1.5, 0.1, 1],
           [6.2, 2.9, 4.3, 1.3, 2],
           [6.5, 2.8, 4.6, 1.5, 2],
           [5.4, 3.9, 1.3, 0.4, 1],
           [5.8, 2.6, 4.0, 1.2, 2],
           [5.4, 3.7, 1.5, 0.2, 1],
           [4.5, 2.3, 1.3, 0.3, 1],
           [6.3, 3.4, 5.6, 2.4, 0],
           [6.2, 3.4, 5.4, 2.3, 0],
           [5.7, 2.5, 5.0, 2.0, 0],
           [5.8, 2.7, 3.9, 1.2, 2],
           [6.4, 2.7, 5.3, 1.9, 0],
           [5.1, 3.8, 1.6, 0.2, 1],
           [6.3, 2.5, 4.9, 1.5, 2],
           [7.7, 2.8, 6.7, 2.0, 0],
           [5.1, 3.5, 1.4, 0.3, 1],
           [6.8, 2.8, 4.8, 1.4, 2],
           [6.1, 3.0, 4.6, 1.4, 2],
           [5.5, 4.2, 1.4, 0.2, 1],
           [5.0, 2.0, 3.5, 1.0, 2],
           [7.7, 3.0, 6.1, 2.3, 0],
           [5.1, 2.5, 3.0, 1.1, 2],
           [5.9, 3.0, 5.1, 1.8, 0],
           [7.2, 3.2, 6.0, 1.8, 0],
           [4.9, 3.1, 1.5, 0.2, 1],
           [5.7, 3.0, 4.2, 1.2, 2],
           [6.1, 2.9, 4.7, 1.4, 2],
           [5.0, 3.2, 1.2, 0.2, 1],
           [4.4, 3.2, 1.3, 0.2, 1],
           [6.7, 3.1, 5.6, 2.4, 0],
           [4.6, 3.6, 1.0, 0.2, 1],
           [5.1, 3.4, 1.5, 0.2, 1],
           [5.2, 2.7, 3.9, 1.4, 2],
           [6.4, 3.1, 5.5, 1.8, 0],
           [7.4, 2.8, 6.1, 1.9, 0],
           [4.9, 3.1, 1.5, 0.1, 1],
           [5.0, 3.5, 1.6, 0.6, 1],
           [6.7, 3.1, 4.7, 1.5, 2],
           [6.4, 3.2, 5.3, 2.3, 0],
           [6.3, 2.7, 4.9, 1.8, 0],
           [5.8, 4.0, 1.2, 0.2, 1],
           [6.9, 3.1, 5.4, 2.1, 0],
           [5.9, 3.2, 4.8, 1.8, 2],
           [6.6, 2.9, 4.6, 1.3, 2],
           [6.1, 2.8, 4.0, 1.3, 2],
           [7.7, 2.6, 6.9, 2.3, 0],
           [5.5, 2.6, 4.4, 1.2, 2],
           [6.3, 2.9, 5.6, 1.8, 0],
           [7.2, 3.0, 5.8, 1.6, 0],
           [6.5, 3.0, 5.8, 2.2, 0],
           [5.4, 3.9, 1.7, 0.4, 1],
           [6.5, 3.2, 5.1, 2.0, 0],
           [5.9, 3.0, 4.2, 1.5, 2],
           [5.1, 3.7, 1.5, 0.4, 1],
           [5.7, 2.8, 4.5, 1.3, 2],
           [5.4, 3.4, 1.5, 0.4, 1],
           [4.6, 3.4, 1.4, 0.3, 1],
           [4.9, 3.6, 1.4, 0.1, 1],
           [6.7, 2.5, 5.8, 1.8, 0],
           [5.0, 3.6, 1.4, 0.2, 1],
           [6.7, 3.3, 5.7, 2.5, 0],
           [4.4, 3.0, 1.3, 0.2, 1],
           [6.0, 2.2, 5.0, 1.5, 0],
           [6.0, 2.2, 4.0, 1.0, 2],
           [5.0, 3.4, 1.5, 0.2, 1],
           [5.7, 2.8, 4.1, 1.3, 2],
           [5.5, 2.4, 3.8, 1.1, 2],
           [5.1, 3.8, 1.9, 0.4, 1],
           [6.9, 3.1, 5.1, 2.3, 0],
           [5.6, 2.9, 3.6, 1.3, 2],
           [6.1, 2.8, 4.7, 1.2, 2],
           [5.5, 2.5, 4.0, 1.3, 2],
           [5.5, 2.3, 4.0, 1.3, 2],
           [6.0, 2.9, 4.5, 1.5, 2],
           [5.1, 3.8, 1.5, 0.3, 1],
           [5.7, 3.8, 1.7, 0.3, 1],
           [6.7, 3.3, 5.7, 2.1, 0],
           [4.8, 3.1, 1.6, 0.2, 1],
           [5.4, 3.0, 4.5, 1.5, 2],
           [6.5, 3.0, 5.2, 2.0, 0],
           [6.8, 3.0, 5.5, 2.1, 0],
           [7.6, 3.0, 6.6, 2.1, 0],
           [5.0, 3.0, 1.6, 0.2, 1],
           [6.7, 3.0, 5.0, 1.7, 2],
           [4.8, 3.4, 1.9, 0.2, 1],
           [5.8, 2.8, 5.1, 2.4, 0],
           [5.0, 2.3, 3.3, 1.0, 2],
           [4.8, 3.0, 1.4, 0.3, 1],
           [5.2, 3.5, 1.5, 0.2, 1],
           [6.1, 2.6, 5.6, 1.4, 0],
           [5.8, 2.7, 4.1, 1.0, 2],
           [6.9, 3.2, 5.7, 2.3, 0],
           [6.4, 2.9, 4.3, 1.3, 2],
           [7.3, 2.9, 6.3, 1.8, 0],
           [6.3, 2.8, 5.1, 1.5, 0],
           [6.2, 2.8, 4.8, 1.8, 0],
           [6.7, 3.1, 4.4, 1.4, 2],
           [6.0, 2.7, 5.1, 1.6, 2],
           [6.5, 3.0, 5.5, 1.8, 0],
           [6.1, 3.0, 4.9, 1.8, 0],
           [5.6, 3.0, 4.1, 1.3, 2],
           [4.7, 3.2, 1.6, 0.2, 1],
           [6.6, 3.0, 4.4, 1.4, 2]]

if __name__ == '__main__':
    a = int(0.3 * len(dataset))
    b = int(0.6 * len(dataset))
    
    trainOne = dataset[:a]
    trainTwo = dataset[a:b]
    trainThree = dataset[b:]
    
    oneClassifier = DecisionTreeClassifier(random_state=0)
    twoClassifier = DecisionTreeClassifier(random_state=0)
    threeClassifier = DecisionTreeClassifier(random_state=0)
    
    oneX = [row[:-1] for row in trainOne]
    oneY = [row[-1] for row in trainOne]
    twoX = [row[:-1] for row in trainTwo]
    twoY = [row[-1] for row in trainTwo]
    threeX = [row[:-1] for row in trainThree]
    threeY = [row[-1] for row in trainThree]
    
    oneClassifier.fit(oneX, oneY)
    twoClassifier.fit(twoX, twoY)
    threeClassifier.fit(threeX, threeY)
    
    entry = [float(el) for el in input().split(", ")]
    entry.pop()
    
    predOne = oneClassifier.predict([entry])[0]
    predTwo = twoClassifier.predict([entry])[0]
    predThree = threeClassifier.predict([entry])[0]
    
    predictions = {0: 0, 1: 0, 2: 0}
    for p in [predOne, predTwo, predThree]:
        predictions[p] += 1
    print(f"Glasovi: {predictions}")
    
    one, two, three = tuple(predictions.values())
    winner = None
    if one >= two and one >= three:
        winner = 0
    elif two >= one and two >= three:
        winner = 1
    elif three >= one and three >= two:
        winner = 2
    else: winner = "unknown"
    print(f"Predvidena klasa: {winner}")