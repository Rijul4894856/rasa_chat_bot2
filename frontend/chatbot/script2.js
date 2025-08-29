const messagesDiv = document.getElementById('messages');
const startButton = document.getElementById('start-recording');
const sendButton = document.getElementById('send-button');
const userInput = document.getElementById('user-input');
const bear = document.querySelector('.bear-avatar');

// Function to add messages to the chat
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.textContent = text;
    messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// Function to play Text-to-Speech (TTS)
function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.pitch = 1;
    utterance.rate = 1;
    window.speechSynthesis.speak(utterance);

    // 🐻 Bear Talking Animation
    bear.classList.add('talking');
    utterance.onend = () => bear.classList.remove('talking');
}

// Function to send a message
function sendMessage(message) {
    if (!message.trim()) return; // Ignore empty messages
    addMessage(message, 'user');

    fetch('http://localhost:5006/webhooks/rest/webhook', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message, sender: 'user' })
    })
    .then(response => response.json())
    .then(data => {
        const botReply = data[0]?.text || 'Sorry, I didn\'t understand that.';
        addMessage(botReply, 'bot');
        speak(botReply);
    })
    .catch(err => {
        const errorReply = 'Error communicating with the chatbot.';
        addMessage(errorReply, 'bot');
        speak(errorReply);
        console.error('Fetch error:', err);
    });
}

// Send message when clicking send button
sendButton.addEventListener('click', () => {
    const message = userInput.value;
    sendMessage(message);
    userInput.value = '';
});

// Voice recognition setup
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'en-US';

// Start voice recognition on button click
startButton.addEventListener('click', () => {
    recognition.start();
    bear.classList.add('listening'); // 🐻 Raise ears when listening
});

// When voice input is detected
recognition.onresult = (event) => {
    const userMessage = event.results[0][0].transcript.trim();
    sendMessage(userMessage);
};

// Stop listening animation when recording stops
recognition.onend = () => {
    bear.classList.remove('listening'); 
};

// Send message when Enter key is pressed
userInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        sendButton.click();
    }
});