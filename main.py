import tkinter as tk
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.currencyOptions = [
            "£",
            "$",
            "€"
        ]
        self.option_var = tk.StringVar(self)

        self.createWidgets()

    def createWidgets(self):
        # label for initial amount box
        self.lbl_initCurrency = Label(self, text="Initial currency")
        self.lbl_initCurrency.grid(row=0, column=0, columnspan=2, sticky=W)

        # drop down to select currency
        self.opm_inputCurrency = OptionMenu(self, self.option_var, self.currencyOptions, *self.currencyOptions)
        self.opm_inputCurrency.grid(row=1, column=0, sticky=W)

        # entry box for inital amount
        self.ent_initAmount = Entry(self)
        self.ent_initAmount.grid(row=1, column=1, sticky=W)

        self.bttn_convert = Button(self, text='Submit')
        self.bttn_convert.grid(row=1, column=2, sticky=W)

        self.lbl_equals = Label(self, text = "=")
        self.lbl_equals.grid(row=1, column = 3, columnspan= 3, sticky = W)

        # drop down to select currency
        self.opm_outputCurrency = OptionMenu(self, self.option_var, self.currencyOptions, *self.currencyOptions)
        self.opm_outputCurrency.grid(row=1, column=4, sticky=W)


root = Tk()

root.title("Currency Converter")

root.geometry("300x150")

app = Application(root)

root.mainloop()
