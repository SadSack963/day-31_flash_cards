import tkinter as tk
from tkinter import messagebox
import pandas
from random import choice
import os

# Audio suggested by HUGO https://www.udemy.com/course/100-days-of-code/learn/#questions/14256878
from gtts import gTTS  # Google Text-to-Speech
import playsound


BACKGROUND_COLOR = "#B1DDC6"
CARD_WIDTH = 800
CARD_HEIGHT = 526
CANVAS_WIDTH = 825
CANVAS_HEIGHT = 550
title_font = ("Arial", 32, "italic")
word_font = ("Arial", 48, "bold")

french_csv = "./data/french_words.csv"
french_encoding = "uft-8"
german_csv = "./data/german_words.csv"
german_encoding = "utf-16"

word_list = []
random_dict = {}
foreign_word = ""
english_word = ""
language_0 = ""
language_1 = ""


def close_app():
    exit()


def read_data(data_file, encoding):
    """Read the word list, and save it to remaining words to be learned.
    If there is a file containing words to be learned then use that,
    otherwise use the entire word list."""
    global word_list, language_0, language_1
    if os.path.exists("./data/german_words_remaining.csv"):
        data_file = "./data/german_words_remaining.csv"
    try:
        # Ensure csv file has Byte Order Mark (BOM) = big-endian for utf-16
        # i.e. The first four bytes in the file = 0xFFFE
        data_frame = pandas.read_csv(data_file, encoding=encoding)
    except FileNotFoundError:
        messagebox.showinfo(parent=window, title="Error", message=f"The data file {data_file} could not be found.")
    else:
        # Pandas .to_dict()
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
        word_list = data_frame.to_dict(orient="records")
        language_0 = data_frame.columns[0]
        language_1 = data_frame.columns[1]
        save_words()


def remove_word():
    """Remove learnt words from the list of remaining words.
    Save the remaining words and display the next card.
    If there are no more words, then display messagebox and exit"""
    if len(word_list) >= 1:
        word_list.remove(random_dict)
        save_words()
    if len(word_list) != 0:
        display_card_front()
    else:
        messagebox.showinfo(parent=window, title="Complete", message=f"Well done!\nYou have completed the Flash Cards.")
        if os.path.exists("./data/german_words_remaining.csv"):
            os.remove("./data/german_words_remaining.csv")
        window.after(500, close_app)


def save_words():
    """Save remaining words to learn to CSV"""
    # Convert list of dictionaries to Pandas DataFrame
    df = pandas.DataFrame.from_records(word_list)
    # Write to CSV
    df.to_csv("./data/german_words_remaining.csv", index=False, encoding=german_encoding)


def display_card_front():
    """Display the card front with the foreign word"""
    global word_list, random_dict, foreign_word, english_word, flip_timer
    button_right["state"] = "disabled"
    button_wrong["state"] = "disabled"
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

    # Play Audio of word using Google Text-to-Speech
    audio_output = gTTS(text=foreign_word, lang="de")
    audio_output.save("foreign_word.mp3")
    playsound.playsound("foreign_word.mp3", True)
    os.remove("foreign_word.mp3")

    flip_timer = window.after(5000, func=display_card_back)


def display_card_back():
    """Display the card back with the English word"""
    button_right["state"] = "active"
    button_wrong["state"] = "active"
    # Change the word on the card - English
    canvas_card.itemconfig(canvas_title, text=language_1, fill="white")
    canvas_card.itemconfig(canvas_word, text=english_word, fill="white")
    canvas_card.itemconfig(canvas_image, image=image_back)

    # Play Audio of word using Google Text-to-Speech
    audio_output = gTTS(text=english_word, lang="en")
    audio_output.save("english_word.mp3")
    playsound.playsound("english_word.mp3", True)
    os.remove("english_word.mp3")


# ---------------- UI Setup -------------------

window = tk.Tk()
window.title("Language Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=display_card_back)

canvas_card = tk.Canvas(
    bg=BACKGROUND_COLOR,
    width=CANVAS_WIDTH,
    height=CANVAS_HEIGHT,
    highlightthickness=0
)
image_front = tk.PhotoImage(file="./images/card_front.png")
image_back = tk.PhotoImage(file="./images/card_back.png")
canvas_image = canvas_card.create_image(424, 287, image=image_front)
canvas_title = canvas_card.create_text(400, 150, text="Title", font=title_font)
canvas_word = canvas_card.create_text(400, 263, text="ABCDEFGHIJKLMNOP", font=word_font)

image_wrong = tk.PhotoImage(file="./images/wrong.png")
button_wrong = tk.Button(
    image=image_wrong,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=display_card_front
)
image_right = tk.PhotoImage(file="./images/right.png")
button_right = tk.Button(
    image=image_right,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=remove_word
)


# Grid layout
canvas_card.grid(row=0, column=0, columnspan=2)
button_wrong.grid(row=1, column=0)
button_right.grid(row=1, column=1)


# canvas_title.config(text="French")
# word_list = read_data(french_csv, french_encoding)
# display_card_front("fr")

canvas_card.itemconfig(canvas_title, text="German")
read_data(german_csv, german_encoding)
display_card_front()


# -----------------------------------

window.mainloop()
