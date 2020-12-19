from tkinter import *
import pandas
from random import randint, choice

BACKGROUND_COLOR = "#B1DDC6"


data_frame = pandas.read_csv("data/french_words.csv")
# print(data_frame)
to_learn = data_frame.to_dict(orient="records")
# print(data_list)
# >>> [{'German': 'Ich', 'English': 'I'}, {'German': 'ist', 'English': 'is'}, ... ]


def next_card():
    current_card = choice(to_learn)
    foreign_word = current_card["French"]
    english_word = current_card["English"]
    # Change the word on the card
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=foreign_word)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

image_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=image_wrong, relief="flat", pady=5, borderwidth=0, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)

image_right = PhotoImage(file="./images/right.png")
button_right = Button(image=image_right, relief="flat", pady=5, borderwidth=0, highlightthickness=0, command=next_card)
button_right.grid(row=1, column=1)

next_card()


window.mainloop()
