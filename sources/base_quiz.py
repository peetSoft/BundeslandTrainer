import random


class Quiz:
    def __init__(self, quan_1=None, answer_generic_term_1=None, answer_generic_term_2=None,
                 synonyms=None, mnemonics=None):
        pass
        # self.quan_1 = quan_1.copy()
        # self.answer_generic_term_1 = answer_generic_term_1
        # self.answer_generic_term_2 = answer_generic_term_2
        # self.mnemonics = mnemonics
        # self.synonyms = synonyms
        # self.quan_2 = dict((v, k) for k, v in quan_1.items())

    def config(self, quan_1, general_question, generic_term_1, generic_term_2, synonyms, mnemonics):
        self.quan_1 = quan_1.copy()
        self.general_question = general_question
        self.generic_term_1 = generic_term_1
        self.generic_term_2 = generic_term_2
        self.mnemonics = mnemonics
        self.synonyms = synonyms
        self.quan_2 = dict((v, k) for k, v in quan_1.items())

    def next_question(self):
        if random.randint(0, 1) == 0:
            quan = self.quan_1
            other_quan = self.quan_2
            answer_generic_term = self.generic_term_1
        else:
            quan = self.quan_2
            other_quan = self.quan_1
            answer_generic_term = self.generic_term_2

        question, answer = list(quan.items())[random.randint(0, len(quan) - 1)]
        # chooses random question and answer from quan
        if question in self.mnemonics:
            mnemonic = self.mnemonics[question]
        elif answer in self.mnemonics:
            mnemonic = self.mnemonics[answer]
        else:
            mnemonic = ''

        # if question == answer:
        #     other_quan.remove(question)

        return answer_generic_term, question, answer, mnemonic

    def get_canonic(self, word):
        canonic_word = canonic(word)
        if canonic_word in self.synonyms:
            return self.synonyms[canonic_word]
        return canonic_word


def canonic(input_string):
    string1 = input_string.replace(" ", "-")
    string2 = string1.split("-")
    string3 = [i.capitalize() for i in string2 if len(i) > 0]
    output_string = "-".join(string3)
    return output_string
