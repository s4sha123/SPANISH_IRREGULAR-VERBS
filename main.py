
from tkinter import *
import pandas as pd
import random

# Get the data
data = pd.read_csv("words/Spanish_irregularverbs.csv")
language_data = data.to_dict(orient="records")
current_word = {}


def next_card():
    """This function displays the spanish word to the user"""
    global current_word
    current_word = random.choice(language_data)
    canvas.itemconfig(language, text="Spanish", fill="black")
    canvas.itemconfig(word, text=current_word["Spanish"], fill="black")
    canvas.itemconfig(card_image, image=front_image)


def flip_card():
    """This function displays the english equivalent of the word"""
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")
    canvas.itemconfig(card_image, image=back_image)


def known_words():
    language_data.remove(current_word)
    print(len(language_data))
    next_card()


BACKGROUND_COLOR = "#F6ECF5"

# Setup the User interface
interface = Tk()
interface.title("IRREGULAR SPANISH VERBS FLASHCARDS")
interface.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Add front card image using canvas widget
canvas = Canvas(width=340, height=210)
front_image = PhotoImage(file="flash_cards/front.png")
back_image = PhotoImage(file="flash_cards/back.png")
card_image = canvas.create_image(170, 105, image=front_image)
settings = canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language = canvas.create_text(170, 55, text="", font=("Arial", 30, "normal"))
word = canvas.create_text(170, 140, text="", font=("Arial", 39, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

cross = PhotoImage(file="checker/unknown.png")
unknown_button = Button(image=cross, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check = PhotoImage(file="checker/known.png")
known_button = Button(image=check, highlightthickness=0, command=known_words)
known_button.grid(column=1, row=1)

flip_button = Button(text="Flip Card", font=("Arial", 15, "normal"), command=flip_card)
flip_button.config(padx=10, pady=10, highlightthickness=0)
flip_button.grid(column=0, columnspan=2,  row=2)

next_card()

# Keeps the interface open until exited
interface.mainloop()
