import tkinter as tk
from tkinter import messagebox
import pandas
from random import randint, choice
import time


BACKGROUND_COLOR = "#B1DDC6"
CARD_WIDTH = 800
CARD_HEIGHT = 526
CANVAS_WIDTH = 825
CANVAS_HEIGHT = 550
title = "German"
title_font = ("Arial", 32, "italic")
word_font = ("Arial", 48, "bold")
french_csv = "./data/french_words.csv"
french_encoding = "uft-8"
german_csv = "./data/german_words.csv"
german_encoding = "utf-16"
foreign_word = ""
english_word = ""
language_0 = ""
language_1 = ""


# ---------------- Read Words from file -------------------

def read_data(data_file, encoding):
    try:
        # Ensure csv file has Byte Order Mark (BOM) = big-endian for utf-16
        # i.e. The first two words of the file = 0xFFFE
        # NOTE: No need to open the file when using Pandas
        # with open(data_file, mode="r", encoding=encoding) as file:
        data_frame = pandas.read_csv(data_file, encoding=encoding)
        # print(data_frame)
    except FileNotFoundError:
        messagebox.showinfo(parent=window, title="Error", message=f"The data file {data_file} could not be found.")
    else:
        global language_0, language_1
        # Pandas .to_dict()
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
        data_list = data_frame.to_dict(orient="records")
        language_0 = data_frame.columns[0]
        language_1 = data_frame.columns[1]
        return data_list


def pick_word():
    global foreign_word, english_word, flip_timer
    # Cancel event timer if a new word is selected
    window.after_cancel(flip_timer)
    # Get a random word
    random_dict = choice(word_list)
    foreign_word = random_dict[language_0]
    english_word = random_dict[language_1]
    # Change the word on the card - German
    canvas_card.itemconfig(canvas_title, text=language_0, fill="black")
    canvas_card.itemconfig(canvas_word, text=foreign_word, fill="black")
    canvas_card.itemconfig(canvas_image, image=image_front)
    flip_timer = window.after(5000, func=display_card_back)


def display_card_back():
    # Change the word on the card - English
    canvas_card.itemconfig(canvas_title, text=language_1, fill="white")
    canvas_card.itemconfig(canvas_word, text=english_word, fill="white")
    canvas_card.itemconfig(canvas_image, image=image_back)


# ---------------- UI Setup -------------------

window = tk.Tk()
window.title("Language Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=display_card_back)

canvas_card = tk.Canvas(bg=BACKGROUND_COLOR, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0)
image_front = tk.PhotoImage(file="./images/card_front.png")
image_back = tk.PhotoImage(file="./images/card_back.png")
canvas_image = canvas_card.create_image(424, 287, image=image_front)
canvas_title = canvas_card.create_text(400, 150, text=title, font=title_font)
canvas_word = canvas_card.create_text(400, 263, text="ABCDEFGHIJKLMNOP", font=word_font)

image_wrong = tk.PhotoImage(file="./images/wrong.png")
button_wrong = tk.Button(image=image_wrong, relief="flat", borderwidth=0, highlightthickness=0, command=pick_word)
image_right = tk.PhotoImage(file="./images/right.png")
button_right = tk.Button(image=image_right, relief="flat", borderwidth=0, highlightthickness=0, command=pick_word)


# Grid layout
canvas_card.grid(row=0, column=0, columnspan=2)
button_wrong.grid(row=1, column=0)
button_right.grid(row=1, column=1)


# canvas_title.config(text="French")
# word_list = read_data(french_csv, french_encoding)
canvas_card.itemconfig(canvas_title, text="German")
word_list = read_data(german_csv, german_encoding)
pick_word()


# -----------------------------------

window.mainloop()