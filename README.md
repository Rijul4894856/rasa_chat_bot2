🤖 Rasa Chatbot Project

An AI-powered chatbot application built using Rasa, React.js frontend, Node.js backend, and SQLite database.
The chatbot supports text & voice input/output, user authentication (signup/login/OTP), and integration with APIs (Weather, YouTube, Spotify, Google Search, etc.).

📦 Prerequisites

Python 3.8 – 3.10 (Rasa compatibility)

Node.js v16+ and npm

SQLite (can be extended to PostgreSQL)

Git

📂 Project Structure
project-root/
│
├── backend/                 
│   ├── Roots/               # Authentication & routes
│   │   └── AUTH.js
│   │
│   ├── app.py               # Python script (integrations/voice)
│   ├── db.js                # Database connection
│   ├── server.js            # Main backend server
│   ├── user.db              # SQLite database
│   │
│   └── package.json
│
├── actions/                 # Rasa custom actions
│   └── actions.py
│
├── data/                    # Rasa training data
│   ├── chit-chat.yml
│   ├── rules-have.yml
│   ├── stories.yml
│   └── ...
│
├── frontend/                
│   ├── public/              # Static files
│   │   └── chatbot/         
│   │       ├── index.html   # Chatbot UI
│   │       ├── style.css
│   │       ├── script.js
│   │       └── voice.py     # Voice-to-text Python script
│   │
│   └── src/                 # React application source
│       ├── components/      # Reusable UI components
│       │   └── navbar.js
│       │
│       ├── pages/           # React pages
│       │   ├── login.js
│       │   ├── signup.js
│       │   └── chatbot.js
│       │
│       └── App.js
│
├── rasa/                    # (Optional: configs)
│   ├── domain.yml
│   ├── config.yml
│   └── credentials.yml
│
└── README.md                # Documentation

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

2️⃣ Setup Rasa (Python environment)
python -m venv rasa_env
source rasa_env/bin/activate   # (Linux/Mac)
rasa_env\Scripts\activate     # (Windows)
pip install rasa

3️⃣ Run Rasa servers

Rasa Server (port: 5006)

rasa run --enable-api --cors "*" --port 5006


Rasa Action Server (port: 5055)

rasa run actions --port 5055

4️⃣ Start Backend (Node.js)
cd backend
npm install
node server.js   # Backend server runs on port 5000

5️⃣ Start Frontend (React App)
cd frontend
npm install
npm start   # Runs on port 3000

🔐 Authentication Flow

Signup → Register with username, email, phone, password, OTP verification

Login → Verify credentials (passwords hashed with bcrypt)

Database → User data stored in SQLite (user.db)


🤖 Bot Functionalities

✅ Weather updates via API

✅ YouTube & Spotify opening

✅ Web search (Google integration)

✅ Voice & text input/output

✅ User authentication (signup/login + OTP)

✅ Chit-chat, stories, rules (custom Rasa NLU data)

🗄️ Database Schema Example
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone_number TEXT,
    password_hash TEXT NOT NULL,
    otp_verified BOOLEAN DEFAULT 0
);

🚀 Run Flow

Activate Python env → Run Rasa server (5006) & Action server (5055)

Start Backend → node server.js (runs on 5000)

Start Frontend → npm start (runs on 3000)

Go to frontend → Signup → Login → Chatbot page

Interact with the chatbot 🎉

📌 Notes

Ensure correct Python version (Rasa doesn’t support 3.12 yet).

Ports used:

Frontend → 3000

Backend → 5000

Rasa Server → 5006

Rasa Actions → 5055

Update .env file for API keys (e.g., weather API).

Install dependencies for voice features (speechrecognition, pyaudio).
