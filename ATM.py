accounts = {
    "account1": 1000.00,
    "account2": 2500.00,
    "account3": 500.00
}


def format_text(text, width):
    padding = " " * ((width - len(text)) // 2)
    return f"║{padding}{text}{padding}║"


def print_line():
    print("╔════════════════════════════════════════════════════╗")


def print_divider():
    print("╠════════════════════════════════════════════════════╣")


def print_end_line():
    print("╚════════════════════════════════════════════════════╝")


def display_account_names():
    print_line()
    print("║                Available Accounts                  ║")
    print_divider()
    for account in accounts:
        print(f"║ {account.capitalize().center(50)} ║")
    print_end_line()


def display_menu():
    print_line()
    print(format_text("║                  ATM Menu                   ║", 50))
    print_divider()
    print("║ 1. Check Balance                            ║")
    print("║ 2. Withdraw Money                           ║")
    print("║ 3. Deposit Money                            ║")
    print("║ 4. Exit                                     ║")
    print_end_line()


def check_balance(account):
    balance = accounts.get(account)
    if balance is None:
        print("Account not found!")
    else:
        print_line()
        print(format_text(f"Account Balance: ${balance:.2f}", 50))
        print_end_line()


def withdraw(account, amount):
    balance = accounts.get(account)
    if balance is None:
        print("Account not found!")
        return

    if amount > balance:
        print("Insufficient funds!")
    else:
        accounts[account] -= amount
        print_line()
        print(format_text("Withdrawal Successful", 50))
        print(format_text(f"Remaining Balance: ${accounts[account]:.2f}", 50))
        print_end_line()


def deposit(account, amount):
    balance = accounts.get(account)
    if balance is None:
        print("Account not found!")
        return

    accounts[account] += amount
    print_line()
    print(format_text("Deposit Successful", 50))
    print(format_text(f"Current Balance: ${accounts[account]:.2f}", 50))
    print_end_line()


def main():
    display_account_names()
    account = input("Enter your account name: ").capitalize()
    print_line()
    print(format_text(f"Welcome, {account}!", 52))
    print_end_line()
    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            check_balance(account)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: $"))
            withdraw(account, amount)
        elif choice == '3':
            amount = float(input("Enter the amount to deposit: $"))
            deposit(account, amount)
        elif choice == '4':
            print_line()
            print("Thank you for using the ATM!")
            print_end_line()
            break
        else:
            print("Invalid choice. Please enter a valid number.")


if __name__ == '__main__':
    main()
