from tkinter import *
import pandas
from random import randint, choice

BACKGROUND_COLOR = "#B1DDC6"
current_card={}

data_frame = pandas.read_csv("data/french_words.csv")
# print(data_frame)
to_learn = data_frame.to_dict(orient="records")
# print(data_list)
# >>> [{'German': 'Ich', 'English': 'I'}, {'German': 'ist', 'English': 'is'}, ... ]


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
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
