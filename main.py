import asyncio
import time
import aiohttp
import datetime
from colour import *

weathers = {
    "Clouds": "Bulutli☁️",
    "Rain": "Yomg'ir🌧️",
    "Drizzle": "Yomg'ir☁️",
    "Clear": "Musaffo☁️",
    "Thunderstorm": "Momaqaldiroq🌩️",
    "Snow": "Qor🌨️",
    "Mist": "Tuman💨",
    "Smoke": "Tuman💨"
}

async def weather(city):
    parameters = {
        'q': city,
        'appid': 'b01e7608c07f15c54ff9d9b64d478705',
        'units': 'metric'
    }
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=parameters) as response:
                req = await response.json()
                temp = req['main']['temp']
                city = req['name']
                description = req['weather'][0]['main']
                if description in weathers:
                    res = weathers[description]
                else:
                    res = "☁"
                wind = req['wind']['speed']
                humidity = req['main']['humidity']
                utc = 10800
                sunrise = datetime.datetime.fromtimestamp(req['sys']['sunrise'] + req['timezone'] - utc).strftime(
                    '%H:%M:%S')
                sunset = datetime.datetime.fromtimestamp(req['sys']['sunset'] + req['timezone'] - utc).strftime('%H:%M:%S')

                info = (
                        f"{city} {blue("shahrining hozirgi ob-havo ma'lumoti:")}\n"
                        f"{blue("Havo:")} {res}\n"
                        f"{blue("🌡️Temperatura:")} {temp} C°\n"
                        f"️{blue("️☁️Namlik:")} {humidity}%\n"
                        f"{blue("🌪️Shamol:")} {wind}\n"
                        f"{blue("🌤️Quyosh chiqishi:")} {sunrise}\n"
                        f"{blue("🌥️Quyosh botishi:")} {sunset}\n"
                        f"{blue("⏱️Sana:")} {datetime.datetime.today().strftime('%Y/%d/%m')}    {blue("Vaqt:")} {datetime.datetime.today().strftime('%H:%M:%S')}"
                        f"\n{'-'*70}")
                print(info)
    except:
        print(yellow("Shahar topilmadi!!!"))

async def main():
    tasks = []
    while True:
        city = input(green("Shahar nomini kiriting: "))
        if city == 'stop':
            print(red("Dastur to'xtadi!!!"))
            break
        task = asyncio.create_task(weather(city))
        tasks.append(task)

        for task in tasks:
            await task

start = time.time()
asyncio.run(main())
end = time.time()
print(red(f"{round(end-start, 2)} sekund vaqt davomida ishladi!!!"))