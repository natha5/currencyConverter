import tkinter as tk
from tkinter import *
import requests
from requests.structures import CaseInsensitiveDict
import json


url = "https://api.freecurrencyapi.com/v1/latest"

headers = CaseInsensitiveDict()
headers["apikey"] = "9QGTXHu0cUEOrWHFFSQBTjkf7tq36kzL4SUNyEYR"

resp = requests.get(url, headers=headers)

print(resp.status_code)

passoutputcurrency = ""
passinputcurrency = ""


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.currencyOptions = [
            "AUD",
            "BGN",
            "BRL",
            "CAD",
            "CHF",
            "CNY",
            "CZK",
            "DKK",
            "EUR",
            "GBP",
            "HKD",
            "HRK",
            "HUF",
            "IDR",
            "ILS",
            "INR",
            "ISK",
            "JPY",
            "KRW",
            "MXN",
            "MYR",
            "NOK",
            "NZD",
            "PHP",
            "PLN",
            "RON",
            "RUB",
            "SGD",
            "SEK",
            "THB",
            "TRY",
            "USD",
            "ZAR"
        ]
        self.inputCurrency = tk.StringVar(self)
        self.outputCurrency = tk.StringVar(self)

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
        self.opm_inputCurrency = OptionMenu(self, self.inputCurrency, self.currencyOptions, *self.currencyOptions)
        self.opm_inputCurrency.grid(row=1, column=0, sticky=E)

        # entry box for inital amount
        self.ent_initAmount = Entry(self)
        self.ent_initAmount.grid(row=1, column=1, sticky=W)

        # equals sign to separate input and output visually
        self.lbl_equals = Label(self, text = "=")
        self.lbl_equals.grid(row=1, column = 2, sticky = W)

        # drop down to select output currency
        self.opm_outputCurrency = OptionMenu(self, self.outputCurrency, self.currencyOptions, *self.currencyOptions)
        self.opm_outputCurrency.grid(row=1, column=3, sticky=E)

        # result text box
        self.txt_outputAmount = Text(self, width = 5, height = 1, wrap= NONE)
        self.txt_outputAmount.grid(row = 1, column = 4, sticky = W)
        self.txt_outputAmount.config(state = 'disabled')

        # submit button
        self.bttn_convert = Button(self, text='Submit', command = self.convert)
        self.bttn_convert.grid(row=2, column=0, sticky=W)

    def convert(self):
        inputAmount = self.ent_initAmount.get()

        # use input currency as base, request output currency
        passinputcurrency = self.inputCurrency.get()
        passoutputcurrency = self.outputCurrency.get()
        requesturl = "https://api.freecurrencyapi.com/v1/latest?apikey=9QGTXHu0cUEOrWHFFSQBTjkf7tq36kzL4SUNyEYR&currencies=" + passoutputcurrency + "&base_currency=" + passinputcurrency

        exchangeresp = requests.get(requesturl, headers=headers)

        self.txt_outputAmount.delete(0.0, END)


        response_data = exchangeresp.json()

        exchange_rate = response_data["data"]
        actual_exchange_rate = exchange_rate.get(passoutputcurrency)

        floatInput = float(inputAmount)
        outputAmount = floatInput * actual_exchange_rate

        print(inputAmount)
        print(exchange_rate)
        print(outputAmount)
        self.txt_outputAmount.config(state = 'normal')
        self.txt_outputAmount.insert('end', outputAmount)
        self.txt_outputAmount.config(state='disabled')




root = Tk()

root.title("Currency Converter")

root.geometry("500x250")

app = Application(root)

root.mainloop()
