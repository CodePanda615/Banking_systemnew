import { useState } from "react";
import Login from "./components/Login";
import Dashboard from "./components/Dashboard";

export default function App() {
  const [pin, setPin] = useState("");
  const [loggedIn, setLoggedIn] = useState(false);
  const [balance, setBalance] = useState(10000);

  const handleLogin = () => {
    if (pin === "1234") {
      setLoggedIn(true);
    } else {
      alert("Wrong PIN");
    }
  };

  const withdrawMoney = () => {
    if (balance >= 500) {
      setBalance(balance - 500);
    } else {
      alert("Insufficient balance");
    }
  };

  const depositMoney = () => {
    setBalance(balance + 1000);
  };

  const logout = () => {
    setLoggedIn(false);
    setPin("");
  };

  return (
    <>
      {!loggedIn ? (
        <Login
          pin={pin}
          setPin={setPin}
          handleLogin={handleLogin}
        />
      ) : (
        <Dashboard
          balance={balance}
          withdrawMoney={withdrawMoney}
          depositMoney={depositMoney}
          logout={logout}
        />
      )}
    </>
  );
}