"""Креирајте функција која го враќа мнозинството на гласови во листа.
Мнозинството на гласови е елемент што се појавува > N / 2 пати во листата (
каде што N е должината на листата).
Забелешки:
    Фреквенцијата на мнозинскиот глас мора да биде поголема од 1/2.
    Ако нема мнозинство на гласови, врати None.
    Ако листата е празна, врати None.
"""


def majority_vote(votes):
    totalVotes = len(votes)
    if totalVotes == 0: return None

    countPerVote = {}
    for vote in votes:
        if countPerVote.get(vote) is not None:
            countPerVote[vote] += 1
        else:
            countPerVote[vote] = 1

    # Get max
    majority = next(iter(countPerVote))
    for vote in countPerVote:
        if countPerVote[vote] > countPerVote[majority]:
            majority = vote

    return majority if countPerVote[majority] > (totalVotes / 2) else None


if __name__ == '__main__':
    input1 = ["A", "A", "B"]
    input2 = ["A", "A", "A", "B", "C", "A"]
    input3 = ["A", "B", "B", "A", "C", "C"]

    print(majority_vote(input1))
    print(majority_vote(input2))
    print(majority_vote(input3))
    print(majority_vote([]))