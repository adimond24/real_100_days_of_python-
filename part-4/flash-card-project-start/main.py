from dataclasses import dataclass
from tkinter import *
import pandas
import random
from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")




def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card_img)
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=back_card_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



canvas = Canvas(width=800, height=526)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=front_card_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word=canvas.create_text(300, 263, text="word", font=("Ariel",60,"bold" ))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image = wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()


back_image = PhotoImage(file="images/card_back.png")







window.mainloop()