# import webbrowser
# import subprocess
# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet

# class ActionOpenYouTube(Action):
#     def name(self):
#         return "action_open_youtube"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message(text="Opening YouTube...")
#         webbrowser.open("https://www.youtube.com")
#         return []

# class ActionOpenSpotify(Action):
#     def name(self):
#         return "action_open_spotify"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message(text="Opening Spotify...")
#         try:
#             subprocess.Popen(["spotify"])  # Opens Spotify if installed
#         except FileNotFoundError:
#             dispatcher.utter_message(text="Spotify is not installed.")
#         return []

# class ActionWebSearch(Action):
#     def name(self):
#         return "action_web_search"

#     def run(self, dispatcher, tracker, domain):
#         query = tracker.get_slot("query")
#         if query:
#             search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
#             dispatcher.utter_message(text=f"Searching for {query}...")
#             webbrowser.open(search_url)
#         else:
#             dispatcher.utter_message(text="What would you like to search for?")
#         return []
