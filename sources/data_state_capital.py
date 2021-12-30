def create_game_collection():
    '''
    Creation of game collection (a list)
    :return:
       - index of start game
       - list of  data of games
    '''
    games = [
        DataStateCapital(),
        DataEnDe()
    ]
    return 0, games


class DataStateCapital:
    """

    """

    def __init__(self):
        self.game_name = "Bundesland Hauptstadt Trainer"

        self.quan = {
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
        self.mnemonics = {
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
        self.synonyms = {"Nrw": "Nordrhein-Westfalen", "Meck-Pomm": "Mecklenburg-Vorpommern"}
        self.general_question = " Geben sie #generic# von #question# ein: "
        self.generic_term_1 = 'die Hauptstadt'
        self.generic_term_2 = 'das Bundesland'


class DataEnDe:
    def __init__(self):
        self.game_name = "Englisch deutsch dictionary"

        self.quan = {
            "House": "Haus",
            "Walk": "Gehen",
            "Table": "Tisch",
        }

        self.mnemonics = {
            "House": "klingt gleich",
            "Walk": "jemand geht auf Wolken",
        }
        self.synonyms = {
            "Building": "House",
            "Go": "Walk"
        }
        self.general_question = " übersetzen sie das Wort #question# in #generic#: "
        self.generic_term_1 = 'deutsch'
        self.generic_term_2 = 'englisch'
