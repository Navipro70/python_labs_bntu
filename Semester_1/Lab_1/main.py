from tkinter import *  # Import all func and objects from GUI lib (tkinter)
from tkinter import messagebox  # import messagebox (object, class, file :?) I don't know
import time  # import time lib

root = Tk()  # Create root object by calling default function from tkinter


# Make a callback for button command (onPress) func
def button_callback():
    phrase = phraseInput.get()  # Get value of text input
    if phrase:  # Comparison for if block (string phrase automatically cast to bool type)
        print(phrase)  # print phrase to console
        Label(frame, text=phrase, font=60, pady=20, bg='#ff8d85', foreground='#004394').pack()  # print phrase in GUI
        button["state"] = "disabled"  # Set button state to disabled
        time.sleep(1)  # Artificial delay
        messagebox.showinfo("And this it!", "GAME OVER")  # Additional task (show alert with animation and Game over


# Setup root object
root['bg'] = '#fafafa'  # Add background color of GUI root (overwriting 'bg' value from a root object)
root.title("Python Lab BNTU")  # Add title of GUI (by calling function)
root.wm_attributes('-alpha', 1)  # Reset opacity of GUI lib (by calling function)
root.geometry('300x250')  # Add default size of GUI window (by calling function)
root.resizable(width=True, height=True)  # Allow resizeable GUI window

# Bind function (without calling) with lambda func (instead of def func (in this case lambda is callback func)) for
# focus on each component https://stackoverflow.com/questions/24072567/remove-focus-from-entry-widget?rq=1
root.bind_all("<1>", lambda event: event.widget.focus_set())

# Styling GUI window
frame = Frame(root, bg='#ff8d85')  # Make new frame in root GUI with
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)  # Center new frame and set relative width and height

# Setup label with options with Label function, pack is required method for render component
title = Label(frame, text="Enter your phrase", font=60, pady=20, bg='#ff8d85', foreground='#004394').pack()

# Setup Input for phrase with Entry function, pack is required method for render component
phraseInput = Entry(frame, bg='#fff', highlightthickness=0)
phraseInput.pack()

# Setup button for showing text form phraseInput, pack is required method for render component
button = Button(frame, text="Show phrase", bg="yellow", command=button_callback)
button.pack()

# Running a canned cycle
root.mainloop()
