import tkinter as tk
from base_quiz import Quiz
from games_data import create_game_collection

"""
The game can be in 4 different states: 
state1 = Game Start
state2 = The question is asked
state3 = Answer inputted by user
state4 = Evaluation of the user answers
"""

def set_state1(event=None):
    """

    """

    global state, positive_counter, negative_counter
    next_question_text.config(text="")
    user_entry.config(state="disabled")
    question_valuation_text.config(text="")
    mnemonic_text.config(text="")
    counter_right_text.config(text="")
    counter_wrong_text.config(text="")
    user_evaluation_text.config(text="")
    hint_text.config(text="Starten sie das Spiel mit Enter oder Senden")
    positive_counter = negative_counter = 0
    state = 1
    state_text.config(text=state)


def set_state2():
    global state
    next_question_text.config(text=str(negative_counter + positive_counter + 1) + "." + next_question())
    user_entry.config(state='normal')
    user_entry.focus_force()
    question_valuation_text.config(text="")
    mnemonic_text.config(text="")
    counter_right_text.config(text=str(positive_counter))
    counter_wrong_text.config(text=str(negative_counter))
    user_evaluation_text.config(text="")
    hint_text.config(text="Geben Sie eine Antwort ein, und bestätigen Sie mit Absenden oder Enter")
    state = 2
    user_entry.delete(0, "end")
    state_text.config(text=state)


def set_state3():
    global state, positive_counter, negative_counter
    # next_question_text.config(text=next_question())  # im next_question_label wird text2 ausgespielt.
    user_entry.config(state='disabled', )
    user_answer = user_entry.get()
    user_answer_canonic = quiz.get_canonic(user_answer)
    if user_answer_canonic == machine_answer:
        positive_counter += 1
        counter_right_text.config(text=str(positive_counter))
        question_valuation_text.config(text=machine_answer + " : Das ist richtig")
    else:
        negative_counter += 1
        counter_wrong_text.config(text=str(negative_counter))
        question_valuation_text.config(text="Falsch!  Richtige Antwort ist:" + machine_answer)

        mnemonic_text.config(text=mnemonic)
    user_evaluation_text.config(text="")
    if positive_counter + negative_counter == total_tries:
        hint_text.config(text="Enter oder Absenden für Ihre Bewertung")
    else:
        hint_text.config(text="Enter oder Absenden für nächste Frage")
    state = 3
    state_text.config(text=state)


def set_state4():
    global state, positive_counter, negative_counter
    next_question_text.config(text="")
    user_entry.config(state='disabled')

    question_valuation_text.config(text="")
    mnemonic_text.config(text="")
    result = 100 * positive_counter / total_tries
    if result < 30:
        user_evaluation_text.config(text="Starke Bildungslücke!")
    elif result < 70:
        user_evaluation_text.config(text="Das muss besser werden!")
    else:
        user_evaluation_text.config(text="Sehr stark!")

    hint_text.config(text="Für ein neues Spiel drücken Sie Enter.")
    positive_counter = negative_counter = 0
    state = 4
    state_text.config(text=state)


def send(event=None):
    """
    Picks one state of the game.
    :param event:
    :return:
    """
    global state
    if state == 1:
        set_state2()
    elif state == 2:
        set_state3()
    elif state == 3:
        if positive_counter + negative_counter == total_tries:
            set_state4()
        else:
            set_state2()
    elif state == 4:
        set_state2()


def next_question():
    """

    :return: txt2
    """
    global machine_answer, mnemonic
    generic_term, question, machine_answer, mnemonic = quiz.next_question()
    txt = quiz.general_question
    txt1 = txt.replace("#generic#", generic_term)  # Was wird hier warum replaced ?
    txt2 = txt1.replace("#question#", question)
    return txt2


def game_changer(index= None):
    global quiz, current_game_name_label, games
    if index is not None:
        game_index.set(index)
    game = games[game_index.get()]
    current_game_name_label.config(text=game.game_name)
    quiz.config(game.quan, game.general_question, game.generic_term_1, game.generic_term_2,
                game.synonyms, game.mnemonics)
    set_state1()
    state_text.config(text=state)


state = 1
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
row9 = tk.Frame(root)

# Parameters as dictionary
title_style_parameters = {"bg": "#ff9933", "font": 18, "width": 11, "anchor": "w"}
text_style_parameters = {'bg': text_color, 'font': 18, 'width': text_width, 'anchor': "w"}

# Labels Entrys Button (text,size,fonts,bg)
current_game_name_label = tk.Label(row0, bg="#5d6d7e", font=20)

next_question_title = tk.Label(row1, text='Frage: ', **title_style_parameters)
next_question_text = tk.Label(row1, text='', **text_style_parameters)

user_answer_title = tk.Label(row2, text="Antwort: ", **title_style_parameters)
user_entry = tk.Entry(row2, width=40, state="disabled")
send_button = tk.Button(row2, text="Absenden", command=send, bg="#ffffcc",
                        width=10)  ## Absenden in der GUI löst send() aus

question_valuation_title = tk.Label(row3, text="Resultat: ", **title_style_parameters)
question_valuation_text = tk.Label(row3, **text_style_parameters)

mnemonic_title = tk.Label(row4, text="Eselsbrücke ", **title_style_parameters)
mnemonic_text = tk.Label(row4, text='', **text_style_parameters)

counter_right_title = tk.Label(row5, text="Richtig: ", **title_style_parameters)
counter_right_text = tk.Label(row5, text=str(positive_counter), width=3, bg=text_color)

counter_wrong_title = tk.Label(row6, text="Falsch: ", **title_style_parameters)
counter_wrong_text = tk.Label(row6, text=str(negative_counter), width=3, bg=text_color)

user_evaluation_title = tk.Label(row7, text="Auswertung", **title_style_parameters)
user_evaluation_text = tk.Label(row7, **text_style_parameters)

hint_text = tk.Label(row8, text='Hint', bg="#c2d6d6", font=("Courier", 10, "italic"), width=text_width + 20, anchor="w")
state_text = tk.Label(row8, text=str(state), font=("Courier", 10, "italic"))
cancel_button = tk.Button(row9, text="Abbrechen", bg="#ffffcc", width=10, command=set_state1)
quit_button = tk.Button(row9, text="Beenden", bg="#ffffcc", width=10, command=root.destroy)
# Layout-Manager
# Frames .pack2 row0.pack(pady=(10, 10))
row0.pack(fill="x", pady=(10, 10))
row1.pack(fill="x", pady=(10, 10))
row2.pack(fill="x", pady=(10, 10))
row3.pack(fill="x", pady=(10, 10))
row4.pack(fill="x", pady=(10, 10))
row5.pack(fill="x", pady=(10, 10))
row6.pack(fill="x", pady=(10, 10))
row7.pack(fill="x", pady=(10, 10))
row8.pack(fill="x", pady=(10, 10))
row9.pack(fill="x", pady=(10, 10))

title_pack_parameter = {"side": "left", "anchor": "w", "padx": (0, 40)}

# Labels, Entry, Button, .pack
current_game_name_label.pack()
next_question_title.pack(**title_pack_parameter)
next_question_text.pack(side="left", anchor="w")
user_answer_title.pack(**title_pack_parameter)
user_entry.pack(side="left", anchor="w")
send_button.pack(side="left", anchor="w", padx=(60, 0))
question_valuation_title.pack(**title_pack_parameter)
question_valuation_text.pack(**title_pack_parameter)
counter_right_title.pack(**title_pack_parameter)
counter_wrong_title.pack(side="left", anchor="w", padx=(0, 40))
counter_right_text.pack(**title_pack_parameter)
counter_wrong_text.pack(**title_pack_parameter)
mnemonic_title.pack(**title_pack_parameter)
mnemonic_text.pack(side="left", anchor="w", padx=(0, 40))
user_evaluation_title.pack(**title_pack_parameter)
user_evaluation_text.pack(side="left", anchor="w")
hint_text.pack(side="left", anchor="w")
state_text.pack(side="left", padx=10)
cancel_button.pack(side="left", anchor="w", padx=(413, 10))
quit_button.pack(side="left", anchor="w")

# Hover over Buttons
send_button.bind("<Enter>", lambda e: send_button.config(text="(Enter)"))
send_button.bind("<Leave>", lambda e: send_button.config(text="Absenden"))

cancel_button.bind("<Enter>", lambda e: cancel_button.config(text="(Esc)"))
cancel_button.bind("<Leave>", lambda e: cancel_button.config(text="Abbrechen"))

quit_button.bind("<Enter>", lambda e: quit_button.config(text="(Strg+X)"))
quit_button.bind("<Leave>", lambda e: quit_button.config(text="Beenden"))

root.bind('<Return>', send)
root.bind('<Control-x>', lambda e: root.destroy())
root.bind('<Escape>', set_state1)
# Menu
gui_menu = tk.Menu(root)
root.config(menu=gui_menu)

gi, games = create_game_collection()
game_index = tk.IntVar(value=gi)

game_menu = tk.Menu(gui_menu)
gui_menu.add_cascade(label="Game", menu=game_menu)
for gi in range(len(games)):
    game_menu.add_radiobutton(label=games[gi].game_name, variable=game_index, value=gi, command=game_changer)
    key = '<Control-Key-' + str(gi + 1) + '>'
    root.bind(key, lambda e: game_changer(gi))

game_changer()

# set_state1()
root.mainloop()
