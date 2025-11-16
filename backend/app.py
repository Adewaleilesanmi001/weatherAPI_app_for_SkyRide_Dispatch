import requests
import os
from dotenv import load_dotenv # Import env file module
load_dotenv()  #Loading Env module 
from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


geocoding_api_key = os.getenv('GEOCODING_API') # Import env file that contain api keys 
current_weather_api_key = os.getenv('CURRENT_WEATHER_API') # Import env file that contain api keys 
# geocoding api
# city = 'new york' # creating variable to store location

# print (data['results'][0]['lat'])

#helper function 
def converter_kelvin_to_celcius (value: float):
    data = round(value - 273.15, 1) 
    return data
    

def cordinate (city):

    url = f"https://api.geoapify.com/v1/geocode/search?text={city}&format=json&apiKey={geocoding_api_key}"
    respose = requests.get(url)
    data = respose.json()

    lon = data['results'][0]['lon']
    lat = data['results'][0]['lat']
    return lat, lon


lat, lon  = cordinate('new york')

def weatherapp(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={current_weather_api_key}'

    response= requests.get(url)
    data = response.json()
    return data

data = weatherapp(lat, lon)
# print (data.get('main', {}).get ('feels_like'))
# print (data.get('weather')[0].get('id'))
# data = data.get('weather')
# print(data.get('clouds').get('all'))

def formatter (payload: dict[str, Any]):
    weather = payload.get('weather')[0]
    main = payload.get('main')
    wind = payload.get('wind')
    sys = payload.get('sys')

    return {
        'city': payload.get('name'),
        'country': sys.get('country'),
        'coordinates': payload.get('coord'),
        'conditions': {
            'label': weather.get('main'),
            'description': weather.get('description'),
            'icon': weather.get('icon')
            },

        'temperature': {
            'current_c': converter_kelvin_to_celcius(main.get('temp', 0)),
            'feels_like_c': converter_kelvin_to_celcius(main.get('feels_like', 0)),
            'min_c': converter_kelvin_to_celcius(main.get('temp_min', 0)),
            'max_c': converter_kelvin_to_celcius(main.get('temp_max', 0)),
        },

        'humidity' : main.get('humidity'),
        'pressure': main.get('pressure'),
        'wind': {
            'speed_mps': wind.get('speed'),
            'direction_deg': wind.get('deg'),
            'gust_mps': wind.get('gust'),
        },
        'visibility_m': payload.get('visibility'),
        'cloud_cover_pct': payload.get('clouds').get('all'),
        'timestamp': payload.get('id'),
        'timezone_offset_s': payload.get('timezone'),
        'source': 'openweathermap & geoapify',
        'raw': payload,

    }







@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/weather")
def root(city: str):
    lat, lon = cordinate (city)
    payload = weatherapp(lat, lon)
    formatted_data = formatter (payload)
    formatted_data['city'] = city
    return formatted_data
