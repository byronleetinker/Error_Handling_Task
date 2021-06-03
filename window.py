from tkinter import *
from tkinter import messagebox

# Window - size, title and colours
window = Tk()
window.geometry("600x300")
window.title("Exception Handling")
window["bg"] = "violet"


# Information on the window, labels, entries and buttons. Defining functions
class Money:
    def __init__(self, window):
        self.label = Label(window, text="Please enter your amount.", bg="violet")
        self.label.place(x=200, y=50)
        self.label_entry = Entry(window)
        self.label_entry.place(x=200, y=100)
        self.verify = Button(window, text="Verify", bg="pink", command=self.verify, borderwidth=5)
        self.verify.place(x=250, y=150)
        self.exit = Button(window, text="Exit", command=self.exit, bg="lightblue", borderwidth=5)
        self.exit.place(x=255, y=200)

# Defining the verify button function
    def verify(self):
        try:
            money = float(self.label_entry.get())
            if money < 3000:
                messagebox.showerror("Insufficient funds", "Please deposit more funds for this excursion.")
                self.label_entry.delete(0, END)
            else:
                messagebox.showinfo("Accepted", "Congratulations. You qualify to go to Malaysia")
                self.label_entry.delete(0, END)
        except ValueError:
            messagebox.showerror("Invalid input", "Please put in an amount in numbers.")
            self.label_entry.delete(0, END)

# Defining the exit button function
    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()


# Object Money(class), Window(where information is displayed)
obj = Money(window)
# Closing the window
window.mainloop()
