import tkinter as tk
from tkinter import messagebox
import random


def auto_choose_house():
    houses = ["Blue House", "Green House", "Yellow House", "Red House"]
    chosen_house = random.choice(houses)
    messagebox.showinfo('Congratulations!', f'You have been automatically chosen in {chosen_house}\n\nThank You!!!!')
    root.destroy()


root = tk.Tk()
root.title('HPSR House Selections')

auto_choose_button = tk.Button(root, text='Automatically Choose House',
                               command=auto_choose_house)
auto_choose_button.pack()

root.mainloop()
