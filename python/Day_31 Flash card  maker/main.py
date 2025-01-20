from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# ----------------------- Getting words from csv ----------------------- #
try:
    data = pandas.read_csv("data/word to learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ----------------------- generating new card ----------------------- #
def next_card():
    global flip_timer
    global current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_bg, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


# ----------------------- Flipping card ----------------------- #
def flip_card():
    global current_card
    canvas.itemconfig(card_bg, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ----------------------- Known words handling ----------------------- #
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/word to learn.csv", index=False)
    next_card()


# ----------------------- UI ----------------------- #
window = Tk()
window.title("French-English flash card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# ----------------------- Front Flash card Canvas ----------------------- #
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='images/card_front.png')
card_bg = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 125, text="", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

card_back = PhotoImage(file='images/card_back.png')

# ----------------------- Cross Button ----------------------- #
cross_img = PhotoImage(file="images/wrong.png")
cross = Button(image=cross_img, highlightthickness=0, bg="white", command=next_card)
cross.grid(row=1, column=0)

# ----------------------- Tick Button ----------------------- #
tick_img = PhotoImage(file="images/right.png")
tick = Button(image=tick_img, highlightthickness=0, bg="white", command=is_known)
tick.grid(row=1, column=1)

next_card()

window.mainloop()
