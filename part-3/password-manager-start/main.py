from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(0,nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(0,nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(0,nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)


    password = "".join(password_list)
    password_answer.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_answer.get()
    email = name_answer.get()
    password = password_answer.get()
    new_data = {website:{
        "email": email,
        "password": password,
    }}

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
            try:
                with open("data.json", "r") as data_file:
                    #reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #updating old data with new data
                data.update(new_data)

                with open("data.json", "w"):
                    #saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_answer.delete(0, END)
                password_answer.delete(0, END)

#-------------------------------Find Password -------------------------------#
def find_password():
    website = website_answer.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label=Label(text="Website")
website_label.grid(column=0, row=1)

name_label = Label(text="Email/Username")
name_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

website_answer = Entry(width=40)
website_answer.grid(column=1, row=1)
website_answer.focus()

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

name_answer = Entry(width=56)
name_answer.grid(column=1, row=2, columnspan=2)
name_answer.insert(0, "ilovefood4ever@gmail.com")

password_answer = Entry(width=37)
password_answer.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2,row=3)

add_button = Button(text="Add", width=47, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
