from os import system, path
from sys import version_info
# If libraries (dependencies) are not present
# on system, tries to install them
try:
    import sqlite3
    if version_info.major > 2:
        from tkinter import *
    else:
        from Tkinter import *
except:
    try:
        system("pip3 install sqlite3 tkinter")
    except:
        system("pip install sqlite3 tkinter")
    import sqlite3
    if version_info.major > 2:
        from tkinter import *
    else:
        from Tkinter import *


# Defining Tkinter variables
root = Tk()
root.title("Login & Register System")
width = 400
height = 340
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
cpath = path.dirname(__file__)  # Current path
python_path = "C:/Python38/python.exe"
python_file = "d:/GitHub/Python-Projects/airhockey/index.py"


# Checks for valid credentials in db
def CheckLogin(username=None, password=None):
    global conn, cursor
    # Joins current path & db name to make sure it is saved in the same directory
    conn = sqlite3.connect(path.join(cpath, "airhockey.db"))
    cursor = conn.cursor()
    # Table already created, but just to be sure
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `members` (member_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
    # Check is username:password combination are valid
    cursor.execute(
        f"SELECT * FROM `members` WHERE `username` = '{username}' AND `password` = '{password}'")
    # If not, return False
    # else, return True
    if cursor.fetchone() is None:
        return False
    else:
        return True


# Login function
def Login(event=None):
    # Getting username & password for easier usage
    user = USERNAME.get()
    password = PASSWORD.get()

    if user == "" or password == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        if CheckLogin(user, password) is True:
            print("Succesfully logged in! Starting Game!")
            root.withdraw()
            # This will throw an error when exiting the game
            # since the tkinter window was already closed
            root.destroy()
            # Simply starts airhockey
            system(
                f"{python_path} {python_file}")
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            print("Bad credentials")
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    # Save changes and close connection to db
    conn.commit()
    cursor.close()
    conn.close()


# Register function
def Register(event=None):
    # Getting username & password for easier usage
    user = USERNAME.get()
    password = PASSWORD.get()

    if user == "" or password == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        if CheckLogin(user, password) is True:
            print("Already registered!")
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="Already registered!", fg="red")
        else:
            cursor.execute(
                f"INSERT INTO `members` (username, password) VALUES('{user}', '{password}')")
        lbl_text.config(text="Succesfully registered!", fg="green")
        USERNAME.set("")
        PASSWORD.set("")
    # Save changes and close connection to db
    conn.commit()
    cursor.close()
    conn.close()


# Defining variables
USERNAME = StringVar()
PASSWORD = StringVar()


# Top and Form frames
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)


# Labels (headers)
lbl_title = Label(Top, text="AirHockey Login", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text="Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)


# Input
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)


# Buttons
btn_login = Button(Form, text="Login & Start Game!", width=45, command=Login)
btn_login.grid(pady=15, row=3, columnspan=2)
btn_login.bind('<Return>', Login)

btn_register = Button(Form, text="Register", width=45, command=Register)
btn_register.grid(pady=0, row=4, columnspan=2)
btn_register.bind('<Return>', Login)


root.mainloop()
