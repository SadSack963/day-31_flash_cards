import tkinter as tk
from tkinter import messagebox
import pandas
from random import randint, choice


BACKGROUND_COLOR = "#B1DDC6"
CARD_WIDTH = 800
CARD_HEIGHT = 526
CANVAS_WIDTH = 825
CANVAS_HEIGHT = 550
title_font = ("Arial", 32, "italic")
word_font = ("Arial", 48, "bold")
data_file = "./data/german_words.csv"


# ---------------- Read Words from file -------------------

def read_data():
    try:
        # Ensure csv file has Byte Order Mark (BOM) = big-endian for utf-16
        # i.e. The first two words of the file = 0xFFFE
        with open(data_file, mode="r", encoding="utf-16") as file:
            data_frame = pandas.read_csv(file)
            # print(data_frame)
    except FileNotFoundError:
        messagebox.showinfo(parent=window, title="Error", message=f"The data file {data_file} could not be found.")
    else:
        # required format: [{foreign_word: english_word}, ...]
        # data_list = [{row.German: row.English} for (index, row) in data_frame.iterrows()]
        # >>> [{'Ich': 'I'}, {'ist': 'is'}, {'ich': 'I'}, ...]

        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
        data_list = data_frame.to_dict(orient="records")
        print(data_list)
        # >>> [{'German': 'Ich', 'English': 'I'}, {'German': 'ist', 'English': 'is'}, ... ]


# ---------------- Pick a random word -------------------



# ---------------- UI Setup -------------------

window = tk.Tk()
window.title("German Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)


canvas_card = tk.Canvas(bg=BACKGROUND_COLOR, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0)
image_front = tk.PhotoImage(file="./images/card_front.png")
canvas_card.create_image(424, 287, image=image_front)
title = canvas_card.create_text(400, 150, text="Title", font=title_font)
foreign_word = canvas_card.create_text(400, 263, text="ABCDEFGHIJKLMNOP", font=word_font)

image_wrong = tk.PhotoImage(file="./images/wrong.png")
button_wrong = tk.Button(image=image_wrong, relief="flat", borderwidth=0, highlightthickness=0)
image_right = tk.PhotoImage(file="./images/right.png")
button_right = tk.Button(image=image_right, relief="flat", borderwidth=0, highlightthickness=0)


# Grid layout
canvas_card.grid(row=0, column=0, columnspan=2)
button_wrong.grid(row=1, column=0)
button_right.grid(row=1, column=1)

read_data()


# -----------------------------------

window.mainloop()