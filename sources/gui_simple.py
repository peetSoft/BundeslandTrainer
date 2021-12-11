# from main import input_user
import tkinter as tk
from base_quiz import Quiz
from data_state_capital import quan, mnemonics, synonyms, generic_term_1, generic_term_2


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
            question_valuation_label.config(text="Falsch!  Richtige Antwort ist:" + machine_answer + " Eselsbrücke=" + mnemonic)

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
            welcome_label.config(text="Für ein neues Spiel Enter drücken!")
            user_entry.config(state="disabled")
            question_valuation_label.config(text="")
            next_question_label.config(text="")
            machine_answer = ""
            return
        next_question()
    else:
        welcome_label.config(text="")
        counter_count_label.config(text="")
        user_evaluation_label.config(text="")
        user_entry.config(state="normal")
        next_question()

def next_question():
    global machine_answer, mnemonic
    generic_term, question, machine_answer, mnemonic = quiz.next_question()
    next_question_label.config(text="Nächste Frage: Geben sie " + generic_term + " von " + question + " ein: ")


game_state = True

positive_counter = 0
negative_counter = 0
total_tries = 3

machine_answer = ""
mnemonic = ""

quiz = Quiz(quan, generic_term_1, generic_term_2, synonyms, mnemonics)
root = tk.Tk()
root.geometry("1000x400")

welcome_label = tk.Label(root, text="Willkommen zum Spiel - Drücken sie Enter zum starten."
                         , bg="#5d6d7e"
                         )
next_question_label = tk.Label(root, text='', font=18)
send_button = tk.Button(root, text="Absenden", command=send)
user_entry = tk.Entry(root, state="disabled")
question_valuation_label = tk.Label(root)
counter_count_label = tk.Label(root)
user_evaluation_label = tk.Label(root)

welcome_label.grid(row=0, column=0, pady=10, sticky="W")
next_question_label.grid(row=1, pady=10, sticky="W")
send_button.grid(row=2, column=0, padx=20, pady=10, sticky="W")
user_entry.grid(row=3, column=0, pady=10, sticky="W")
question_valuation_label.grid(row=4, column=0, pady=10, sticky="W")
counter_count_label.grid(row=5, column=0, sticky="W")
user_evaluation_label.grid(row=6, column=0, sticky="W")

root.bind('<Return>', send)
root.mainloop()
