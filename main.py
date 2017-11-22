from tkinter import *
import evaluation_function
import compare_source
import urllib.request

# Formatting GUI

root = Tk()
root.resizable(width=False, height=False)
root.minsize(width=300, height=200)
root.configure(background='cadet blue')
root.attributes("-topmost", True)

# Button function, takes input and stores string as txt file


def callback():
    url_received = enter_1.get()
    with open('URL.txt', 'w') as url_file:
        url_file.write(url_received)

# Button function, takes string from txt file, runs engine eval from import function, updates label with results


def evaluation():
    url_location = open('URL.txt', 'r')
    game_url = url_location.read()
    best_move = evaluation_function.evaluation_function(game_url)[0]
    best_line = evaluation_function.evaluation_function(game_url)[1]
    label_4.config(text=best_move)
    label_6.config(text=best_line)
    root.after(400, looper)

# Loops code after analysis until lichess.org update, then call evaluation


def looper():
    url_location = open('URL.txt', 'r')
    game_url = url_location.read()
    control = 0
    if control == 0:
        urllib.request.urlretrieve(game_url, "compare.txt")
        control = compare_source.file_compare('raw.txt', 'compare.txt')
        if control == 0:
            root.after(400, looper)
        elif control == 1:
            return evaluation()
    else:
        print('Goodbye')

# Setting up labels/buttons


label_1 = Label(text="LiChess Position Eval v1.0")
label_1.grid(row=0, column=0)

label_2 = Label(text='Input LiChess URL')
label_2.grid(row=3, column=0, pady=20)

label_3 = Label(text='Best move:', font=16)
label_3.grid(row=4, column=0)

label_4 = Label(text="N/A", font=16)
label_4.grid(row=4, column=1)

label_5 = Label(text='Line:')
label_5.grid(row=5, column=0, pady=30)

label_6 = Label(text='N/A', width=30)
label_6.grid(row=5, column=1)

enter_1 = Entry(root)
enter_1.grid(row=3, column=1)

button_1 = Button(root, text="Submit", command=callback)
button_1.grid(row=3, column=2, padx=10)

button_2 = Button(root, text='Start', command=evaluation)
button_2.grid(row=6, column=2)


# Loop the GUI

root.mainloop()
