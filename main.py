from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = entry_website.get().title()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website:
            {"email": email,
             "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please don't left any fields empty!")
        # is_ok = False
    else:
        try:
            with open("data.json", mode="r") as file:
                #reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #Updating old data
            data.update(new_data)
            #saving updating data
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            entry_password.delete(0, END)
            entry_website.delete(0, END)

# ---------------------------- find password ------------------------------- #
def search():
    website = entry_website.get().title()
    try:
        with open("data.json", mode="r") as file:
            # reading old data
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
            entry_password.insert(0, password)
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title=website, message=f"You don't have any data for this website.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_website = Entry(width=21)
entry_website.grid(column=1, row=1, sticky=W)
entry_website.insert(END, string="")

#change "YOUR_EMAIL"
entry_email = Entry(width=51)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "YOUR_EMAIL")

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3, sticky=W)
entry_password.insert(END, string="")


button_generate_password = Button(text="Generate Password",width=14, command=generate_password)
button_generate_password.grid(column=2, row=3, sticky=W)

button_add = Button(text="Add", width=43, command=add)
button_add.grid(column=1, row=4, columnspan=2)

button_search = Button(text="Search", width=14, command=search)
button_search.grid(column=2, row=1)

window.mainloop()
