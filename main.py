from tkinter import *
import pandas
import json
import random

BACKGROUND_COLOR = "#B1DDC6"

# read the data using pandas library
data = pandas.read_csv("data/french_words.csv")
# convert the data into a dic changing the orient parameter to records
learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(learn)
    # changing the title tex
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

# Step 1 - Create the User Interface (UI) with Tkinter
# configure the window UI
window = Tk()
window.title("Flash Cards App")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
# make the front card img
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
# another option to change the bg color
# canvas.config(background=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# create the text in canvas
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# create the cross ❌ image with PhotoImage and add the image to a button
cross_image = PhotoImage(file="images/wrong.png")
unk_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unk_button.grid(row=1, column=0)
# create the cross ✅ image with PhotoImage and add the image to a button
check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
