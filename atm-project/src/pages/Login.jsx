import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles.css";

export default function Login({ setAuth }) {
  const [accountId, setAccountId] = useState("");
  const [name, setName] = useState("");
  const [pin, setPin] = useState("");
  const navigate = useNavigate();

  const login = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          account_id: Number(accountId),
          name: name,
          pin: Number(pin),
        }),
      });

      const data = await response.json();

      if (response.ok) {
        // ✅ store token
        localStorage.setItem("token", data.access_token);

        setAuth(true);
        alert("Login successful ✅");
        navigate("/dashboard");
      } else {
        alert(data.detail || "Invalid credentials ❌");
      }
    } catch (error) {
      console.error("ERROR:", error);
      alert("Server not connected ⚠️");
    }
  };

  return (
    <div className="login-bg">
      <form className="glass-card" onSubmit={login}>
        <h1>🏦 MyBank</h1>

        <input
          type="number"
          placeholder="Account ID"
          value={accountId}
          onChange={(e) => setAccountId(e.target.value)}
        />

        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          type="password"
          placeholder="PIN"
          value={pin}
          onChange={(e) => setPin(e.target.value)}
        />

        <button type="submit">Login</button>
      </form>
    </div>
  );
}