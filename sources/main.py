import random

#changetest 1
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
"Bayern":"Bayern München Fußball",
"Brandenburg":"In Brandenburg brennen die Postkutschen (Potsdam)",
"Hessen":"In Hessen tanzen die Hasen auf der Wiese (Wiesbaden)",
"Mecklenburg-Vorpommern":"In Meck-Pomm sind die Pommes aus Schwein (Schwerin)",
"Nordrhein-Westfalen":"In NRW wohnen viele Dussel aber es ist kein Dorf",
"Rheinland-Pfalz":"Rheinland-Mainz",
"Sachsen":"Dynamo Dresden gibt allen auf den Sack (Sachsen)",
"Sachsen-Anhalt":"In Sachsen-Anhalt wohnen alle in einer Haltestelle, außer die Magd wohnt in der Burg (Magdeburg)",
"Schleswig-Holstein":"Schleswig-Holstein liegt weit oben im Norden, deswegen fühlen sich alle dort Kool (Kiel)",
"Thüringen":"Die Thüringer essen viel Thüringer Wurst, deswegen müssen sie oft Er(furtzen)",

"München":"Bayern München Fußball",
"Potsdam":"In Brandenburg brennen die Postkutschen (Potsdam)",
"Wiesbaden":"In Hessen tanzen die Hasen auf der Wiese (Wiesbaden)",
"Schwerin":"In Meck-Pomm sind die Pommes aus Schwein (Schwerin)",
"Düsseldorf":"In NRW wohnen viele Dussel aber es ist kein Dorf",
"Mainz":"Rheinland-Mainz",
"Dresden":"Dynamo Dresden gibt allen auf den Sack (Sachsen)",
"Magdeburg":"In Sachsen-Anhalt wohnen alle in einer Haltestelle, außer die Magd wohnt in der Burg (Magdeburg)",
"Kiel":"Schleswig-Holstein liegt weit oben im Norden, deswegen fühlen sich alle dort Kool (Kiel)",
"Erfurt":"Die Thüringer essen viel Thüringer Wurst, deswegen müssen sie oft Er(furtzen)",


}


dict_capital_state = {}
for key in dict_state_capital.keys():
    value = dict_state_capital.get(key)
    dict_capital_state.update({value:key})

dict_synonym_state = {"Nrw":"Nordrhein-Westfalen","Meck-Pomm":"Mecklenburg-Vorpommern"}

states = list(dict_state_capital.keys())
capitals = list(dict_capital_state.keys())
counter = 0
try_number = 10



def canonic(input_string):
    string1 = input_string.replace(" ", "-")
    string2 = string1.split("-")
    string3 = [i.capitalize() for i in string2 if len(i) > 0]
    output_string = "-".join(string3)
    return output_string


for i in range(try_number):
    if random.randint(0, 1) == 0:
        questions = states
        other_questions = capitals
        current_dict = dict_state_capital
        x = "die Hauptstadt"
    else:
        questions = capitals
        other_questions = states
        current_dict = dict_capital_state
        x = "das Bundesland"
    question = questions.pop(random.randint(0, len(questions) - 1))

    answer = current_dict[question]
    if question == answer:
        other_questions.remove(question)



    input_user = input("Geben sie "+ x +" von " + question + " ein: ")
    input_user1 = canonic(input_user)

    s = dict_synonym_state.get(input_user1)
    if s != None:
        input_user1 = s

    if input_user1 == answer:
        counter += 1
        print("Das ist richtig")
    else:

        if answer in esel.keys():
            hint = " // " +esel[answer]
        else:
            hint = ""
        print("Falsch: " + answer + hint)

percentage = 100 * counter / try_number
print("Ihr Ergebniss " + str(percentage) + "%")

if percentage <= 25:
    print("Achtung starke Bildungslücke ! ")
elif percentage <= 50:
    print("Das muss besser gehen !")
elif percentage <= 75:
    print("Nicht schlecht !")
else:
    print("Alter Schlaumeier ! ")
