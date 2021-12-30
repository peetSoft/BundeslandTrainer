import tkinter as tk
from base_quiz import Quiz
from data_state_capital import create_game_collection


def send(event=None):
    global positive_counter, negative_counter, machine_answer
    counter = positive_counter + negative_counter
    if machine_answer == "":
        # Das passiert alles wenn machine answer "leer" ist.

        if counter == total_tries:  # Bei Beendigung der kompletten Versuche

            user_entry.config(state="disabled")
            counter_wrong_label.config(text="")
            counter_right_label.config(text="")
            question_valuation_text_label.config(text="")
            next_question_text_label.config(text="")
            mnemonic_label.config(text="")
            positive_counter = 0
            negative_counter = 0
            machine_answer = ""
        else:
            next_question()  # next_question wird aufgerufen.
            # return

    else:
        user_answer = user_entry.get()
        user_answer_canonic = quiz.get_canonic(user_answer)

        if user_answer_canonic == machine_answer:
            positive_counter += 1
            counter_right_label.config(text=str(positive_counter))
            question_valuation_text_label.config(text=machine_answer + " : Das ist richtig")
            next_question()
        else:
            negative_counter += 1
            counter_wrong_label.config(text=str(negative_counter))
            question_valuation_text_label.config(text="Falsch!  Richtige Antwort ist:" + machine_answer)

            mnemonic_label.config(text=mnemonic)
        if positive_counter + negative_counter == total_tries:
            machine_answer = ""
            result = 100 * positive_counter / total_tries
            if result < 30:
                user_evaluation_label_text.config(text="Starke Bildungslücke!")
            elif result < 70:
                user_evaluation_label_text.config(text="Das muss besser werden!")
            else:
                user_evaluation_label_text.config(text="Sehr stark!")

        else:
            next_question()
        user_entry.delete(0, "end")


def next_question():
    global machine_answer, mnemonic  # wird generiert und global gemacht?
    generic_term, question, machine_answer, mnemonic = quiz.next_question()  # die 4 Variablen werden in Class Quiz
    # Hergestellt und hier benutzt.
    txt = quiz.general_question
    txt1 = txt.replace("#generic#", generic_term)  # Was wird hier warum replaced ?
    txt2 = txt1.replace("#question#", question)
    next_question_text_label.config(text=txt2)  # im next_question_label wird text2 ausgespielt.
    user_entry.config(state='normal')
    user_entry.focus_force()


def game_changer():
    global quiz, current_game_name_label, games
    game = games[game_index.get()]
    current_game_name_label.config(text=game.game_name)
    quiz.config(game.quan, game.general_question, game.generic_term_1, game.generic_term_2,
                game.synonyms, game.mnemonics)


positive_counter = 0
negative_counter = 0
total_tries = 3

machine_answer = ""  # machine_answer wird ein leerer String zugewiesen
mnemonic = ""

quiz = Quiz()
'''
Initiierung der Klasse: 3 initierte Klassen ( quiz_en_de_data, state_capital_data, quiz )
'''
root = tk.Tk()
root.geometry("1000x450")

## Variables for Labels and Pack
text_color = "#4dffff"
text_width = 50

## Frames
row0 = tk.Frame(root)
row1 = tk.Frame(root)
row2 = tk.Frame(root)
row3 = tk.Frame(root)
row4 = tk.Frame(root)
row5 = tk.Frame(root)
row6 = tk.Frame(root)
row7 = tk.Frame(root)
row8 = tk.Frame(root)

# Parameters as dictionary
title_style_parameters = {"bg": "#ff9933", "font": 18, "width": 11, "anchor": "w"}
text_style_parameters = {'bg': text_color, 'font': 18, 'width': text_width, 'anchor': "w"}
## Labels Entrys Button (text,size,fonts,bg)
current_game_name_label = tk.Label(row0, bg="#5d6d7e", font=20)

next_question_title_label = tk.Label(row1, text='Frage: ', **title_style_parameters)
next_question_text_label = tk.Label(row1, text='', **text_style_parameters)

user_answer_title_label = tk.Label(row2, text="Antwort: ", **title_style_parameters)
user_entry = tk.Entry(row2, width=40, state="disabled")
send_button = tk.Button(row2, text="Absenden", command=send, bg="#ffffcc")  ## Absenden in der GUI löst send() aus

machine_result_title_label = tk.Label(row3, text="Resultat: ", **title_style_parameters)
question_valuation_text_label = tk.Label(row3, bg=text_color, font=18, width=text_width)

mnemonic_title = tk.Label(row4, text="Eselsbrücke ", **title_style_parameters)
mnemonic_label = tk.Label(row4, text='', **text_style_parameters)

correctness_counter_right_title = tk.Label(row5, text="Richtig: ", **title_style_parameters)
counter_right_label = tk.Label(row5, text=str(positive_counter), width=3, bg=text_color)

correctness_counter_wrong_title = tk.Label(row6, text="Falsch: ", **title_style_parameters)
counter_wrong_label = tk.Label(row6, text=str(negative_counter), width=3, bg=text_color)

user_evaluation_label_title = tk.Label(row7, text="Auswertung", **title_style_parameters)
user_evaluation_label_text = tk.Label(row7, **text_style_parameters)

hint_text = tk.Label(row8, text='Hint', bg="#c2d6d6", font=7, width=text_width + 15, anchor="w")

# Layout-Manager
## Frames .pack
row0.pack(pady=(10, 10))
row1.pack(fill="x", pady=(10, 10))
row2.pack(fill="x", pady=(10, 10))
row3.pack(fill="x", pady=(10, 10))
row4.pack(fill="x", pady=(10, 10))
row5.pack(fill="x", pady=(10, 10))
row6.pack(fill="x", pady=(10, 10))
row7.pack(fill="x", pady=(10, 10))
row8.pack(fill="x", pady=(10, 10))

title_pack_parameter = {"side": "left", "anchor": "w", "padx": (0, 40)}

## Labels, Etry, Button, .pack
current_game_name_label.pack()
next_question_title_label.pack(**title_pack_parameter)
next_question_text_label.pack(side="left", anchor="w")
user_answer_title_label.pack(**title_pack_parameter)
user_entry.pack(side="left", anchor="w")
send_button.pack(side="left", anchor="w", padx=(60, 0))
correctness_counter_right_title.pack(**title_pack_parameter)
correctness_counter_wrong_title.pack(side="left", anchor="w", padx=(0, 40))
counter_right_label.pack(**title_pack_parameter)
counter_wrong_label.pack(**title_pack_parameter)
machine_result_title_label.pack(**title_pack_parameter)
question_valuation_text_label.pack(**title_pack_parameter)
mnemonic_title.pack(**title_pack_parameter)
mnemonic_label.pack(side="left", anchor="w", padx=(0, 40))
user_evaluation_label_title.pack(**title_pack_parameter)
user_evaluation_label_text.pack(side="left", anchor="w")
hint_text.pack(side="left", anchor="w")

root.bind('<Return>', send)

## Menu
gui_menu = tk.Menu(root)
root.config(menu=gui_menu)

gi, games = create_game_collection()
game_index = tk.IntVar(value=gi)

game_menu = tk.Menu(gui_menu)
gui_menu.add_cascade(label="Game", menu=game_menu)
for gi in range(len(games)):
    game_menu.add_radiobutton(label=games[gi].game_name, variable=game_index, value=gi, command=game_changer)
game_changer()

root.mainloop()

