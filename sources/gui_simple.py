import tkinter as tk
from base_quiz import Quiz
from bundestrainer import quan, mnemonics, synonyms, generic_term_1, generic_term_2

game_state = True


def start_stop(event=None):
    global game_state
    print(event.char)
    game_state = not game_state
    if game_state:
        name = "Stop"
    else:
        name = "Start"
    start_stop_button.config(text=name)


def next_question():
    generic_term, question, answer, mnemonic = quiz.next_question()
    next_label.config(text="Geben sie " + generic_term + " von " + question + " ein: ")


quiz = Quiz(quan, generic_term_1, generic_term_2, synonyms, mnemonics)
root = tk.Tk()

start_stop_button = tk.Button(
    text="Start",
    command=start_stop
)
start_stop_button.pack()

next_button = tk.Button(
    text='Nächste Frage',
    command=next_question
)
next_button.pack()

next_label = tk.Label(
    text=''
)
next_label.pack()

root.bind('s', start_stop)
root.bind('r', start_stop)

root.mainloop()
