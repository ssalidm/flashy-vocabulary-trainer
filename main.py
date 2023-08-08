import tkinter as tk
import pandas as pd
import random


# ------------------------------- CONSTANTS--------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#F6F4EB"
BLACK = "#272829"

# ----------------------------- READ CSV DATA ------------------------------ #
words_to_learn = {}
current_card = {}

def load_data():
    """
    Loads the data from the CSV file containing the French words and their English translations.
    If the file 'data/words_to_learn.csv' is found, it loads the previously learned words.
    If the file is not found or empty, it loads the original data from 'data/french_words.csv'.
    The loaded data is stored in the global variable 'words_to_learn'.
    """
    global words_to_learn
    try:
        data = pd.read_csv('data/words_to_learn.csv')
    except (FileNotFoundError, IndexError, pd.errors.EmptyDataError):
        original_data = pd.read_csv('data/french_words.csv')
        words_to_learn = original_data.to_dict(orient="records")
    else:
        words_to_learn = data.to_dict(orient="records")

# ------------------------ PICK RANDOM FRENCH WORD ------------------------- #
def next_card():
    """
    Picks a random French word from the 'words_to_learn' dictionary and displays it on the application.
    If there are no more words to learn, a congratulatory message is shown.
    After displaying a word, the function schedules a call to 'flip_card()' after a delay of 3000 milliseconds (3 seconds).
    """
    global current_card, flip_timer, words_to_learn
    root.after_cancel(flip_timer)
    try:
        current_card = random.choice(words_to_learn)
    except IndexError:
        message = 'You have learned all the words.\nClick the Reset button to start again.'
        canvas.itemconfig(card_title, text='Congratulations!', fill=BLACK, font=('Ariel', 50, 'bold'))
        canvas.itemconfig(card_word, text=message, font=('Ariel', 28, 'normal'),fill=BLACK)        
    else:
        canvas.itemconfig(card_title, text='French', fill=BLACK, font=('Ariel', 40, 'italic'))
        canvas.itemconfig(card_word, text=current_card['French'], fill=BLACK, font=('Ariel', 60, 'bold'))
        canvas.itemconfig(card_background, image=card_front_img)
        flip_timer = root.after(3000, func=flip_card)


# ------------------------------- FLIP CARD --------------------------------- #
def flip_card():
    """
    Flips the displayed card, revealing the English translation of the current French word.
    This function is called automatically after a delay of 3000 milliseconds (3 seconds) by 'next_card()'.
    """
    canvas.itemconfig(card_title, text='English', fill=WHITE)
    canvas.itemconfig(card_word, text=current_card['English'], fill=WHITE)
    canvas.itemconfig(card_background, image=card_back_img)


# ----------------------------- CORRECT BUTTON ------------------------------- #
def correct_answer():
    """
    Handles the user's response when they click the "Correct" button.
    If there are still words to learn, the current word is removed from 'words_to_learn' dictionary,
    and the dictionary is saved back to the CSV file 'data/words_to_learn.csv'.
    The function then proceeds to display the next word by calling 'next_card()'.
    """
    if len(words_to_learn) != 0:
        words_to_learn.remove(current_card)
        data = pd.DataFrame(data=words_to_learn)
        data.to_csv('data/words_to_learn.csv', index=False)
        next_card()      


# ----------------------------- RESET BUTTON ------------------------------- #
def reset():
    """
    Resets the learning progress by clearing the 'words_to_learn' dictionary and the 'words_to_learn.csv' file.
    It reloads the original data from 'data/french_words.csv' and proceeds to display the next word by calling 'next_card()'.
    """
    data = pd.DataFrame(data={})
    data.to_csv('data/words_to_learn.csv', index=False)
    load_data()
    next_card()


def initialize_app():
    """
    Initializes the application by loading data from the CSV file and displaying the first word using 'next_card()'.
    """
    load_data()
    next_card()


if __name__ == '__main__':
    # ------------------------------- UI SETUP --------------------------------- #
    root = tk.Tk()
    root.title('Flashy')
    root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    flip_timer = root.after(3000, func=flip_card)

    card_front_img = tk.PhotoImage(file='images/card_front.png')
    card_back_img= tk.PhotoImage(file='images/card_back.png')

    canvas = tk.Canvas(root, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
    card_background = canvas.create_image(400, 263, image=card_front_img)
    canvas.grid(column=0, row=0, columnspan=3)

    card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
    card_word = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))


    # --- Buttons --- #

    right_img = tk.PhotoImage(file='images/right.png')
    wrong_img = tk.PhotoImage(file='images/wrong.png')

    button_correct = tk.Button(image=right_img, borderwidth=0, highlightthickness=0,command=correct_answer)
    button_correct.grid(column=2, row=1)

    button_wrong = tk.Button(image=wrong_img, borderwidth=0, highlightthickness=0, command=next_card)
    button_wrong.grid(column=0, row=1)

    button_reset = tk.Button(text="Reset", borderwidth=0, highlightthickness=0, command=reset, width=10, height=3, font=("Ariel", 14, 'bold'))
    button_reset.grid(column=1, row=1)

    # App initialization
    initialize_app()

    # Run app
    root.mainloop()