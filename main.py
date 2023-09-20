import requests

# User input for city name
city_name = input("Enter the name of a city: ")

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = 'YOUR_API_KEY'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']
    
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description}")
else:
    print(f"Error: Unable to retrieve weather data for {city_name}.")
