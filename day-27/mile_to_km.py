#!/bin/python3

from tkinter import *

def main():
    """Run the program as a whole."""
    
    global mile_entry, km_label
    
    window = Tk()
    window.title("Mile to KM converter")
    
    mile_entry = Entry()
    mile_entry.grid(row=0,column=1)
    
    mile_label = Label(text="Miles")
    mile_label.grid(row=0,column=2)
    
    equal_label = Label(text="is equal to")
    equal_label.grid(row=1,column=0)
    
    km_label = Label(text=0)
    km_label.grid(row=1,column=1)
    
    km_sym_label = Label(text="Km")
    km_sym_label.grid(row=1,column=2)
    
    calculate_btn = Button(text="Calculate",
                           command=convert_to_km)
    
    calculate_btn.grid(row=2,column=1)
    
    
    window.mainloop()


def convert_to_km():
    """Convert input miles to KM."""
    
    miles = round(int(mile_entry.get()) * 1.6)
    km_label.config(text=miles)
    

if __name__ == "__main__":
    main()