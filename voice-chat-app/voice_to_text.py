import pyttsx3 #text-to-speech
import requests 
import speech_recognition as sr #speech-text

# Initialize TTS engine
engine = pyttsx3.init()

# Set speech rate (optional)
engine.setProperty('rate', 150)  # Speed of speech

# Function to get voice input
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        audio = recognizer.listen(source)
    try:
        print("You said: " + recognizer.recognize_google(audio))
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, the service is down.")
        return None
    



# Function to send message to Rasa and get the response
def send_message_to_rasa(user_input):
    url = "http://localhost:5006/webhooks/rest/webhook"
    headers = {"Content-Type": "application/json"}
    data = {"sender": "user", "message": user_input}
    try:
        response = requests.post(url, json=data, headers=headers)
        response_data = response.json()
        for r in response_data:
            print("Rasa says: " + r.get('text'))  # Print Rasa's text response
            engine.say(r.get('text'))  # Convert text to speech
            engine.runAndWait()  # Play the speech
    except Exception as e:
        print(f"Error sending message to Rasa: {e}")

if __name__ == "__main__":
    while True:
        user_input = get_voice_input()  # Get voice input from the user
        if user_input:
            send_message_to_rasa(user_input)  # Send input to Rasa and get response
        else:
            print("No input detected. Please try again.")
