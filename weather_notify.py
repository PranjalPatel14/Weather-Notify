from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import requests

n = ToastNotifier()
url = "https://freemeteo.in/weather/Ahmedabad/current-weather/location/?gid=9034993&language=english&country=india"
r = requests.get(url, headers={'User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})


print(r.html.find('title', first=True).text)


# soup = BeautifulSoup(htmldata, 'html.parser')
# title = soup.title
# # print(type(title))
# # print(type(soup.navigation))
# # print(type(soup.string))

# current_temp = soup.find_all("div", class_="temp")

# wind_speed= soup.find_all("span", class_="white")
# # print(soup.find_all("span", class_="white")) \


# temp = (str(current_temp))

# wind = (str(wind_speed))

# result = (f"Current Temp:{temp} Wind Speed:{wind}")
# print(result)