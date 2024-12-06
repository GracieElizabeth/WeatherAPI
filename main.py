"""
Will use https://openweathermap.org/ API to get weather forcast for 5 days
Weather forcast data with 3 hour step

main.py will put all the data from user provided city into data.txt file
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

city_name = "Bloomington"

url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'

print(url)
r = requests.get(url)
response = r.json()

city = response['city']['name']

with open('data.txt', 'w') as file:
    file.write("City, Time, Temperature, Condition\n")
    for forecast in response["list"]:
        file.write(f'{city}, ')
        file.write(f'{forecast['dt_txt']}, ')
        file.write(f'{forecast['main']['temp']}, ')
        for condition in forecast['weather']:
            file.write(f'{condition['description']}\n')