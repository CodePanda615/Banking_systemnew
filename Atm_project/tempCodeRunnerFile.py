from controller.bank_controller import BankController
from view.atm_view import ATMView

controller = BankController()
view = ATMView()

print("===== WELCOME TO ATM =====")


name = input("Enter Name: ")
acc_id = int(input("Enter Account ID: "))
pin = int(input("Enter PIN: "))

if not controller.login(acc_id, name, pin):
    print("Invalid Credentials ")
    exit()

print("Login Successful ")


while True:
    choice = view.menu()

    if choice == 1:
        print("Balance:", controller.check_balance(acc_id))

    elif choice == 2:
        amt = float(input("Enter amount: "))
        print(controller.deposit(acc_id, amt))

    elif choice == 3:
        amt = float(input("Enter amount: "))
        print(controller.withdraw(acc_id, amt))

    elif choice == 4:
        transactions = controller.mini_statement(acc_id)

        print("\n----- MINI STATEMENT -----")
        for t in transactions:
            print(f"""
Date: {t['date']}
Type: {t['type']}
Description: {t['desc']}
Amount: {t['amount']}
Balance Before: {t['before']}
Balance After: {t['after']}
-----------------------------
""")

    elif choice == 5:
        new_pin = int(input("Enter New PIN: "))
        print(controller.change_pin(acc_id, new_pin))

    elif choice == 6:
        confirm = input("Are you sure you want to exit? (yes/no): ")
        
        if confirm.lower() == "yes":
            print("Thank you 🙏")
            break
        else:
            print("Continuing...")   

    