import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from data import name, uid, balance
import random

class BankingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Banking System")
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use a modern theme
        self.style.configure('TLabel', font=('Helvetica', 14))
        self.style.configure('TButton', font=('Helvetica', 12))
        self.main_menu()

    def main_menu(self):
        self.clear_frame()
        ttk.Label(self.root, text="VIRTUAL BANKING SYSTEM", font=("Helvetica", 16)).pack(pady=20)
        ttk.Button(self.root, text="Create Account", command=self.create_account).pack(pady=10)
        ttk.Button(self.root, text="Log in", command=self.log_in).pack(pady=10)

    def create_account(self):
        self.clear_frame()
        ttk.Label(self.root, text="Enter your name:").pack(pady=10)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.pack(pady=10)
        ttk.Button(self.root, text="Submit", command=self.save_account).pack(pady=10)

    def save_account(self):
        user_name = self.name_entry.get()
        if user_name:
            name.append(user_name)
            user_id = random.randint(1000, 9999)
            uid.append(user_id)
            balance.append(0)
            messagebox.showinfo("Account Created", f"Your account has been successfully created.\nName: {user_name}\nUID: {user_id}")
            self.main_menu()
        else:
            messagebox.showerror("Error", "Name cannot be empty")

    def log_in(self):
        self.clear_frame()
        ttk.Label(self.root, text="Enter your UID:").pack(pady=10)
        self.uid_entry = ttk.Entry(self.root)
        self.uid_entry.pack(pady=10)
        ttk.Button(self.root, text="Submit", command=self.verify_uid).pack(pady=10)

    def verify_uid(self):
        user_id = self.uid_entry.get()
        if user_id.isdigit() and int(user_id) in uid:
            self.current_user_index = uid.index(int(user_id))
            messagebox.showinfo("Welcome", f"Welcome back, {name[self.current_user_index]}")
            self.bank_menu()
        else:
            messagebox.showerror("Error", "Invalid UID")
            self.main_menu()

    def bank_menu(self):
        self.clear_frame()
        ttk.Label(self.root, text=f"Hello {name[self.current_user_index]}, How can we help you today?", font=("Helvetica", 14)).pack(pady=20)
        ttk.Button(self.root, text="Credit", command=self.credit).pack(pady=10)
        ttk.Button(self.root, text="Debit", command=self.debit).pack(pady=10)
        ttk.Button(self.root, text="Check Balance", command=self.check_balance).pack(pady=10)
        ttk.Button(self.root, text="Log out", command=self.main_menu).pack(pady=10)

    def credit(self):
        self.clear_frame()
        ttk.Label(self.root, text="Enter the amount you want to credit:").pack(pady=10)
        self.amount_entry = ttk.Entry(self.root)
        self.amount_entry.pack(pady=10)
        ttk.Button(self.root, text="Submit", command=self.process_credit).pack(pady=10)

    def process_credit(self):
        amount = self.amount_entry.get()
        if amount.isdigit():
            balance[self.current_user_index] += int(amount)
            messagebox.showinfo("Success", "Credited successfully!")
            self.bank_menu()
        else:
            messagebox.showerror("Error", "Invalid amount")

    def debit(self):
        self.clear_frame()
        ttk.Label(self.root, text="Enter the amount you want to debit:").pack(pady=10)
        self.amount_entry = ttk.Entry(self.root)
        self.amount_entry.pack(pady=10)
        ttk.Button(self.root, text="Submit", command=self.process_debit).pack(pady=10)

    def process_debit(self):
        amount = self.amount_entry.get()
        if amount.isdigit() and int(amount) <= balance[self.current_user_index]:
            balance[self.current_user_index] -= int(amount)
            messagebox.showinfo("Success", "Debited successfully!")
            self.bank_menu()
        else:
            messagebox.showerror("Error", "Invalid amount or insufficient balance")

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: {balance[self.current_user_index]}")
        self.bank_menu()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingSystem(root)
    root.mainloop()