from tkinter import *
from tkinter import messagebox
import random

class Index:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Generator")
        self.window.geometry("400x400")
        self.logo = PhotoImage(file="logo.png")
        #Variables
        self.user_var = StringVar()
        self.pw_var = StringVar()
        self.web_var = StringVar()
        self.home_page()
        self.window.mainloop()

    def home_page(self):
        #Logo
        logo_label = Label(self.window, image=self.logo)
        logo_label.grid(row=0, column=1,pady=30,sticky="SW", padx=(10,0))

        #Website entry
        website_label = Label(self.window, text="Website:", font=('Inter',12, 'bold'))
        website_entry = Entry(self.window, textvariable=self.web_var,font=('Inter',12),width=25)
        website_entry.focus()
        website_label.grid(row=1, column=0, sticky="E")
        website_entry.grid(row=1, column=1,columnspan=2, sticky= "W")

        #username entry
        username_label = Label(self.window, text="Email/Username:",font=('Inter',12, 'bold'))
        username_entry = Entry(self.window,textvariable=self.user_var,font=('Inter',12),width=25)
        username_label.grid(row=3, column=0, sticky="W", padx=(10,0), pady=15)
        username_entry.grid(row=3, column=1,columnspan=2, sticky="W")

        #password entry
        pw_label = Label(self.window, text="Password:", font=('Inter', 12, 'bold'))
        pw_entry = Entry(self.window, textvariable=self.pw_var, font=('Inter', 12), width=17)
        generate_button = Button(text="Generate", command=self.generate)
        pw_label.grid(row=4, column=0, sticky="E")
        pw_entry.grid(row=4,column=1, sticky="W")
        generate_button.grid(row=4,column=2, sticky="E")

        #Add button
        add_button = Button(text="Add",width=30, command=self.add)
        add_button.grid(row=5,column=1, columnspan=2, pady=15, sticky="W")




    def add(self):
        website = self.web_var.get()
        email = self.user_var.get()
        password = self.pw_var.get()
        if not website or not email or not password:
            messagebox.showwarning(
                title="Missing Info",
                message="Please fill in all fields"
            )
            return
        with open('file.txt',"a") as file:
            file.write(f"{website} | {email} | {password}\n")
        self.web_var.set("")
        self.user_var.set("")
        self.pw_var.set("")
        messagebox.showinfo(
            title="Saved",
            message="Your password has been saved!"
        )
    def generate(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        self.pw_var.set("")
        password_characters = []

        # choice of letter
        letter_number = random.randint(6,10)
        random_letters = random.choices(letters, k=letter_number)
        password_characters.append(random_letters)

        # Choice of symbols
        symbol_number = random.randint(2,4)
        random_symbols = random.choices(symbols,k=symbol_number)
        password_characters.append(random_symbols)

        # choice of numbers
        number_number = random.randint(4,8)
        random_number = random.choices(numbers,k=number_number)
        password_characters.append(random_number)

        #password maker
        flattened_list = [item for sublist in password_characters for item in (sublist if isinstance(sublist, list) else [sublist])]
        for n in range(0,3):
            random.shuffle(flattened_list)
        password = "".join(flattened_list)
        self.pw_var.set(password)


home = Index()





















# ---------------------------- PASSWORD GENERATOR ------------------------------- #

"""""



print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))







#Password generation
print(password)

result = ""
for char in password:
    result += char

print(f"Your generated password is {result}")
"""""

# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
