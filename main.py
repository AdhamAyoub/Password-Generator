from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    pass_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [
        *[random.choice(letters) for _ in range(random.randint(8, 10))],
        *[random.choice(symbols) for _ in range(random.randint(2, 4))],
        *[random.choice(numbers) for _ in range(random.randint(2, 4))]
    ]

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    pass_input.insert(END, password)
    # messagebox.showinfo(title="Success", message="password copied")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = mail_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="empty fields detected")
    else:
        try:
            with open("DATA.json", "r") as data_file:
                data = json.load(data_file)  # json.load reads what is inside
        except FileNotFoundError:  # if no file
            with open("DATA.json", "w") as data_file:  # make a file
                json.dump(new_data, data_file, indent=4)  # add the new data
        else: # if there is a file
            data.update(new_data)  # update what existing with new data
            with open("DATA.json", "w") as data_file:  # change mood
                json.dump(data, data_file, indent=4)  # write the new data
        finally:  # whatever happens do this
            web_input.delete(0, END)
            # mail_input.delete(0, END)
            pass_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_input.get().title()
    if len(website) > 0:
        try:
            with open("DATA.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo("Error", "data file is empty")
        else:
            if website in data:
                mail = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(f"{website}", f"E-mail: {mail}\n"
                                            f"password: {password} ")
            else:
                messagebox.showinfo("not exciting", f"the website ({website}) is not included")










# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1, sticky=EW)

# Labels
website_label = Label(text="Website:", font=("Arial", 10, "normal"), bg="white")
website_label.grid(row=1, column=0, sticky=EW)

website_user = Label(text="E-mail:", font=("Arial", 10, "normal"), bg="white")
website_user.grid(row=2, column=0, sticky=EW)

password_label = Label(text="Password:", font=("Arial", 10, "normal"), bg="white")
password_label.grid(row=3, column=0, sticky=EW)

# Entries
web_input = Entry(width=32)
web_input.grid(row=1, column=1, columnspan=2, sticky=W)
web_input.focus()

mail_input = Entry(width=32)
mail_input.insert(END, "user@gmail.com")
mail_input.grid(row=2, column=1, columnspan=2, sticky=W)

pass_input = Entry(width=32)
pass_input.grid(row=3, column=1, sticky=W)

# Button
generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=2, sticky=EW)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

search_button = Button(text="Search",command=find_password)
search_button.grid(row=1, column=2, sticky=EW)


window.mainloop()
