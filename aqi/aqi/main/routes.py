import requests
from datetime import datetime

from flask import render_template,Blueprint, url_for, redirect, request
from aqi.main.forms import GetCity
from geopy.geocoders import Nominatim



main = Blueprint("main", __name__)

def getData(city):
  locator = Nominatim(user_agent="myGeocoder")
  location = locator.geocode(city)
  lat = location.latitude
  lon = location.longitude
  api_key = "7c3ee70966a7361a697fda3ca7a310ac"
  URL = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
  
  response = requests.get(URL)
  data = ""
  if(response.status_code == 200):
    data = response.json()
  else:
    data="!D"
  return data

@main.route("/", methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
def home():
  form = GetCity()
  if form.validate_on_submit():
    city = form.city.data
    return redirect(url_for("main.airindex", city=city))
  return render_template("home.html", form=form)

@main.route("/airindex", methods=["GET", "POST"])
def airindex():
  city = request.args['city']
  data = getData(city)

  aqi = data["list"][0]["main"]
  components = data["list"][0]["components"]

  labels, values = zip(*components.items())
  labels, values = list(labels), list(values)

  now = datetime.now()

  return render_template("airindex.html", aqi = aqi, labels = labels, values = values, now = now)