import { Link } from "react-router-dom";

function Navbar() {
  const navStyle = {
    backgroundColor: "#4B0082",
    padding: "10px 20px",
    display: "flex",
    justifyContent: "space-between",
    color: "white",
  };

  const linkStyle = { marginRight: "15px", color: "white", textDecoration: "none" };

  return (
    <nav style={navStyle}>
      <h1>Rasa Auth</h1>
      <div>
        <Link to="/" style={linkStyle}>Login</Link>
        <Link to="/signup" style={linkStyle}>Signup</Link>
        <Link to="/chatbot" style={linkStyle}>Chatbot</Link>
      </div>
    </nav>
  );
}

export default Navbar;
