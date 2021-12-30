import tkinter as tk
from base_quiz import Quiz
from data_state_capital import DataStateCapital, DataEnDe

"""
3 Klassen werden importiert. 
"""


def send(event=None):
    global positive_counter, negative_counter, machine_answer
    if machine_answer != "":
        user_answer = user_entry.get()
        user_answer_canonic = quiz.get_canonic(user_answer)

        if user_answer_canonic == machine_answer:
            positive_counter += 1
            question_valuation_label.config(text=machine_answer + " : Das ist richtig")
        else:
            negative_counter += 1
            question_valuation_label.config(text="Falsch!  Richtige Antwort ist:   "
                                                 + machine_answer + " Eselsbrücke=" + mnemonic, )

        counter_count_label.config(text=str(negative_counter) + " " + str(positive_counter))

        user_entry.delete(0, "end")
        if positive_counter + negative_counter == total_tries:
            result = 100 * positive_counter / total_tries
            if result < 30:
                user_evaluation_label.config(text="Starke Bildungslücke!")
            elif result < 70:
                user_evaluation_label.config(text="Das muss besser werden!")
            else:
                user_evaluation_label.config(text="Sehr stark!")
            positive_counter = 0
            negative_counter = 0
            press_enter_label.config(text="Für ein neues Spiel Enter drücken!")
            user_entry.config(state="disabled")
            question_valuation_label.config(text="")
            next_question_label.config(text="")
            machine_answer = ""
            return
        next_question()
    else:  # Das passiert alles wenn machine answer "leer" ist.
        press_enter_label.config(text="", )
        counter_count_label.config(text="")
        user_evaluation_label.config(text="")
        user_entry.config(state="normal")
        next_question()  # next_question wird aufgerufen.


def next_question():
    global machine_answer, mnemonic, quiz_data  # wird generiert und global gemacht?
    generic_term, question, machine_answer, mnemonic = quiz.next_question()  # die 4 Variablen werden in Class Quiz
    # Hergestellt und hier benutzt.
    txt = "Nächste Frage:" + quiz_data.general_question
    txt1 = txt.replace("#generic#", generic_term)  # Was wird hier warum replaced ?
    txt2 = txt1.replace("#question#", question)
    next_question_label.config(text=txt2)  # im next_question_label wird text2 ausgespielt.


def game_changer():
    global quiz, current_game_name_label, quiz_data
    if game.get() == 1:
        quiz_data = state_capital_data
    elif game.get() == 2:
        quiz_data = de_en_data
    else:
        quiz_data = None
    current_game_name_label.config(text=quiz_data.game_name)
    quiz.config(quiz_data.quan, quiz_data.generic_term_1, quiz_data.generic_term_2,
                quiz_data.synonyms, quiz_data.mnemonics)


positive_counter = 0
negative_counter = 0
total_tries = 3

machine_answer = ""  # machine_answer wird ein leerer String zugewiesen
mnemonic = ""

de_en_data = DataEnDe()  # initierung der Klasse
state_capital_data = DataStateCapital()  # initierung der Klasse

quiz_data = state_capital_data

quiz = Quiz(quiz_data.quan, quiz_data.generic_term_1, quiz_data.generic_term_2,
            quiz_data.synonyms, quiz_data.mnemonics)
'''
Initierung der Klasse: 3 initierte Klassen ( quiz_en_de_data, state_capital_data, quiz )
'''
root = tk.Tk()
root.geometry("1000x400")

## Menu
gui_menu = tk.Menu(root)
root.config(menu=gui_menu)

game = tk.IntVar(value=1)

game_menu = tk.Menu(gui_menu)
gui_menu.add_cascade(label="Game", menu=game_menu)
game_menu.add_radiobutton(label=state_capital_data.game_name, variable=game, value=1, command=game_changer)

game_menu.add_radiobutton(label=de_en_data.game_name, variable=game, value=2, command=game_changer)

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

## 6x Label, 1x Entry, 1x Button: Definitionen

current_game_name_label = tk.Label(frame1, text=f"Spiel: {quiz_data.game_name}",
                                   bg="#5d6d7e", font=20)
press_enter_label = tk.Label(frame1, text=" Drücken sie Enter zum starten.",
                             bg="#b3ffb3", font=15)
next_question_label = tk.Label(frame1, text='', bg="#cceeff", font=18)
send_button = tk.Button(frame2, text="Absenden", command=send)  ## Absenden in der GUI löst send() aus
user_entry = tk.Entry(frame2, width=20, state="disabled")
question_valuation_label = tk.Label(frame3, bg="#99ffff", font=12)
counter_count_label = tk.Label(frame3, bg="#ff794d", font=15)
user_evaluation_label = tk.Label(frame3, bg="#ff3333", font=15)

frame1.grid(column=0, row=0, sticky="W")
frame2.grid(column=0, row=1, sticky="W")
frame3.grid(column=0, row=2, sticky="W")

# Label, Button, Entry --> Packmanager .grid
current_game_name_label.grid(row=0, pady=10, sticky="W")  # --> Frame1
press_enter_label.grid(row=1, column=0, pady=10, sticky="W")  # --> Frame1
next_question_label.grid(row=2, column=0, pady=10, sticky="W")  # --> Frame1
send_button.grid(row=0, column=1, padx=20, pady=10, sticky="W", )  # --> Frame2
user_entry.grid(row=0, column=0, pady=10, sticky="W")  # --> Frame2
question_valuation_label.grid(row=0, column=0, pady=10, sticky="W")  # -> Frame3
counter_count_label.grid(row=1, column=0, sticky="W")  # -> Frame 3
user_evaluation_label.grid(row=2, column=0, pady=10, sticky="W")  # -> Frame 3

root.bind('<Return>', send)
root.mainloop()
