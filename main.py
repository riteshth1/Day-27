import tkinter

window = tkinter.Tk()
window.title("My GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label and packer
"""
packer is one of Tk’s geometry-management mechanisms. 
Geometry managers are used to specify the relative positioning of widgets within their container.
"""

my_label = tkinter.Label(text="I'm label", font=("Times New Roman", 24, 'bold') )
# my_label.pack(side = "left", expand= True)  # used to show the content in the GUI
my_label.grid(column = 1,  row = 1)

# Methods to change the content of the label
# my_label["text"] = "New text"
my_label.config(text= "Ritesh")


# Buttons
def button_clicked():
    my_label.config(text= input_s.get())


buttons = tkinter.Button(text="click me", command=button_clicked)
buttons.grid(column= 2,  row = 2)

button1 = tkinter.Button(text="Anime", command=button_clicked)
button1.grid(column=3, row=1)

# Entry
input_s = tkinter.Entry(width=10)
input_s.grid(column= 4,  row= 4)




window.mainloop()
