
import requests
import xmltodict

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
data = xmltodict.parse(response.content)
print(data)

my_array = []
for item in data['ValCurs']['Valute']:
    my_set = [item['CharCode'], item['Nominal'], item['Name'], item['Value']]
    my_array.append(my_set)
    print(my_set)

# print(my_array)
