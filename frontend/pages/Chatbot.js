function Chatbot() {
    const containerStyle = {
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      height: "90vh",
      backgroundColor: "#f0f2f5",
    };
  
    const iframeStyle = {
      width: "80%",
      height: "70%",
      border: "1px solid #ccc",
      borderRadius: "10px",
    };
  
    return (
      <div style={containerStyle}>
        <h1 style={{ marginBottom: "20px" }}>Welcome to Rasa Chatbot</h1>
        <iframe
          src="http://localhost:5006"
          title="Rasa Chatbot"
          style={iframeStyle}
        ></iframe>
      </div>
    );
  }
  
  export default Chatbot;
  
