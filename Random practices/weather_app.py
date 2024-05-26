'''
    Create a simple weather forecast application that retrieves data from an API like Tomorrow.IO. 
    Allow users to enter a city name and display the current weather conditions.
'''
import requests


city = input('Enter city name: ')

url = f"https://api.tomorrow.io/v4/timelines?location={city}&fields=temperature,weatherCode&units=imperial&apikey={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    forecast = data['data']['timelines'][0]
    interval = forecast['intervals'][0]['values']
    
    temperature = interval['temperature']
    weather_code = interval['weatherCode']
# Adjusted code handling missing keys
    precipitation_probability = interval['values'].get('precipitationProbability', 'N/A')
    humidity = interval['humidity']
    wind_speed = interval['windSpeed']
    state_code = data['location']['region']

    print(f'Temperature: {temperature}°F')
    print(f'Weather Code: {weather_code}')
    print(f'Precipitation Probability: {precipitation_probability}%')
    print(f'Humidity: {humidity}%')
    print(f'Wind Speed: {wind_speed} mph')
    print(f'State: {state_code}')
else:
    print('Error fetching weather data')

