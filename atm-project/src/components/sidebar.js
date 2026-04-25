import React from "react";
import { useNavigate } from "react-router-dom";

export default function Sidebar({ setAuth }) {
  const navigate = useNavigate();

  return (
    <div className="sidebar">
      <h2>MyBank</h2>

      <button onClick={() => navigate("/dashboard")}>Dashboard</button>
      <button onClick={() => navigate("/atm")}>ATM</button>
      <button onClick={() => navigate("/transactions")}>Transactions</button>

      <button className="logout" onClick={() => setAuth(false)}>Logout</button>
    </div>
  );
}