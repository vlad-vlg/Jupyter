# Парсер прогноза погоды по данным Гисметео
# Прогноз погоды в Москве на 10 дней

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.gismeteo.ru/weather-moscow-4368/10-days/'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
resp = requests.get(url, headers=headers)

soup = BeautifulSoup(resp.text, 'html.parser')

print(soup.prettify())

# Определяем список дат:
dates = soup.find_all('div', class_='date')
dates = [date.string for date in dates]
print(dates, '\n')

# Определяем список дней недели:
days = soup.find_all('div', class_='day')
days = [day.string for day in days]
print(days, '\n')

# Определяем полный список температур:
t = soup.find_all('span', class_='unit unit_temperature_c')
t = [x.string for x in t]

# Определяем необходимый диапазон температур по датам:
maxt = t[1:21:2]
mint = t[2:22:2]
print(maxt, '\n')
print(mint, '\n')

# Определяем информацию по ветру:
wind = soup.find_all('span', class_='wind-unit unit unit_wind_m_s')
wind = [x.string for x in wind]

wind_speed = wind[0:10]
wind_gust = wind[10:]
print(wind_speed, '\n')
print(wind_gust, '\n')

# Определяем информацию по давлению:
pressure = soup.find_all('span', class_='unit unit_pressure_mm_hg')
pressure = [x.string for x in pressure][1:21:2]
print(pressure, '\n')

# Собираем всю полученную информацию в один массив:
result = [days, maxt, mint, wind_speed, wind_gust, pressure]
print(result, '\n')

# Создаем массив Pandas для дальнейшей обработки и анализа данных:
forecast = pd.DataFrame(result, 
        index=('День недели', 'Температура макс, С', 'Температура мин, С', 'Скорость ветра, м/с', 'Порывы ветра, м/с', 'Давление, мм.рт.ст.'),
        columns=dates)
print(forecast)
