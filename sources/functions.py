my_questions = [ "q3"]

my_delay_pipe = [None, None, None]


def delay_pipe_update(questions, delay_pipe, question):  
    try:
        i = questions.index(question)
        x = questions.pop(i)
    except ValueError:
        x = None
    delay_pipe.append(x)
    y = delay_pipe.pop(0)
    if y is not None:
        questions.append(y)


delay_pipe_update(my_questions, my_delay_pipe, "q3")
print(my_questions)
print(my_delay_pipe)
delay_pipe_update(my_questions, my_delay_pipe, "q3")
print(my_questions)
print(my_delay_pipe)
delay_pipe_update(my_questions, my_delay_pipe, "q3")
print(my_questions)
print(my_delay_pipe)
delay_pipe_update(my_questions, my_delay_pipe, "q3")
print(my_questions)
print(my_delay_pipe)
delay_pipe_update(my_questions, my_delay_pipe, "q3")
print(my_questions)
print(my_delay_pipe)
delay_pipe_update(my_questions, my_delay_pipe, "q3")
print(my_questions)
print(my_delay_pipe)
