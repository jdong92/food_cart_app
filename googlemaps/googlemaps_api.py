import googlemaps
from datetime import datetime

# Replace the API key below with a valid API key.
gmaps = googlemaps.Client(key='AIzaSyCX7cz6O-IkZo_UiZiG_yRt5eKFly-hlsM')

# Geocoding and address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
print(gmaps)
print("-------------------------------------")
print(geocode_result)
print("-------------------------------------")
print(geocode_result[0]['formatted_address'])
print("-------------------------------------")
print(geocode_result[0]['geometry']['viewport']['southwest']['lat'])
# print(reverse_geocode_result)
print("-------------------------------------")
print(geocode_result[0]['geometry']['viewport']['southwest']['lng'])
# print(directions_result)
