"""
Четворица пријатели играат едноставна игра со коцки (играчите се означени
со p1, p2, p3 и p4). Во секое коло, сите играчи фрлаат пар од шестстрани
коцки. Играчот со најнизок вкупен резултат е отстранет. Ако најнискиот
резултат го делат двајца или повеќе играчи,
играчот во таа група со најнизок резултат од првата коцка е отстранет. Ако
најнискиот резултат е сè уште споделен (т.е. двајца или повеќе играчи имаат исти фрлања во ист редослед),
тогаш сите играчи повторно ги фрлаат коцките.
Овој процес продолжува сè додека не остане еден играч.
Ако е дадена листа на фрлања на коцките
(дадени во редоследот на играчите за секое коло), вратете го победникот на играта.
"""


def dice_game(turns):
    players = [0, 0, 0, 0]
    playerIndexes = [0, 1, 2, 3]
    while len(players) != 1:
        for player in players:
            if len(turns) != 0:
                players[players.index(player)] = turns.pop(0)
            else:
                break

        # Find player with least "points"
        min, sum, toRemoveIndex = players[0], players[0][0] + players[0][1], 0
        isDraw = False  # For case of same dices thrown
        for player in players[1:]:
            sum = player[0] + player[1]
            if sum == min[0] + min[1]:
                # Both same sum, get min from lower first throw
                if player[0] < min[0]:
                    toRemoveIndex = players.index(player)
                    min = player
                # Check for draw
                elif min == player:
                    isDraw = True
            elif sum < min[0] + min[1]:
                # Standard minimum player
                toRemoveIndex = players.index(player)
                min = player

        if not isDraw:
            players.pop(toRemoveIndex)
            playerIndexes.pop(toRemoveIndex)

    # Get index of last remaining player
    return f"Player {playerIndexes[0] + 1} wins!"


if __name__ == '__main__':
    turns = [(6, 2), (4, 3), (3, 4), (5, 4), (3, 5), (1, 5), (4, 3), (1, 5),
             (1, 5), (2, 2), (5, 6)]
    print(dice_game(turns))