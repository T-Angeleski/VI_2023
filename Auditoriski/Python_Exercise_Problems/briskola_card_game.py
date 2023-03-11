def briscola_score(first_round, second_round):
    # Not sure about rules of this one
    pointsFirst = countPoints(first_round)
    pointsSecond = countPoints(second_round)

    if pointsSecond > pointsFirst:
        return "You Win!"
    elif pointsSecond < pointsFirst:
        return "You Lose!"
    else:
        return "Draw!"


def countPoints(cards):
    points = 0
    for card in cards:
        cardType = card[0]
        if cardType == "A":
            points += 11
        elif cardType == "3":
            points += 10
        elif cardType == "K":
            points += 4
        elif cardType == "Q":
            points += 3
        elif cardType == "J":
            points += 2
        else:
            pass
    return points


if __name__ == '__main__':
    print(briscola_score(
        ["3c", "3s", "Qd", "Jh", "5d", "Jc", "6d", "Ad", "Js", "Qc"],
        ["Jd", "Kd", "4c", "6s", "Ks", "5c", "3d", "As", "Jh", "6h"]
    ))

    # Igrachot ima 43 poeni vo prvoto kolo. Potrebno e da se osvojat najmalku 78 poeni
    # vo vtoroto kolo. Brojot na poeni na igrachot vo vtoroto kolo e 33.

    print(briscola_score(
        ["Ac", "As", "3d", "3h", "3s", "Ah", "Kd"],
        ["3d", "Ad", "Ac", "As", "Ah"]
    ))

    # Igrachot ima 67 poeni vo prvoto kolo. Potrebno e da se osvojat najmalku 54 poeni
    # vo vtoroto kolo. Brojot na poeni na igrachot vo vtoroto kolo e 54.

    print(briscola_score(
        ["Ac", "As", "3d", "3h", "3s", "Ah", "Kd"],
        ["3d", "Ad", "Ac", "As", "3h"]
    ))

    # Igrachot ima 67 poeni vo prvoto kolo. Potrebno e da se osvojat najmalku 54 poeni
    # vo vtoroto kolo. Brojot na poeni na igrachot vo vtoroto kolo e 53. Vkupniot rezultat
    # e 120 poeni, sto e ist rezultat so protivnikot.

"""
## Задача 3 - Брискола
Брискола е Италијанска игра со карти, каде што со се вклучуваат 40 карти со
4 форми (hearts, spades, clubs и diamonds) и со 10 карти за секоја форма.
Во овој предизвик, нотацијата што се користи за картите е стринг што ја содржи
вредноста на картата
(со почетна голема буква за картите без бројка) и мала иницијална буква за формата, пр.:

    Ah = Ace of Hearts
    2s = Two of Spades
    Jc = Jack of Clubs
    Kd = King of Diamonds

Максималниот број на поени е **120**. Кога се бројат постигнатите поени на
крајот на играта, картите ги имаат следниве вредности:

    Ace: 11 поени
    Three: 10 поени
    King: 4 поени
    Queen: 3 поени
    Jack: 2 поени
    Било која друга карта нема вредност (0 поени).

Секоја игра на Брискола е направена од две кола. По првото коло, поените се бројат за
играчот и за противникот, и овие поени (плус 1) ја постават целта за победа на играта,
по што се игра второто коло.
Потребно е да се имплементира функција која прима две листи како влез (колекцијата од
карти на играчот од првото коло и колекцијата на карти од второто коло), и враќа како излез:

    "Win!" ако во второто коло играчот има поголем резултат на поените од противникот во првото коло.
    "Lose!" ако во второто коло играчот има помал рзултат од противникот во првото коло.
    "Draw!" ако во второто коло играчот има ист вкупен број на поени како и противникот.

"""