from os import path, system
from tkinter import *
import requests
import json

root = Tk()
cpath = path.dirname(__file__)
width = 400
height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.title("gui-bank")
root.resizable(0, 0)

"""
wallet = {}
wallet["balance"] = {}
wallet["balance"]["eur"] = 10000.0
wallet["balance"]["usd"] = 500.0
wallet["balance"]["gbp"] = 300.0
wallet["balance"]["btc"] = 0.0
wallet["balance"]["ltc"] = 0.0
wallet["balance"]["eth"] = 0.0
wallet["balance"]["xmr"] = 0.0
wallet["balance"]["xrp"] = 0.0
"""

global options
options = ["eur", "usd", "gbp", "btc", "ltc", "eth", "xmr", "xrp"]


def save():
    with open(path.join(cpath, 'data.json'), 'w') as outfile:
        json.dump(wallet, outfile)


def load():
    with open(path.join(cpath, 'data.json')) as json_file:
        wallet = json.load(json_file)
    return wallet


global keys
with open(path.join(cpath, 'keys.json')) as json_file:
    keys = json.load(json_file)

global user
f = open(path.join(cpath, "logged-in.txt"), "r")
user = f.read()
f.close()

global wallet
wallet = load()


def balance():
    bwin = Toplevel(root)
    bwin.title("View wallet")
    bwin.geometry("400x240")
    bwin.resizable(0, 0)
    blabel1 = Label(bwin, text="View current balance in:", font=('arial', 12))
    blabel1.pack()
    bvar = StringVar(bwin)
    bvar.set(options[0])
    bdropdown = OptionMenu(bwin, bvar, *options)
    bdropdown.pack()

    blbl = Label(bwin)
    blbl.pack()

    def show():
        bv = bvar.get()
        bbal = wallet[user]["balance"][bv]
        blbl.config(text=f"{bv} balance: {bbal}")

    bshow = Button(bwin, text="Show balance", command=show)
    bshow.pack()

    save()


def convert():
    cwin = Toplevel(root)
    cwin.title("Currency converter")
    cwin.geometry("400x240")
    cwin.resizable(0, 0)
    clabel1 = Label(cwin, text="Convert currency\n(from - to)",
                    font=('arial', 12))
    clabel1.pack()
    clabel2 = Label(cwin)
    clabel2.pack()
    cvar1 = StringVar(cwin)
    cvar2 = StringVar(cwin)
    cvar1.set(options[0])
    cvar2.set(options[1])
    cdrop1 = OptionMenu(cwin, cvar1, *options)
    cdrop1.pack()
    cdrop2 = OptionMenu(cwin, cvar2, *options)
    cdrop2.pack()
    cvar3 = StringVar(cwin)
    clabel3 = Label(cwin, text="amount to convert:")
    clabel3.pack()
    centry1 = Entry(cwin, textvariable=cvar3)
    centry1.pack()

    def convert_btn():
        cbal1 = wallet[user]["balance"][cvar1.get()]
        cbal2 = wallet[user]["balance"][cvar2.get()]
        camount = cvar3.get()
        try:
            camount = float(camount)
            clabel2.config(text="Valid value", fg="green")
        except:
            clabel2.config(text="Invalid float value", fg="red")
        #print(camount, cbal1)
        if camount > cbal1:
            clabel2.config(text="Not enough balance", fg="red")
        else:
            tax = camount * 5 / 100
            wallet[user]["balance"][cvar1.get()] -= camount
            if cvar1.get() in ["eur", "usd", "gbp"] and cvar2.get() in ["eur", "usd", "gbp"]:
                er_key = keys["er"]
                cr = requests.get(
                    f"https://v6.exchangerate-api.com/v6/{er_key}/latest/{cvar1.get()}")
                cdic = cr.json()
                conversion = cdic["conversion_rates"][cvar2.get().upper()]
            else:
                if cvar1.get() not in ["eur", "usd", "gbp"]:
                    ccoin = cvar1.get()
                    creal = cvar2.get()
                if cvar2.get() not in ["eur", "usd", "gbp"]:
                    ccoin = cvar2.get()
                    creal = cvar1.get()
                creal = creal.upper()
                ccoin = ccoin.upper()
                cl_key = keys["cl"]
                cr = requests.get(
                    f"http://api.coinlayer.com/api/live?access_key={cl_key}&target={creal}&symbols={ccoin}")
                cdic = cr.json()
                conversion = cdic["rates"][ccoin]
            wallet[user]["balance"][cvar2.get()] += camount / \
                conversion - tax / conversion
            cbal1 = wallet[user]["balance"][cvar1.get()]
            cbal2 = wallet[user]["balance"][cvar2.get()]
            clabel2.config(
                text=f"new bals: {cvar1.get()} {cbal1} \n {cvar2.get()} {cbal2} \n tax: {cvar1.get()} {tax}")
            save()

    cbutton1 = Button(cwin, text="Convert", command=convert_btn)
    cbutton1.pack()


Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=300)
Form.pack(side=TOP, pady=20)

lbl_title = Label(Top, text="gui-bank v0.1", font=('arial', 11))
lbl_title.pack(fill=X)

btn_wallet = Button(Form, text="View wallet", width=45, command=balance)
btn_wallet.grid(pady=15, row=3, columnspan=2)
btn_wallet.bind('<Return>', balance)

btn_convert = Button(Form, text="Convert & Trade",
                     width=45, command=convert)
btn_convert.grid(pady=15, row=4, columnspan=2)
btn_convert.bind('<Return>', convert)

root.mainloop()
