from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)
    password_gen = "".join(password_list)
    password_entry.insert(0, password_gen)
    pyperclip.copy(password_gen)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_data = web_entry.get()
    email_data = email_entry.get()
    pass_data = password_entry.get()
    new_data = {web_data: {
        "email": email_data,
        "password": pass_data
    }}
    if len(web_data) == 0 or len(pass_data) == 0:
        messagebox.showerror(title="Error", message="Some fields are empty")
    else:
        try:
            with open("data.json", "r") as file_data:
                data_loaded = json.load(file_data)
        except FileNotFoundError:
            with open("data.json", "w") as file_data:
                json.dump(new_data, file_data, indent=4)
        else:
            data_loaded.update(new_data)
            with open("data.json", "w") as file_data:
                json.dump(data_loaded, file_data, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Search Function ------------------------------- #
def find_password():
    to_search = web_entry.get()

    try:
        with open("data.json", "r") as search_data:
            loaded_data = json.load(search_data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"file not found")
    else:
        if to_search in loaded_data:
            new_data_email = loaded_data[to_search]["email"]
            new_data_password = loaded_data[to_search]["password"]
            messagebox.showinfo(title="Your Password", message=f"Email: {new_data_email},\nPassword: {new_data_password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {to_search} exists")
# ---------------------------- UI SETUP ------------------------------- #

# Set up of Window

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Set Up of Canvas

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# set up of website Entry
web = Label(text="Website:")
web.grid(column=0, row=1)

web_entry = Entry(width=20)
web_entry.focus()
web_entry.grid(column=1, row=1)

# Search Button
search = Button(text="search", command=find_password)
search.grid(column=2, row=1)

# set up of Email Entry
email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.insert(0, "Yanendrajha@Gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

# set up of Password Entry
password = Label(text="Password:")
password.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, )

pass_gen = Button(text="Generate Password", command=generate_password)
pass_gen.grid(column=2, row=3, )

# Data Adding Button
add_pass = Button(text="Add", width=38, command=save)
add_pass.grid(column=1, row=4, columnspan=2)

window.mainloop()
