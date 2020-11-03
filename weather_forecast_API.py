import pyowm

## Copy and paste your key into the line below
KEY = '1234567890abcdefghijklmnopqrstuvwxyz'

## Place your location (city, country code) into the line below
location = 'Bordeaux,fr'

owm = pyowm.OWM(KEY)
fc = owm.three_hours_forecast(location)
f = fc.get_forecast()
icons = [weather.get_weather_icon_name() for weather in f]
