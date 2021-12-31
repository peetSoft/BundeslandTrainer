from base_quiz import Quiz
from games_data import create_game_collection

index, games_data = create_game_collection()

for i in range(len(games_data)):
    print(f"{i + 1}. {games_data[i].game_name}")

game_number = int(input("Welches Spiel möchten sie spielen? (Nummer eingeben):"))

quiz_data = games_data[game_number - 1]

quiz = Quiz()
quiz.config(quiz_data.quan, quiz_data.general_question, quiz_data.generic_term_1, quiz_data.generic_term_2,
            quiz_data.synonyms, quiz_data.mnemonics)

try_number = 10
counter = 0
for i in range(try_number):

    answer_generic_term, question, machine_answer, mnemonic = quiz.next_question()
    input_user = input("Geben sie " + answer_generic_term + " von " + question + " ein: ")
    input_user1 = quiz.get_canonic(input_user)

    if input_user1 == machine_answer:
        counter += 1
        print("Das ist richtig")
    else:
        if mnemonic:
            hint = ' // Eselsbrücke: ' + mnemonic
        else:
            hint = ''
        print("Falsch: " + machine_answer + hint)

percentage = 100 * counter / try_number
print('--------------------')
print("Ihr Ergebniss " + str(percentage) + "%")

if percentage <= 25:
    print("Achtung starke Bildungslücke ! ")
elif percentage <= 50:
    print("Das muss besser gehen !")
elif percentage <= 75:
    print("Nicht schlecht !")
else:
    print("Alter Schlaumeier ! ")
