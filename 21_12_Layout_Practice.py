import tkinter as tk
from base_quiz import Quiz
from data_EN_DE import DataEnDe
from data_state_capital import DataStateCapital

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
            counter_right_label.config(text=str(positive_counter))
            question_valuation_label.config(text=machine_answer + " : Das ist richtig")
        else:
            negative_counter += 1
            counter_wrong_label.config(text=str(negative_counter))
            question_valuation_label.config(text="Falsch!  Richtige Antwort ist:" + machine_answer)

            mnemonic_label.config(text= mnemonic)
        counter_count_label.config(text=str(negative_counter) + " " + str(positive_counter))

        user_entry.delete(0, "end")
        if positive_counter + negative_counter == total_tries:  # Bei Beendigung der kompletten Versuche
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
            counter_wrong_label.config(text="")
            counter_right_label.config(text="")
            question_valuation_label.config(text="")
            next_question_text_label.config(text="")
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
    txt = quiz_data.general_question
    txt1 = txt.replace("#generic#", generic_term)  # Was wird hier warum replaced ?
    txt2 = txt1.replace("#question#", question)
    next_question_text_label.config(text=txt2)  # im next_question_label wird text2 ausgespielt.


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

## Variables for Labels and Pack
text_color = "#4dffff"

title_color = "#ff9933"
title_font = 18
title_width = 11
title_anchor = "w"
# title_font_layout = [bg="#ff9933", font=18, width=11, anchor="w"]

## Frames
row0 = tk.Frame(root)
row1 = tk.Frame(root)
row2 = tk.Frame(root)
row3 = tk.Frame(root)
row4 = tk.Frame(root)
row5 = tk.Frame(root)
row6 = tk.Frame(root)
row7 = tk.Frame(root)

## Labels Entrys Button (text,size,fonts,bg)
current_game_name_label = tk.Label(row0, text=f"Spiel: {quiz_data.game_name}",
                                   bg="#5d6d7e", font=20)
press_enter_label = tk.Label(root, text=" Drücken sie Enter zum starten.",
                             bg="#b3ffb3", font=15)
next_question_title_label = tk.Label(row1, text='Frage: ', bg="#ff9933",
                                     font=18, width=11, anchor="w")
next_question_text_label = tk.Label(row1, text='', bg=text_color, font=18, width=50, anchor="w")
user_answer_title_label = tk.Label(row2, text="Antwort: ", bg=title_color, font=title_font, width=title_width,
                                   anchor=title_anchor)
user_entry = tk.Entry(row2, width=40, state="disabled")
send_button = tk.Button(row2, text="Absenden", command=send, bg="#ffffcc")  ## Absenden in der GUI löst send() aus
correctness_counter_right_title = tk.Label(row3, text="Richtig: ", bg=title_color, font=title_font, width=title_width,
                                           anchor=title_anchor)
correctness_counter_wrong_title = tk.Label(row4, text="Falsch: ", bg=title_color, font=title_font, width=title_width,
                                           anchor=title_anchor)
machine_result_title = tk.Label(row5, text="Resultat: ", bg=title_color, font=title_font, width=title_width,
                                anchor=title_anchor)
counter_right_label = tk.Label(row3, text=str(positive_counter), width=3, bg=text_color)
counter_wrong_label = tk.Label(row4, text=str(negative_counter), width=3, bg=text_color)
question_valuation_label = tk.Label(row5, bg="#99ffff", font=12)
counter_count_label = tk.Label(row6, bg="#ff794d", font=15)
user_evaluation_label = tk.Label(row6, bg=text_color, font=15)
mnemonic_title = tk.Label(row6, text="Eselsbrücke ", bg=title_color, font=title_font, width=title_width,
                          anchor=title_anchor)
mnemonic_label = tk.Label(row6, text='', bg=text_color, font=18, width=50, anchor="w")
# Layout-Manager
## Frames .pack
row0.pack(pady=(10, 10))
row1.pack(fill="x", pady=(10, 10))
row2.pack(fill="x", pady=(10, 10))
row3.pack(fill="x", pady=(10, 10))
row4.pack(fill="x", pady=(10, 10))
row5.pack(fill="x", pady=(10, 10))
row6.pack(fill="x", pady=(10, 10))
row7.pack(fill="x")

## Labels, Etry, Button, .pack
current_game_name_label.pack()
next_question_title_label.pack(side="left", anchor="w", padx=(0, 40))
next_question_text_label.pack(side="left", anchor="w")
user_answer_title_label.pack(side="left", anchor="w", padx=(0, 40))
user_entry.pack(side="left", anchor="w")
send_button.pack(side="left", anchor="w", padx=(60, 0))
correctness_counter_right_title.pack(side="left", anchor="w", padx=(0, 40))
correctness_counter_wrong_title.pack(side="left", anchor="w", padx=(0, 40))
counter_right_label.pack(side="left", anchor="w", padx=(0, 40))
counter_wrong_label.pack(side="left", anchor="w", padx=(0, 40))
machine_result_title.pack(side="left", anchor="w", padx=(0, 40))
question_valuation_label.pack(side="left", anchor="w", padx=(0, 40))
mnemonic_title.pack(side="left", anchor="w", padx=(0, 40))
mnemonic_label.pack(side="left", anchor="w", padx=(0, 40))

root.bind('<Return>', send)
root.mainloop()

"""# Label, Button, Entry --> Packmanager .grid
current_game_name_label.grid(row=0, pady=10, sticky="W")  # --> Frame1
press_enter_label.grid(row=1, column=0, pady=10, sticky="W")  # --> Frame1
next_question_label.grid(row=2, column=0, pady=10, sticky="W")  # --> Frame1
send_button.grid(row=0, column=1, padx=20, pady=10, sticky="W", )  # --> Frame2
user_entry.grid(row=0, column=0, pady=10, sticky="W")  # --> Frame2
question_valuation_label.grid(row=0, column=0, pady=10, sticky="W")  # -> Frame3
counter_count_label.grid(row=1, column=0, sticky="W")  # -> Frame 3
user_evaluation_label.grid(row=2, column=0, pady=10, sticky="W")  # -> Frame 3
"""
