class ATMView:

    def menu(self):
        print("""
----- ATM MENU -----
1. Check Balance
2. Deposit
3. Withdraw
4. Mini Statement
5. Change PIN
6. Continue / Exit

""")
        return int(input("Enter choice: "))