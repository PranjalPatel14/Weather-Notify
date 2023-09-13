from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import requests

n = ToastNotifier()
url = "https://freemeteo.in/weather/Ahmedabad/current-weather/location/?gid=9034993&language=english&country=india"
r = requests.get(url, headers={'User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})

api = "dfda56122d04af1b23790dd7d2ffc801"

# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
