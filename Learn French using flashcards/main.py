from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
timer = None

# Set base path to the script's location
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
IMG_DIR = os.path.join(BASE_DIR, "images")

# Load data
try:
    data_path = os.path.join(DATA_DIR, "words_to_learn.csv")
    data = pandas.read_csv(data_path)
except FileNotFoundError:
    french_path = os.path.join(DATA_DIR, "french_words.csv")
    original_data = pandas.read_csv(french_path)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def flip_card():
    canva.itemconfig(flash_card, image=card_back_img)
    canva.itemconfig(lang_title, text="English", fill="white")
    canva.itemconfig(word, text=current_card["English"], fill="white")


def next_card():
    global current_card, timer

    window.after_cancel(timer)
    current_card = random.choice(to_learn)

    canva.itemconfig(flash_card, image=card_front_img)
    canva.itemconfig(lang_title, text="French", fill="black")
    canva.itemconfig(word, text=current_card["French"], fill="black")
    timer = window.after(3000, flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(os.path.join(DATA_DIR, "words_to_learn.csv"), index=False)
    next_card()


# UI setup
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_front_img = PhotoImage(file=os.path.join(IMG_DIR, "card_front.png"))
card_back_img = PhotoImage(file=os.path.join(IMG_DIR, "card_back.png"))
right_image = PhotoImage(file=os.path.join(IMG_DIR, "right.png"))
wrong_image = PhotoImage(file=os.path.join(IMG_DIR, "wrong.png"))

timer = window.after(3000, flip_card)

canva = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card = canva.create_image(400, 263)
lang_title = canva.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canva.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canva.grid(row=0, column=0, columnspan=2)

wrong_btn = Button(image=wrong_image, command=next_card, borderwidth=0, highlightthickness=0, pady=20)
wrong_btn.grid(row=1, column=0)

right_btn = Button(image=right_image, command=is_known, borderwidth=0, highlightthickness=0, pady=20)
right_btn.grid(row=1, column=1)

next_card()

window.mainloop()
