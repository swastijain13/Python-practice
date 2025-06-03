import json

with open("/Users/consultadd/Desktop/python/weather_data.json", "r") as file:
    data = json.load(file)

for city in data["list"]:
    name = city["name"]
    temp = city["main"]["temp"]
    pressure = city["main"]["pressure"]
    wind_speed = city["wind"]["speed"]
    weather_desc = city["weather"][0]["description"]

    print(f"City: {name}")
    print(f"Temperature: {temp}°C")
    print(f"Pressure: {pressure} hPa")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Weather: {weather_desc}")
    print("\n")