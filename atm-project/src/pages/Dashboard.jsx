import React from "react";

export default function Dashboard({ balance }) {
  return (
    <div>
      <h1>Dashboard</h1>
      <div className="card">💰 Balance: ₹{balance}</div>
    </div>
  );
}