import tkinter as tk
from tkinter import messagebox

class LoginForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        
        self.label_username = tk.Label(master, text="Username:")
        self.label_username.pack()

        self.entry_username = tk.Entry(master)
        self.entry_username.pack()

        self.label_password = tk.Label(master, text="Password:")
        self.label_password.pack()

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(master, text="Login", command=self.login)
        self.button_login.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.validate_credentials(username, password):
            messagebox.showinfo("Login Successful", "Welcome!")
            # Proceed with the application logic
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

    def validate_credentials(self, username, password):
        # Placeholder for actual credential validation logic
        return username == "admin" and password == "password"