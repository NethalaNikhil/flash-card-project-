from tkinter import *
import random
import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
random_num = 0
try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    dict_value = original_data.to_dict(orient="records")
else:
    dict_value = df.to_dict(orient="records")


def random_french_value():
    global random_num, flip_card
    window.after_cancel(flip_card)
    white_screen.config(file="images/card_front.png")
    random_num = random.choice(dict_value)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_num["French"], fill="black")
    flip_card = window.after(3000, english_value)


def english_value():
    global random_num
    white_screen.config(file="images/card_back.png")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_num["English"], fill="white")


def remove_from_csv():
    global random_num
    dict_value.remove(random_num)
    data = pandas.DataFrame(dict_value)
    data.to_csv("words_to_learn.csv")
    random_french_value()


window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR)
window.config(padx=50, pady=50)
flip_card = window.after(3000, english_value)
canvas = Canvas(width=800, height=526)
white_screen = PhotoImage(file="images/card_front.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

canvas.create_image(400, 263, image=white_screen)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="value", font=("Ariel", 60, "bold"))

canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
button1 = Button(image=wrong_img, highlightthickness=0, background=BACKGROUND_COLOR, command=random_french_value)
button2 = Button(image=right_img, highlightthickness=0, background=BACKGROUND_COLOR, command=remove_from_csv)
canvas.grid(row=0, column=0, columnspan=2)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
random_french_value()
window.mainloop()
