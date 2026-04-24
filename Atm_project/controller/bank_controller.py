from model.database import SessionLocal
from model.models import Customer, Transaction
from datetime import datetime


class BankController:

    def login(self, account_id, name, pin):
        db = SessionLocal()

        user = db.query(Customer).filter_by(
            account_id=account_id
        ).first()

        print("Fetched user:", user)

        if not user:
            return False

        print("DB Name:", user.name)
        print("DB Pin:", user.pin)
        print("Input Name:", name)
        print("Input Pin:", pin)

        return (
            str(user.name).strip().lower() == str(name).strip().lower()
            and str(user.pin).strip() == str(pin).strip()
        )

    def check_balance(self, account_id):
        db = SessionLocal()
        acc = db.query(Customer).filter_by(account_id=account_id).first()

        if not acc:
            return "Account not found"

        return acc.balance

    def deposit(self, account_id, amount):
        db = SessionLocal()
        acc = db.query(Customer).filter_by(account_id=account_id).first()

        if not acc:
            return "Account not found"

        before = acc.balance
        acc.balance += amount
        after = acc.balance

        txn = Transaction(
            account_id=account_id,
            amount=amount,
            transaction_type="credit",
            description="Cash Deposit",
            balance_before=before,
            balance_after=after,
            transaction_date=datetime.now()
        )

        db.add(txn)
        db.commit()

        return f"Deposited Successfully, New Balance: {after}"
                                                                                          
    def withdraw(self, account_id, amount):
        db = SessionLocal()
        acc = db.query(Customer).filter_by(account_id=account_id).first()

        if not acc:
            return "Account not found"

        if acc.balance < amount:
            return "Insufficient Balance ❌"

        before = acc.balance
        acc.balance -= amount
        after = acc.balance

        txn = Transaction(
            account_id=account_id,
            amount=amount,
            transaction_type="debit",
            description="Cash Withdrawal",
            balance_before=before,
            balance_after=after,
            transaction_date=datetime.now()
        )

        db.add(txn)
        db.commit()

        return f"Withdrawal Successful. New Balance: {after}"

    def mini_statement(self, account_id):
        db = SessionLocal()

        txns = (
            db.query(Transaction)
            .filter_by(account_id=account_id)
            .order_by(Transaction.transaction_date.desc())
            .limit(5)
            .all()
        )

        result = []

        for t in txns:
            result.append({
                "date": t.transaction_date,
                "type": t.transaction_type,
                "desc": t.description,
                "amount": t.amount,
                "before": t.balance_before,
                "after": t.balance_after
            })

        return result

    def change_pin(self, account_id, new_pin):
        db = SessionLocal()
        acc = db.query(Customer).filter_by(account_id=account_id).first()

        if not acc:
            return "Account not found"

        acc.pin = new_pin
        db.commit()

        return "PIN Updated Successfully ✅"