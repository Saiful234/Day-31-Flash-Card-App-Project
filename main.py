from tkinter import *

import pandas
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)
word = {}
data_dict_file = {}

try:
    data_file = pd.read_csv("data/words_to_learn.csv")
    print(data_file)
except FileNotFoundError:
    raw_data = pandas.read_csv("data/french_words.csv")
    data_dict_file = raw_data.to_dict(orient="records")
else:
    data_dict_file = data_file.to_dict(orient="records")
    print(data_dict_file)

def pick_a_word():
    global word, flip_time
    window.after_cancel(flip_time)
    word = random.choice(data_dict_file)
    canvas.itemconfig(text_title, text="French", fill="black")
    canvas.itemconfig(guess_text, text=word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_time = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(text_title, text="English", fill="white")
    canvas.itemconfig(guess_text, text=word["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_image)

def is_known():
    data_dict_file.remove(word)
    print(len(data_dict_file))
    data = pandas.DataFrame(data_dict_file)
    data.to_csv("data/words_to_learn.csv", index=False)
    pick_a_word()

flip_time = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
text_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
guess_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


tick_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
tick_button = Button(image=tick_image,bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=pick_a_word)
wrong_button.grid(column=0, row=1)
tick_button.grid(column=1, row=1)
pick_a_word()
window.mainloop()