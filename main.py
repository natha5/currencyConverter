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

        self.create_widgets()

    def create_widgets(self):

        # label for input currency drop down
        self.lbl_initCurrency = Label(self, text="Initial currency")
        self.lbl_initCurrency.grid(row=0, column=0, columnspan=1, sticky=W)

        # label for input amount entry
        self.lbl_initAmount = Label(self, text="Input amount")
        self.lbl_initAmount.grid(row=0, column=1, columnspan=1, sticky=W)

        # label for output currency drop down
        self.lbl_outputCurrency = Label(self, text="Output currency")
        self.lbl_outputCurrency.grid(row=0, column=3, columnspan=1, sticky=W)

        # drop down to select input currency
        self.opm_inputCurrency = OptionMenu(self, self.option_var, self.currencyOptions, *self.currencyOptions)
        self.opm_inputCurrency.grid(row=1, column=0, sticky=E)

        # entry box for inital amount
        self.ent_initAmount = Entry(self)
        self.ent_initAmount.grid(row=1, column=1, sticky=W)

        # equals sign to separate input and output visually
        self.lbl_equals = Label(self, text = "=")
        self.lbl_equals.grid(row=1, column = 2, sticky = W)

        # drop down to select output currency
        self.opm_outputCurrency = OptionMenu(self, self.option_var, self.currencyOptions, *self.currencyOptions)
        self.opm_outputCurrency.grid(row=1, column=3, sticky=E)

        # result label
        self.txt_outputAmount = Text(self, width = 5, height = 1, wrap= NONE)
        self.txt_outputAmount.grid(row = 1, column = 4, sticky = W)

        # submit button
        self.bttn_convert = Button(self, text='Submit', command = self.convert)
        self.bttn_convert.grid(row=2, column=0, sticky=W)

    def convert(self):
        #inputCurrency = self.opm_initAmount.get()
        #outputCurrency = self.opm_outputAmount.get()

        inputAmount = self.ent_initAmount.get()
        self.txt_outputAmount.delete(0.0, END)
        self.txt_outputAmount.insert(0.0, inputAmount)

        print(inputAmount)




root = Tk()

root.title("Currency Converter")

root.geometry("500x250")

app = Application(root)

root.mainloop()
