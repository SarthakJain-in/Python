from tkinter import *
import random
from tkinter import messagebox
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pass():
    password_list = []
    for letter in range(0, 6) :
        password_list.append(random.choice(letters))

    for num in range(0, 4) :
        password_list.append(random.choice(numbers))

    for sym in range(0, 2) :
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password = ""
    for final in password_list :
        password += final

    #Inserting/Displaying password inside to Entry textbox
    set_password.delete(0, END)
    set_password.insert(0, password)

    # Copy password to clipboard
    window.clipboard_clear()
    window.clipboard_append(set_password.get())
    window.update()


def add():
    website = website_name.get()
    gmail = username.get()
    password = set_password.get()
    new_data = {
        website: {
            "email":gmail,
            "password":password
        }
    }

    if website == "" or gmail == "" or password == "":
        messagebox.showerror(title="Empty field!", message="Some fields are empty!")
    else:
        is_ok = messagebox.askokcancel(title="Confirm save", message=f"{website_name.get()} \nYour detials: \nUsername: {username.get()} \nPassword: {set_password.get()} \nIs this details are ok to save?")
        if is_ok:
            try:
                with open("data_file.json") as data_file:
                    data = json.load(data_file)
            except FileExistsError:
                with open("data_file.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open("data_file.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_name.delete(0, END) 
                username.delete(0, END)
                set_password.delete(0, END)
                website_name.focus()


def search():
    website = website_name.get()
    if website == "":
        messagebox.showerror(title="Empty", message="First enter name of website")
    else:
        try:
            with open("data_file.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="File not found")
        else:
            if website in data:
                messagebox.showinfo(title="Details", message=f"Your details are: \nUsername: {data[website]['email']} \nPassword: {data[website]['password']}")
            else:
                messagebox.showinfo(title="Not found", message=f"No details for {website} exists")


window = Tk()
window.title("Passwword Manager")
window.config(padx=20, pady=20)

canva = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canva.create_image(100, 100, image=logo_img)
canva.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website :")
website_label.grid(row=1, column=0)

website_name = Entry(width=25)
website_name.focus()
website_name.grid(row=1, column=1, pady=6)

username_label = Label(text="Gmail/Username :")
username_label.grid(row=2, column=0)

username = Entry(width=44)
username.grid(row=2, column=1, columnspan=2, pady=6)

password_label = Label(text="Password :")
password_label.grid(row=3, column=0)

set_password = Entry(width=25)
set_password.grid(row=3, column=1, pady=6)

generate_btn = Button(text="Generate Password", command=generate_pass)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="ADD", width=36, command=add)
add_btn.grid(row=4, column=1, columnspan=2, pady=6)

search_btn = Button(text="SEARCH", command=search, width=12)
search_btn.grid(row=1, column=2)

window.mainloop()