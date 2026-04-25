import React from "react";

export default function Transactions({ txns }) {
  return (
    <div>
      <h1>Transactions</h1>
      {txns.map((t, i) => (
        <p key={i}>{t}</p>
      ))}
    </div>
  );
}
