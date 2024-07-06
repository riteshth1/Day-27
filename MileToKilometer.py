from tkinter import *

# fixing window size
window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(height=100, width=300)
window.config(padx=20, pady=20)

# labels
my_label = Label(text="is equal to", font=('Times New Roman', 12))
my_label.grid(column=1, row=2)

my_label2 = Label(text="Miles", font=('Times New Roman', 12))
my_label2.grid(column=3, row=1)

my_label3 = Label(text="0", font=('Times New Roman', 12))
my_label3.grid(column=2, row=2)

my_label4 = Label(text="km", font=('Times New Roman', 12))
my_label4.grid(column=3, row=2)

# entry
input = Entry(width=10)
input.grid(column=2, row=1)


# button
def calculate():
    user_mile = input.get()
    km = round(float(user_mile) * 1.609)
    my_label3.config(text=km)


button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=3)

window.mainloop()
