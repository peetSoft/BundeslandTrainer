# from main import input_user
import tkinter as tk
from base_quiz import Quiz
from data_state_capital import quan, mnemonics, synonyms, generic_term_1, generic_term_2


def send(event=None):
    if answer != "":
        user_answer = user_entry.get()
        user_answer_canonic = quiz.get_canonic(user_answer)
        global positive_counter, negative_counter

        if user_answer_canonic == answer:
            positive_counter += 1
            valuation.config(text=answer + " : Das ist richtig")
        else:
            negative_counter += 1
            valuation.config(text="Falsch! \n\n Richtige Antwort ist:" + answer + "\n \n Eselsbrücke=" + mnemonic)
        print(negative_counter, positive_counter)

        user_entry.delete(0, "end")
    next_question()


def next_question():
    global answer, mnemonic
    generic_term, question, answer, mnemonic = quiz.next_question()
    next_label.config(text="Nächste Frage: Geben sie " + generic_term + " von " + question + " ein: ")


game_state = True

positive_counter = 0
negative_counter = 0

answer = ""
mnemonic = ""

quiz = Quiz(quan, generic_term_1, generic_term_2, synonyms, mnemonics)
root = tk.Tk()
root.geometry("1000x400")

# start_stop_button = tk.Button(root, text="Start", command=start_stop)
# next_button = tk.Button(root, text='Nächste Frage', command=next_question)
welcome_label = tk.Label(root, text="Willkommen zum Spiel - Drücken sie Enter zum starten.")
next_label = tk.Label(root, text='', font=18)
user_entry = tk.Entry(root)
send_button = tk.Button(root, text="Absenden", command=send)
valuation = tk.Label(root)

# start_stop_button.pack()
# next_button.pack()
welcome_label.pack(pady=10)
next_label.pack(pady=10)
user_entry.pack(pady=10)
send_button.pack(pady=10)
valuation.pack(pady=10)

# root.bind('s', start_stop)
# root.bind('r', start_stop)
root.bind('<Return>', send)
root.mainloop()
