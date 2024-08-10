from tkinter import*
import random

root = Tk()

root.geometry("400x400")
root.title("Color Changing App")

label = Label(root, text = "Color Changing Background", font = ("SimSun", 21, "bold"))
label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

def change_color(event) :
    color = ["firebrick1", "firebrick4", "sandy brown", "DarkOrange3", "khaki1", "DarkGoldenRod3", "pale green", "dark green", "pale turquoise", "navy", "MediumPurple1", "purple3", "pink1", "DeepPink2"]
    
    background_random = random.choice(color)
    root.configure(background = background_random)

root.bind('<space>', change_color)
root.mainloop()