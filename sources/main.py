from base_quiz import Quiz

dict_state_capital = {
    "Baden-Württemberg": "Stuttgart",
    "Bayern": "München",
    "Berlin": "Berlin",
    "Brandenburg": "Potsdam",
    "Bremen": "Bremen",
    "Hamburg": "Hamburg",
    "Hessen": "Wiesbaden",
    "Mecklenburg-Vorpommern": "Schwerin",
    "Niedersachsen": "Hannover",
    "Nordrhein-Westfalen": "Düsseldorf",
    "Rheinland-Pfalz": "Mainz",
    "Saarland": "Saarbrücken",
    "Sachsen": "Dresden",
    "Sachsen-Anhalt": "Magdeburg",
    "Schleswig-Holstein": "Kiel",
    "Thüringen": "Erfurt"}

esel = {
    "Bayern": "Bayern München Fußball",
    "Brandenburg": "In Brandenburg brennen die Postkutschen (Potsdam)",
    "Hessen": "In Hessen tanzen die Hasen auf der Wiese (Wiesbaden)",
    "Mecklenburg-Vorpommern": "In Meck-Pomm sind die Pommes aus Schwein (Schwerin)",
    "Nordrhein-Westfalen": "In NRW wohnen viele Dussel aber es ist kein Dorf",
    "Rheinland-Pfalz": "Rheinland-Mainz",
    "Sachsen": "Dynamo Dresden gibt allen auf den Sack (Sachsen)",
    "Sachsen-Anhalt": "In Sachsen-Anhalt wohnen alle in einer Haltestelle, außer die Magd wohnt in der Burg (Magdeburg)",
    "Schleswig-Holstein": "Schleswig-Holstein liegt weit oben im Norden, deswegen fühlen sich alle dort Kool (Kiel)",
    "Thüringen": "Die Thüringer essen viel Thüringer Wurst, deswegen müssen sie oft Er(furtzen)",

    "München": "Bayern München Fußball",
    "Potsdam": "In Brandenburg brennen die Postkutschen (Potsdam)",
    "Wiesbaden": "In Hessen tanzen die Hasen auf der Wiese (Wiesbaden)",
    "Schwerin": "In Meck-Pomm sind die Pommes aus Schwein (Schwerin)",
    "Düsseldorf": "In NRW wohnen viele Dussel aber es ist kein Dorf",
    "Mainz": "Rheinland-Mainz",
    "Dresden": "Dynamo Dresden gibt allen auf den Sack (Sachsen)",
    "Magdeburg": "In Sachsen-Anhalt wohnen alle in einer Haltestelle, außer die Magd wohnt in der Burg (Magdeburg)",
    "Kiel": "Schleswig-Holstein liegt weit oben im Norden, deswegen fühlen sich alle dort Kool (Kiel)",
    "Erfurt": "Die Thüringer essen viel Thüringer Wurst, deswegen müssen sie oft Er(furtzen)",

}

dict_synonym_state = {"Nrw": "Nordrhein-Westfalen", "Meck-Pomm": "Mecklenburg-Vorpommern"}

quiz = Quiz(
    dict_state_capital,
    'die Hauptstadt', 'das Bundesland',
    dict_synonym_state,
    esel
)

try_number = 10
counter = 0
for i in range(try_number):

    answer_generic_term, question, answer, mnemonic = quiz.next_question()
    input_user = input("Geben sie " + answer_generic_term + " von " + question + " ein: ")
    input_user1 = quiz.get_canonic(input_user)

    if input_user1 == answer:
        counter += 1
        print("Das ist richtig")
    else:
        if mnemonic:
            hint = ' // Eselsbrücke: ' + mnemonic
        else:
            hint = ''
        print("Falsch: " + answer + hint)

percentage = 100 * counter / try_number
print('--------------------')
print("Ihr Ergebniss " + str(percentage) + "%")

if percentage <= 25:
    print("Achtung starke Bildungslücke ! ")
elif percentage <= 50:
    print("Das muss besser gehen !")
elif percentage <= 75:
    print("Nicht schlecht !")
else:
    print("Alter Schlaumeier ! ")
