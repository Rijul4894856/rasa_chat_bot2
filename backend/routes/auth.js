const express = require("express");
const router = express.Router();
const db = require("../db");

// SIGNUP
router.post("/signup", (req, res) => {
  const { username, email, phone, password } = req.body;

  const stmt = `INSERT INTO users(username, email, phone, password) VALUES (?, ?, ?, ?)`;

  db.run(stmt, [username, email, phone, password], function (err) {
    if (err) {
      if (err.message.includes("UNIQUE constraint failed")) {
        return res.json({ msg: "Email or phone already exists" });
      }
      return res.json({ msg: "Error registering user" });
    }
    res.json({ msg: "User registered successfully" });
  });
});

// LOGIN
router.post("/login", (req, res) => {
  const { email, password } = req.body;

  const stmt = `SELECT * FROM users WHERE email=? AND password=?`;

  db.get(stmt, [email, password], (err, row) => {
    if (err) return res.json({ msg: "Error logging in" });
    if (row) res.json({ msg: "Login successful" });
    else res.json({ msg: "Invalid email or password" });
  });
});

module.exports = router;
