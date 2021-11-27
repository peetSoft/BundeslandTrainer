import tkinter as tk

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


root = tk.Tk()

start_stop_button = tk.Button(
    text="Start",
    command=start_stop
)
start_stop_button.pack()
root.bind('s', start_stop)
root.bind('r', start_stop)

root.mainloop()
