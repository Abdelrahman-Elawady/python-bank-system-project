from bank_accounts import *
# import pandas as pd
# import tkinter as tk
# from tkinter import messagebox

Ahmed = BankAccount(1000, "Ahmed")
Ibrahim = BankAccount(50000, "Ibrahim")
Fatimah = BankAccount(2300, "Fatimah")

# Ahmed.getBalance()
# Ibrahim.getBalance()
# Fatimah.getBalance()

# Ahmed.deposit(400)
# Fatimah.withdraw(60000)
# Fatimah.withdraw(60)

# Ibrahim.transfer(1000000, Ahmed)
# Ibrahim.transfer(4, Ahmed)

Hossam = InterestRewardsAcc(2000, "Hossam")

# Hossam.getBalance()
# Hossam.deposit(100)
# Hossam.transfer(100, Fatimah)

salah = SavingsAcc(4000, "mohamed")

# salah.getBalance()
# salah.deposit(80)
# salah.transfer(300, Ahmed)

def main():
    accounts = {}
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Check Balance\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            accName = input("Enter account name: ")
            initialAmount = float(input("Enter initial amount: "))
            accType = input("Enter account type (regular/savings): ").lower()
            if accType == 'savings':
                accounts[accName] = SavingsAcc(initialAmount, accName)
            else:
                accounts[accName] = BankAccount(initialAmount, accName)

        elif choice == '2':
            accName = input("Enter account name: ")
            if accName in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[accName].deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            accName = input("Enter account name: ")
            if accName in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[accName].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            fromAcc = input("Enter your account name: ")
            toAcc = input("Enter recipient account name: ")
            if fromAcc in accounts and toAcc in accounts:
                amount = float(input("Enter amount to transfer: "))
                accounts[fromAcc].transfer(amount, accounts[toAcc])
            else:
                print("One or both accounts not found.")

        elif choice == '5':
            accName = input("Enter account name: ")
            if accName in accounts:
                accounts[accName].getBalance()
            else:
                print("Account not found.")

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# def save_accounts_to_excel(accounts, filename="accounts.xlsx"):
#     data = []
#     for accName, account in accounts.items():
#         data.append([accName, account.balance, type(account).__name__])
#     df = pd.DataFrame(data, columns=["Account Name", "Balance", "Account Type"])
#     df.to_excel(filename, index=False)

# def load_accounts_from_excel(filename="accounts.xlsx"):
#     accounts = {}
#     try:
#         df = pd.read_excel(filename)
#         for _, row in df.iterrows():
#             accName = row["Account Name"]
#             balance = row["Balance"]
#             accType = row["Account Type"]
#             if accType == "SavingsAcc":
#                 accounts[accName] = SavingsAcc(balance, accName)
#             elif accType == "InterestRewardsAcc":
#                 accounts[accName] = InterestRewardsAcc(balance, accName)
#             else:
#                 accounts[accName] = BankAccount(balance, accName)
#     except FileNotFoundError:
#         pass
#     return accounts

# def create_account():
#     accName = acc_name_entry.get()
#     initialAmount = float(initial_amount_entry.get())
#     accType = acc_type_var.get()
#     if accType == 'Savings':
#         accounts[accName] = SavingsAcc(initialAmount, accName)
#     else:
#         accounts[accName] = BankAccount(initialAmount, accName)
#     save_accounts_to_excel(accounts)
#     messagebox.showinfo("Success", f"Account '{accName}' created successfully!")

# def deposit():
#     accName = acc_name_entry.get()
#     if accName in accounts:
#         amount = float(amount_entry.get())
#         result = accounts[accName].deposit(amount)
#         save_accounts_to_excel(accounts)
#         messagebox.showinfo("Deposit", result)
#     else:
#         messagebox.showerror("Error", "Account not found.")

# def withdraw():
#     accName = acc_name_entry.get()
#     if accName in accounts:
#         amount = float(amount_entry.get())
#         result = accounts[accName].withdraw(amount)
#         save_accounts_to_excel(accounts)
#         messagebox.showinfo("Withdraw", result)
#     else:
#         messagebox.showerror("Error", "Account not found.")

# def transfer():
#     fromAcc = from_acc_entry.get()
#     toAcc = to_acc_entry.get()
#     if fromAcc in accounts and toAcc in accounts:
#         amount = float(amount_entry.get())
#         result = accounts[fromAcc].transfer(amount, accounts[toAcc])
#         save_accounts_to_excel(accounts)
#         messagebox.showinfo("Transfer", result)
#     else:
#         messagebox.showerror("Error", "One or both accounts not found.")

# def check_balance():
#     accName = acc_name_entry.get()
#     if accName in accounts:
#         result = accounts[accName].getBalance()
#         messagebox.showinfo("Balance", result)
#     else:
#         messagebox.showerror("Error", "Account not found.")

# accounts = load_accounts_from_excel()

# root = tk.Tk()
# root.title("Banking System")

# tk.Label(root, text="Account Name:").grid(row=0, column=0)
# acc_name_entry = tk.Entry(root)
# acc_name_entry.grid(row=0, column=1)

# tk.Label(root, text="Initial Amount:").grid(row=1, column=0)
# initial_amount_entry = tk.Entry(root)
# initial_amount_entry.grid(row=1, column=1)

# acc_type_var = tk.StringVar(value="Regular")
# tk.Label(root, text="Account Type:").grid(row=2, column=0)
# tk.Radiobutton(root, text="Regular", variable=acc_type_var, value="Regular").grid(row=2, column=1)
# tk.Radiobutton(root, text="Savings", variable=acc_type_var, value="Savings").grid(row=2, column=2)

# tk.Label(root, text="Amount:").grid(row=3, column=0)
# amount_entry = tk.Entry(root)
# amount_entry.grid(row=3, column=1)

# tk.Label(root, text="From Account:").grid(row=4, column=0)
# from_acc_entry = tk.Entry(root)
# from_acc_entry.grid(row=4, column=1)

# tk.Label(root, text="To Account:").grid(row=5, column=0)
# to_acc_entry = tk.Entry(root)
# to_acc_entry.grid(row=5, column=1)

# tk.Button(root, text="Create Account", command=create_account).grid(row=6, column=0)
# tk.Button(root, text="Deposit", command=deposit).grid(row=6, column=1)
# tk.Button(root, text="Withdraw", command=withdraw).grid(row=6, column=2)
# tk.Button(root, text="Transfer", command=transfer).grid(row=6, column=3)
# tk.Button(root, text="Check Balance", command=check_balance).grid(row=6, column=4)

# root.mainloop()