from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")
location_data = geolocator.geocode("Sydney")

if location_data:
    print(f"Latitude: {location_data.latitude}, Longitude: {location_data.longitude}")
else:
    print("Failed to fetch location.")
