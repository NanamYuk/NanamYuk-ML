# Import required library
import requests
from datetime import datetime
today = datetime.today()

# API Key for OpenWeatherMap API
api_key = "81c713c1b0fea513c62681c97920daa9"

# Function for defining root_url
def root_url(url_param, city_name, api_key):
  root_url = ["https://history.openweathermap.org/data/2.5/aggregated/month?", "https://api.openweathermap.org/data/2.5/weather?"]
  root_url = root_url[url_param]
  url = [f"{root_url}month={today.month}&q={city_name},ID&appid={api_key}", f"{root_url}q={city_name},ID&appid={api_key}"]
  url = url[url_param]
  r = requests.get(url)
  data = r.json()
  return r, data

# Function for calling response from API
def weather(city_name):
  # Calling root_url function for history data
  r, data = root_url(0, city_name, api_key)
  
  # Checking if response data is 'code'
  if 'cod' in data:
    # Checking if the status of 'cod' is 200
    if data['cod'] == 200:
      # Getting the temperature from the json data
      temp = data['result']['temp']['mean'] - 273.15
      # Getting the humidity from the json data
      humidity = data['result']['humidity']['mean']
      
  # Checking if response data is 'code'
  elif 'code' in data:
    if data['code'] == 404000:
      # Calling root_url function for current data
      r, data = root_url(1, city_name, api_key)

      if 'cod' in data:
        # Checking if the status 'cod' is 200
        if data['cod'] == 200:
          # Getting the temperature from the json data
          temp = data['main']['temp'] - 273.15
          # Getting the humidity from the json data
          humidity = data['main']['humidity']
        else:
          return "Kota tidak terdaftar"

    else:
      return "Nama kota tidak boleh kurang dari 3 karakter"

  # Returning temp and humidity value
  return round(temp, 2), humidity