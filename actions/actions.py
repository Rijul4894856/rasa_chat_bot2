# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import webbrowser
import wikipedia
import subprocess
import requests  # ✅ For Weather API integration

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import os
from dotenv import load_dotenv

from rasa_sdk.executor import CollectingDispatcher


# ✅ Load API key from .env file
load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

# 🌤 Action to Fetch Weather Info
class ActionGetWeather(Action):
    def name(self):
        return "action_get_weather"

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot("location")
        print(f"DEBUG: Requested weather for '{location}'")  

        if location:
            if not api_key:
                dispatcher.utter_message(text="Weather API key is missing!")
                return []

            # ✅ Fetch weather info using API
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            if data.get("cod") != 200:
                message = f"Sorry, I couldn't find weather information for {location}. Please try another city."
            else:
                temp = data["main"]["temp"]
                description = data["weather"][0]["description"]
                message = f"The current temperature in {location} is {temp}°C with {description}."
                dispatcher.utter_message(text=message)
                # ✅ Set slots
                return [
                    SlotSet("temp", str(temp)),
                    SlotSet("description", description),
                    SlotSet("location", location)
                ]
        else:
            message = "Please provide a location to get the weather information."
            dispatcher.utter_message(text=message)

        return []

# 📺 Open YouTube
class ActionOpenYouTube(Action):
    def name(self):
        return "action_open_youtube"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
        return []

# 🎵 Open Spotify
class ActionOpenSpotify(Action):
    def name(self):
        return "action_open_spotify"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Opening Spotify...")
        try:
            subprocess.Popen(["spotify"])
        except FileNotFoundError:
            dispatcher.utter_message(text="Spotify is not installed.")
        return []

# 💬 Open WhatsApp
class ActionOpenWhatsapp(Action):
    def name(self):
        return "action_open_whatsapp"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Opening WhatsApp...")
        try:
            subprocess.Popen(["whatsapp"])
        except FileNotFoundError:
            dispatcher.utter_message(text="WhatsApp is not installed.")
        return []

# 🔍 Web Search
class ActionWebSearch(Action):
    def name(self):
        return "action_web_search"

    def run(self, dispatcher, tracker, domain):
        query = tracker.get_slot("query")
        if not query:
            dispatcher.utter_message(text="What would you like to search for?")
            return []

        # ✅ Filter unnecessary words
        trigger_words = ["search", "google", "find"]
        query_words = query.split()
        filtered_query = " ".join(word for word in query_words if word.lower() not in trigger_words)

        if not filtered_query:
            dispatcher.utter_message(text="Please provide a valid search term.")
            return []

        search_url = f"https://www.google.com/search?q={filtered_query.replace(' ', '+')}"
        dispatcher.utter_message(text=f"Searching for: {filtered_query}")
        webbrowser.open(search_url)

        return [SlotSet("query", None)]

# ❓ Answer General Questions Using Wikipedia
class ActionGeneralQuestion(Action):
    def name(self):
        return "action_general_question"

    def run(self, dispatcher, tracker, domain):
        query = tracker.latest_message.get("text")
        print(f"DEBUG: Received question: {query}")  

        try:
            answer = wikipedia.summary(query, sentences=2)
            dispatcher.utter_message(text=answer)
        except wikipedia.exceptions.DisambiguationError as e:
            dispatcher.utter_message(text=f"Too many meanings! Please specify: {', '.join(e.options[:5])}")
        except wikipedia.exceptions.PageError:
            dispatcher.utter_message(text="Sorry, I couldn't find an answer.")
        except Exception:
            dispatcher.utter_message(text="I'm not sure. Try searching online.")
        return []

# -------------------------------------
# date 12/03/2025

# class ActionGetTime(Action):
#     def name(self):
#         return "action_get_time"

#     def run(self, dispatcher, tracker, domain):
#         location = tracker.get_slot("location")

#         if not location:
#             dispatcher.utter_message(text="Please provide a location to check the time.")
#             return []

#         try:
#             # Convert location to lowercase & replace spaces with underscores for API request
#             formatted_location = location.lower().replace(" ", "_")

#             # WorldTimeAPI request
#             response = requests.get(f"http://worldtimeapi.org/api/timezone/{formatted_location}")

#             if response.status_code != 200:
#                 dispatcher.utter_message(text=f"Sorry, I couldn't find the time for '{location}'. Try another city.")
#                 return []

#             data = response.json()
#             current_time = data["datetime"][:19]  # Extract YYYY-MM-DD HH:MM:SS format

#             dispatcher.utter_message(text=f"The current time in {location.title()} is {current_time}.")

#         except Exception as e:
#             print(f"Error: {e}")  # Debugging logs
#             dispatcher.utter_message(text="Sorry, there was an error fetching the time. Please try again later.")

#         return []