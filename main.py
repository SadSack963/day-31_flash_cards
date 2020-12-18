import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
CARD_WIDTH = 800
CARD_HEIGHT = 526
CANVAS_WIDTH = 825
CANVAS_HEIGHT = 550
title_font = ("Arial", 32, "italic")
word_font = ("Arial", 48, "bold")


# ---------------- UI Setup -------------------

window = tk.Tk()
window.title("German Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)


frame_card = tk.Frame(window, bg=BACKGROUND_COLOR, bd=0)
canvas_card = tk.Canvas(frame_card, bg=BACKGROUND_COLOR, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, highlightthickness=0)
image_front = tk.PhotoImage(file="./images/card_front.png")
canvas_card.create_image(424, 287, image=image_front)
label_title = tk.Label(frame_card, text="Title\n", bg="white", font=title_font)
label_word = tk.Label(frame_card, text="ABCDEFGHIJKLMNOP\n", bg="white", width=18, font=word_font)

frame_buttons = tk.Frame(window, bg=BACKGROUND_COLOR, bd=0)
canvas_buttons = tk.Canvas(frame_buttons, bg=BACKGROUND_COLOR, height=110, width=CANVAS_WIDTH, highlightthickness=0)
image_wrong = tk.PhotoImage(file="./images/wrong.png")
button_wrong = tk.Button(frame_buttons, image=image_wrong, relief="flat", pady=5, borderwidth=0, highlightthickness=0)
label_blank = tk.Label(frame_buttons, text="         ", bg=BACKGROUND_COLOR, height=0, font=word_font)
image_right = tk.PhotoImage(file="./images/right.png")
button_right = tk.Button(frame_buttons, image=image_right, relief="flat", pady=5, borderwidth=0, highlightthickness=0)


# Grid layout
frame_card.grid(row=0, column=0)
canvas_card.grid(row=0, column=0, rowspan=2)
label_title.grid(row=0, column=0, sticky=tk.S)
label_word.grid(row=1, column=0, sticky=tk.N)

frame_buttons.grid(row=1, column=0)
canvas_buttons.grid(row=0, column=0, columnspan=3)
button_wrong.grid(row=0, column=0, sticky=tk.E)
label_blank.grid(row=0, column=1)
button_right.grid(row=0, column=2, sticky=tk.W)


# -----------------------------------

window.mainloop()