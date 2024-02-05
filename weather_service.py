import requests
from api_keys import OPENWEATHERMAP_API_KEY
from config import OWM_ENDPOINT, LATITUDE, LONGITUDE


def get_weather_data():
    weather_params = {
        "lat": LATITUDE,
        "lon": LONGITUDE,
        "appid": OPENWEATHERMAP_API_KEY,
        "exclude": "current, minutely, daily"
    }
    response = requests.get(OWM_ENDPOINT, params=weather_params)
    response.raise_for_status()
    return response.json()
