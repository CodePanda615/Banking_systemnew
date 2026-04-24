from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from .database import Base

class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True)
    name = Column(String)
    account_id = Column(Integer, unique=True)
    balance = Column(Float)
    pin = Column(Integer)
    account_type = Column(String)


class Transaction(Base):
    __tablename__ = "transaction"

    transaction_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("customer.account_id"))
    amount = Column(Float)
    transaction_type = Column(String)
    description = Column(String)
    balance_before = Column(Float)
    balance_after = Column(Float)
    transaction_date = Column(TIMESTAMP, default=func.now())