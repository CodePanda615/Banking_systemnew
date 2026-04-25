import React from "react";
import { Routes, Route } from "react-router-dom";

import Login from "./pages/login";
import Dashboard from "./pages/Dashboard";
import ATM from "./pages/ATM";
import Transactions from "./pages/Transactions";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/atm" element={<ATM />} />
      <Route path="/transactions" element={<Transactions />} />
    </Routes>
  );
}

export default App;