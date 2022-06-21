import tkinter as tk
from tkinter import *

import requests
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()


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
        self.input_currency = tk.StringVar(self)
        self.output_currency = tk.StringVar(self)

        self.lbl_initial_currency = Label(self, text="Initial currency:")
        self.lbl_initial_amount = Label(self, text="Input amount:")
        self.lbl_output_currency = Label(self, text="Output currency:")
        self.lbl_exchange_rate = Label(self, text="Exchange rate:")

        self.opm_input_currency = OptionMenu(self, self.input_currency, self.currencyOptions, *self.currencyOptions)
        self.ent_initial_amount = Entry(self)
        self.lbl_equals = Label(self, text="=")
        self.opm_output_currency = OptionMenu(self, self.output_currency, self.currencyOptions, *self.currencyOptions)
        self.txt_output_amount = Text(self, width=5, height=1, wrap=NONE)
        self.txt_exchange_rate = Text(self, width=5, height=1, wrap=NONE)
        self.bttn_convert = Button(self, text='Submit', command=self.convert)

        self.create_widgets()

    def create_widgets(self):

        self.lbl_initial_currency.grid(row=0, column=0, columnspan=1, sticky=W)
        self.lbl_initial_amount.grid(row=0, column=1, columnspan=1, sticky=W)
        self.lbl_output_currency.grid(row=0, column=3, columnspan=1, sticky=W)
        self.lbl_exchange_rate.grid(row=0, column=5, columnspan=1, sticky=W)

        self.opm_input_currency.grid(row=1, column=0, sticky=E)
        self.ent_initial_amount.grid(row=1, column=1, sticky=W)
        self.lbl_equals.grid(row=1, column = 2, sticky = W)
        self.opm_output_currency.grid(row=1, column=3, sticky=E)
        self.txt_output_amount.grid(row = 1, column = 4, sticky = W)
        self.txt_exchange_rate.grid(row = 1, column = 5, sticky = W)
        self.bttn_convert.grid(row=2, column=0, sticky=W)

        self.txt_exchange_rate.config(state ='disabled')
        self.txt_output_amount.config(state='disabled')

    def convert(self):
        input_amount = self.ent_initial_amount.get()

        # use input currency as base, request output currency
        pass_input_currency = self.input_currency.get()
        pass_output_currency = self.output_currency.get()
        requesturl = \
            "https://api.freecurrencyapi.com/v1/latest?apikey=9QGTXHu0cUEOrWHFFSQBTjkf7tq36kzL4SUNyEYR&currencies=" + pass_output_currency + "&base_currency=" + pass_input_currency

        exchange_resp = requests.get(requesturl, headers=headers)

        self.txt_output_amount.delete(0.0, END)

        response_data = exchange_resp.json()

        exchange_rate = response_data["data"]
        actual_exchange_rate = exchange_rate.get(pass_output_currency)

        float_input = float(input_amount)
        output_amount = float_input * actual_exchange_rate

        print(input_amount)
        print(exchange_rate)
        print(output_amount)

        self.txt_exchange_rate.config(state='normal')
        self.txt_exchange_rate.insert('end', actual_exchange_rate)
        self.txt_exchange_rate.config(state='disabled')

        self.txt_output_amount.config(state='normal')
        self.txt_output_amount.insert('end', output_amount)
        self.txt_output_amount.config(state='disabled')






root = Tk()

root.title("Currency Converter")

root.geometry("500x250")

app = Application(root)

root.mainloop()
