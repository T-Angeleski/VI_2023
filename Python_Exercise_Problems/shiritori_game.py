"""
Оваа задача е англиски пресврт на јапонската игра со зборови Ширитори.
Основната премиса е да се следат две правила:

    Првиот карактер на следниот збор мора да одговара на последниот
    карактер на претходниот збор.
    Даден збор не смее да се повтори во текот на играта.

Напишете класа Shirikori која има два податочни атрибути:
    words: листа на претходно кажани зборови.
    game_over: променлина која има вредност True ако играта е завршена.
    и два методи:

    play: метода која на влез очекува збор како аргумент и проверува дали е
    валиден (зборот треба да ги следи правилата #1 и #2 од погоре).
        Ако е валиден, го додава зборот на листата од зборови, и ја враќа
        листата на зборови како излез.
        Ако не е валиден (некое правило е прекршено), враќа "game over" и го
        поставува game_over на True.
    restart: метода која ја ресетира листата на зборови на празна листа [],
        и го поставува game_over на False. Потребно е да врати "game restarted".

"""


class Shiritori:
    def __init__(self):
        self.words = []
        self.game_over = False

    def restart(self):
        print("Restarting...")
        self.words = []
        self.game_over = False

    def play(self, word):
        if word in self.words:
            self.game_over = True
            print("game over")
            print(f"{word} is already in the list of words!")
            return

        if len(self.words) == 0:
            self.words.append(word)
        else:
            if word[0] == self.words[-1][-1]:
                self.words.append(word)
            else:
                self.game_over = True
                print("game over")
                print(f"{word} does not start with {self.words[-1][-1]}")
                return


if __name__ == '__main__':
    my_shiritori = Shiritori()

    my_shiritori.play("apple")
    my_shiritori.play("ear")
    my_shiritori.play("rhino")
    my_shiritori.play("corn")

    # Corn не почнува на "o".

    print(my_shiritori.words)
    my_shiritori.restart()
    print(my_shiritori.words)

    # Листата на зборови треба да биде ресетирана на празна листа.

    my_shiritori.play("hostess")
    my_shiritori.play("stash")
    my_shiritori.play("hostess")

    # Зборовите не смеат да се повторуваат.