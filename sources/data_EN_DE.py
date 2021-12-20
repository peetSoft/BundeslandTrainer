class DataEnDe:
    def __init__(self):
        self.game_name = "Englisch deutsch dictionary"
        self.general_question = " übersetzen sie das Wort #question# in #generic#: "

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
        self.generic_term_1 = 'deutsch'
        self.generic_term_2 = 'englisch'
