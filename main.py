"""
Will use https://openweathermap.org/ API to get weather forecast for 5 days.
Weather forecast data with 3 hour step.

It will put all the data from user provided city into data.txt file
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city_name, api_key, units='imperial'):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units={units}'

    print(url)
    r = requests.get(url)
    response = r.json()
    city_name = response['city']['name']

    with open('data.txt', 'w') as file:
        file.write("City, Time, Temperature, Condition\n")
        for forecast in response["list"]:
            file.write(f'{city_name}, {forecast['dt_txt']}, {forecast['main']['temp']}, {forecast['weather'][0]['description']}\n')

api = os.getenv("API_KEY")
city = "Bloomington"
get_weather(city, api)