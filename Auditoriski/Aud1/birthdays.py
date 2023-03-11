"""
Во оваа задача се чуваат родендените на пријатели,
кои треба да се пронајдат според имињата на пријателите.
Креирајте речник (dictionary) со имиња и родендени.
Потоа, додадете функционалност со
која од стандарден влез се чита име на пријател,
и вратете го неговиот роденден
(односно испечатете го на стандарден излез)
"""

if __name__ == '__main__':
    birthdays_by_names = {
        "Ana": "17/01/1991",
        "Marija": "02/06/1981",
        "Stefan": "14/08/1999",
        "Aleksandar": "20/09/2002"
    }

    print("Dobredojdovte do rechnikot za rodendeni. "
          "Nie gi znaeme rodendenite na:")

    print("\n".join(birthdays_by_names.keys()))

    print("Koj rodenden e potrebno da se prebara?")
    nameToSearch = input()
    if nameToSearch in birthdays_by_names:
        print(f"Rodendenot na {nameToSearch} e na {birthdays_by_names.get(nameToSearch)}\n")
    else:
        print("Imeto ne e vo rechnikot")
