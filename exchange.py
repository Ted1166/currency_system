import requests
import pandas as pd
import tkinter as tk
from tkinter import ttk



def currency_exchange(amount, from_currency, to_currency):
    API_KEY = "YOUR_API_KEY_HERE"
    API_URL = "https://api.exchangerate-api.com/v4/latest/{}".format(from_currency)
    response = requests.get(API_URL, headers={"Accept-Version": "4"})
    exchange_rates = response.json()["rates"]
    exchange_rates[from_currency] = 1
    exchange_rates_df = pd.DataFrame.from_dict(exchange_rates, orient='index', columns=["rate"])
    exchange_rates_df.reset_index(inplace=True)
    exchange_rates_df.rename(columns={"index": "currency"}, inplace=True)
    exchange_rate = exchange_rates_df[exchange_rates_df["currency"] == to_currency]["rate"].values[0]
    converted_amount = amount * exchange_rate
    return converted_amount

def exchange_button_click():
    amount = float(amount_entry.get())
    from_currency = from_currency_entry.get()
    to_currency = to_currency_entry.get()
    converted_amount = currency_exchange(amount, from_currency, to_currency)
    result_label.config(text="{:.2f}".format(converted_amount))

root = tk.Tk()
root.title("Currency Converter")

amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row=1, column=0)

amount_entry = ttk.Entry(root)
amount_entry.grid(row=1, column=1)

from_currency_label = ttk.Label(root, text="From Currency:")
from_currency_label.grid(row=2, column=0)

from_currency_entry = ttk.Entry(root)
from_currency_entry.grid(row=2, column=1)

to_currency_label = ttk.Label(root, text="To Currency:")
to_currency_label.grid(row=3, column=0)

to_currency_entry = ttk.Entry(root)
to_currency_entry.grid(row=3, column=1)

convert_button = ttk.Button(root, text="Convert", command=exchange_button_click)
convert_button.grid(row=4, column=0)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=1)

root.mainloop()