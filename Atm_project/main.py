from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from controller.bank_controller import BankController
from auth import create_token, verify_token
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
controller = BankController()

# ✅ CORS (REQUIRED for React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request model
class LoginRequest(BaseModel):
    account_id: int
    name: str
    pin: int


# ---------------- LOGIN ----------------
@app.post("/login")
def login(data: LoginRequest):
    if not controller.login(data.account_id, data.name, data.pin):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_token(data.account_id, data.name)

    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer"
    }

# ---------------- CHECK BALANCE ----------------
@app.get("/balance/{account_id}")
def check_balance(
    account_id: int,
    user=Depends(verify_token)
):
    if user["account_id"] != account_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    balance = controller.check_balance(account_id)

    return {
        "account_id": account_id,
        "balance": balance
    }


# ---------------- DEPOSIT ----------------
@app.post("/deposit/{account_id}")
def deposit(
    account_id: int,
    amount: float,
    user=Depends(verify_token)
):
    if user["account_id"] != account_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return controller.deposit(account_id, amount)


# ---------------- WITHDRAW ----------------
@app.post("/withdraw/{account_id}")
def withdraw(
    account_id: int,
    amount: float,
    user=Depends(verify_token)
):
    if user["account_id"] != account_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return controller.withdraw(account_id, amount)


# ---------------- MINI STATEMENT ----------------
@app.get("/statement/{account_id}")
def mini_statement(
    account_id: int,
    user=Depends(verify_token)
):
    if user["account_id"] != account_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return controller.mini_statement(account_id)


# ---------------- CHANGE PIN ----------------
@app.put("/change-pin/{account_id}")
def change_pin(
    account_id: int,
    new_pin: int,
    user=Depends(verify_token)
):
    if user["account_id"] != account_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return controller.change_pin(account_id, new_pin)


# ---------------- LOGOUT ----------------
@app.post("/logout")
def logout():
    return {
        "message": "Logged out successfully. Please login again."
    }