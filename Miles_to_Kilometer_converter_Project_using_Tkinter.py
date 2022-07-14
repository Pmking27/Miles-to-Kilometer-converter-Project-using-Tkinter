from tkinter import *

from click import command

def mile_to_km():
    miles = float(mile_input.get())
    km =round(miles *1.689)
    kilometer_result_label.config(text=f"{km}")

window=Tk()
window.title("Miles to Kilometer converter")
window.minsize(width=100,height=50)
window.config(padx=20,pady=20)

mile_input = Entry(width=7)
mile_input.grid(column=1,row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1,row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2,row=1)

calculate_buttom = Button(text="Calculate",command=mile_to_km)
calculate_buttom.grid(column=1,row=2)

window.mainloop()
