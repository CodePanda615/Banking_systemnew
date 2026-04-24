export default function Login({ pin, setPin, handleLogin }) {
  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1 style={styles.heading}>🏦 ATM Login</h1>

        <input
          type="password"
          placeholder="Enter PIN"
          value={pin}
          onChange={(e) => setPin(e.target.value)}
          style={styles.input}
        />

        <button onClick={handleLogin} style={styles.button}>
          Login
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
    width: "350px",
    backgroundColor: "#102c5a",
    padding: "30px",
    borderRadius: "20px",
    textAlign: "center",
  },
  heading: {
    color: "white",
    marginBottom: "20px",
  },
  input: {
    width: "100%",
    padding: "12px",
    marginBottom: "20px",
  },
  button: {
    width: "100%",
    padding: "12px",
    backgroundColor: "#1d4ed8",
    color: "white",
    border: "none",
  },
};