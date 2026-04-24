export default function Dashboard({
  balance,
  withdrawMoney,
  depositMoney,
  logout
}) {
  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1>🏦 ATM Machine</h1>

        <h2>Balance: ₹{balance}</h2>

        <button style={styles.button} onClick={withdrawMoney}>
          Withdraw ₹500
        </button>

        <button style={styles.button} onClick={depositMoney}>
          Deposit ₹1000
        </button>

        <button style={styles.logoutButton} onClick={logout}>
          Logout
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    minHeight: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#0a1f44",
  },
  card: {
    width: "400px",
    backgroundColor: "#102c5a",
    padding: "30px",
    borderRadius: "20px",
    color: "white",
    textAlign: "center",
  },
  button: {
    width: "100%",
    padding: "12px",
    marginBottom: "10px",
    backgroundColor: "#1d4ed8",
    color: "white",
    border: "none",
  },
  logoutButton: {
    width: "100%",
    padding: "12px",
    backgroundColor: "red",
    color: "white",
    border: "none",
  },
};