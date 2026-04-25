import React, { useState } from "react";

export default function ATM({ balance, setBalance, setTxns }) {
  const [amt, setAmt] = useState("");

  const withdraw = () => {
    if (balance >= amt) {
      setBalance(balance - Number(amt));
      setTxns(t => [...t, `- ₹${amt}`]);
    }
  };

  const deposit = () => {
    setBalance(balance + Number(amt));
    setTxns(t => [...t, `+ ₹${amt}`]);
  };

  return (
    <div>
      <h1>ATM</h1>
      <input onChange={(e) => setAmt(e.target.value)} placeholder="Amount" />
      <button onClick={withdraw}>Withdraw</button>
      <button onClick={deposit}>Deposit</button>
    </div>
  );
}