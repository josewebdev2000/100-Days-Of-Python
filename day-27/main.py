#!/bin/python3

from tkinter import *

def main():
    """Run the program as a whole."""
    
    global my_label, input

    # Make a Tkinter GUI
    window = Tk()
    window.title("My First GUI Program")
    window.minsize(width=500,height=300)
    window.config(padx=20,pady=20)

    # Write a label
    my_label = Label(text = "I am a label")
    my_label.grid(column=0, row=0)
    my_label.config(text = "New Text")
    
    # Button
    button = Button(text="Click Me", command=button_clicked)
    button.grid(column=1, row=1)
    
    # New Button
    new_button = Button(text="New Button")
    new_button.grid(column=2,row=0)
    
    # Entry
    input = Entry(width=10)
    input.grid(column=3,row=2) 

    window.mainloop()

def button_clicked():
    new_text = input.get()
    my_label.config(text = new_text)

if __name__ == "__main__":
    main()
