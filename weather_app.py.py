import requests

API_KEY = "d12a83510035dc33776ee18ce7c692b4"  # replace with your OpenWeatherMap key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather = data["weather"][0]["description"]
        temp = main["temp"]
        humidity = main["humidity"]
        print(f"\nWeather in {city}:")
        print(f"Condition: {weather}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%\n")
    else:
        print("City not found!")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
