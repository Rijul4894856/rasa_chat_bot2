import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

function Signup() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSignup = async () => {
    try {
      const res = await fetch("http://localhost:5000/api/auth/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, email, phone, password }),
      });
      const data = await res.json();
      if (data.msg === "User registered successfully") {
        navigate("/");
      } else {
        alert(data.msg);
      }
    } catch (err) {
      alert("Error connecting to server");
    }
  };

  return (
    <div style={{ display: "flex", justifyContent: "center", alignItems: "center", height: "90vh" }}>
      <div style={{ backgroundColor: "white", padding: "40px", borderRadius: "15px", boxShadow: "0 4px 10px rgba(0,0,0,0.2)", width: "350px" }}>
        <h2 style={{ textAlign: "center", marginBottom: "20px" }}>Signup</h2>
        <input type="text" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} style={{ width: "100%", padding: "10px", margin: "10px 0", borderRadius: "8px", border: "1px solid #ccc" }} />
        <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} style={{ width: "100%", padding: "10px", margin: "10px 0", borderRadius: "8px", border: "1px solid #ccc" }} />
        <input type="text" placeholder="Phone" value={phone} onChange={e => setPhone(e.target.value)} style={{ width: "100%", padding: "10px", margin: "10px 0", borderRadius: "8px", border: "1px solid #ccc" }} />
        <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} style={{ width: "100%", padding: "10px", margin: "10px 0", borderRadius: "8px", border: "1px solid #ccc" }} />
        <button onClick={handleSignup} style={{ width: "100%", padding: "10px", backgroundColor: "#4B0082", color: "white", border: "none", borderRadius: "8px" }}>Signup</button>
        <p style={{ textAlign: "center", marginTop: "10px" }}>Already have an account? <Link to="/">Login</Link></p>
      </div>
    </div>
  );
}

export default Signup;
