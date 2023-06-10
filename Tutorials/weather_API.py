import requests

API_KEY = "b53ee628b3c285cd0bca71d40f8fe982"
city = input("Hallo! Bitte gib eine Stadt ein: ")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
data = requests.get(url).json()
temp = data['main']['temp']
humidity = data['main']['humidity']

print(f'In {city} beträgt die Temperatur {temp}. Die Luftfeuchtigkeit beträgt {humidity}.')