from tkinter import *
import random
import pandas

current_card = {}
to_learn = {}
window = Tk()
BACKGROUND_COLOR = "#B1DDC6"
window.title("Cards")
window.minsize(width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
frontcard = PhotoImage(file="card_front.png")
backcard = PhotoImage(file="card_back.png")
nobutton = PhotoImage(file="wrong.png")
rightbutton = PhotoImage(file="right.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 268, image=frontcard)
canvas.grid(column=0, row=0, columnspan=2)

try:
    data = pandas.read_csv("words_to_learn.csv", encoding = "ISO-8859-1")
except FileNotFoundError:
    original_data = pandas.read_csv("spanish.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def decline():
    global current_card
    current_card = random.choice(to_learn)
    canvas.create_image(400, 268, image=frontcard)
    canvas.create_text(400, 150, text="Spanish", font=("Ariel", 40, "italic"))
    canvas.create_text(400, 263, text=current_card["Spanish"], font=("Ariel", 52, "bold"))
    timer()


def approve():
    global current_card
    current_card = random.choice(to_learn)
    canvas.create_image(400, 268, image=frontcard)
    canvas.create_text(400, 150, text="Spanish", font=("Ariel", 40, "italic"))
    canvas.create_text(400, 263, text=current_card["Spanish"], font=("Ariel", 52, "bold"))
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn", index=False)
    timer()


def flip():
    canvas.create_image(400, 263, image=backcard)
    canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
    canvas.create_text(400, 263, text=current_card["English"], font=("Ariel", 52, "bold"))




def timer():
    window.after(3000, flip)


italian_text = canvas.create_text(400, 150, text="Spanish", font=("Ariel", 40, "italic"))
it_word = canvas.create_text(400, 263, text="Start", font=("Ariel", 52, "bold"))
wrong = Button(image=nobutton, highlightthickness=0, command=decline)
wrong.grid(column=0, row=1)
right = Button(image=rightbutton, highlightthickness=0, command=approve)
right.grid(column=1, row=1)

window.mainloop()
