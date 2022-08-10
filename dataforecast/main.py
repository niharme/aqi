import requests
from geopy.geocoders import Nominatim
import pandas as pd

city = "Rourkela"
locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode(city)
lat = location.latitude
lon = location.longitude

start = 1656637261
end = 1660039424
api_key = "7c3ee70966a7361a697fda3ca7a310ac"

url_hist = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={api_key}"

response = requests.get(url_hist)

data = response.json()
