import requests
import xmltodict

# Получаем список всех городов вылета 
url_city = 'http://api.icstrvl.ru/tour-api/getDepartures.xml'
data = xmltodict.parse(requests.get(url_city).content)
city_array = []
for item in data['result']['cities']['city']:
    city_set = [item['@id'], item['@name']]
    city_array.append(city_set)
    print(city_set)
print()
# Получаем список стран, в которые есть актуальные туры. Если передан идентификатор города вылета,
# то список стран ограничивается теми странами, в которые возможен вылет из данного города.
url_cnt = 'http://api.icstrvl.ru/tour-api/getCountries.xml?city=538729'
data = xmltodict.parse(requests.get(url_cnt).content)
cnt_array = []
for item in data['result']['countries']['country']:
    cnt_set = [item['@position'], item['@name'], item['@id']]
    cnt_array.append(cnt_set)
    print(cnt_set)
print()
# Получаем список всех курортов выбранной страны
url_resort = 'http://api.icstrvl.ru/tour-api/getResorts.xml?cnt=3639153624'
data = xmltodict.parse(requests.get(url_resort).content)
resorts_array = []
for item in data['result']['resorts']['resort']:
    res_set = [item['@id'], item['@name'], item['@country']]
    resorts_array.append(res_set)
    print(res_set)
print()
# Получаем список отелей выбранной страны. Если передан идентификатор города вылета и/или идентификатор курорта в выбранной стране, то список отелей ограничивается теми курортами, в которые возможен вылет из данного города.
url_hotel = 'http://api.icstrvl.ru/tour-api/getHotels.xml?cnt=3639153624&resort=4011410461&city=538729'
data = xmltodict.parse(requests.get(url_hotel).content)
# print(data)
hotels_array = []
for item in data['result']['hotels']['hotel']:
    hotel_set = [item['@id'], item['@name'], item['@category']]
    hotels_array.append(hotel_set)
    print(hotel_set)
print()
