"""
Потребно е да се напише Python програма за пресметка на фреквенцијата
на зборовите на влез. На излез треба да се испечатат зборовите и нивната
фреквенција на појавување, така што зборовите ќе бидат алфабетски поредени
по азбучен редослед.
"""

if __name__ == '__main__':
    example = "New to Python or choosing between Python 2 and Python 3? " \
              "Read Python 2 or Python 3."

    words = example.split(" ")
    # Create starter dictionary
    frequencyByWord = {}
    for word in words:
        if word in frequencyByWord:
            frequencyByWord[word] += 1
        else:
            frequencyByWord[word] = 1

    # Sort
    sortedList = sorted(frequencyByWord.items())  # List[Tuple (key, value)]
    sortedWords = {}
    for word, count in sortedList:
        sortedWords[word] = count

    # Print in format
    for k, v in sortedWords.items():
        print(f"{k}:{v}")