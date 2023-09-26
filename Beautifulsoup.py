from bs4 import BeautifulSoup
import requests


def clean_item(my_item):
    position = my_item.find('</')
    return my_item[30: position]
    
    
url = 'https://seaborn.pydata.org/examples/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())

lst = soup.find_all(class_='thumb-label')
for item in lst:
    print(item)
print()

print(clean_item('<span class="thumb-label"><p>lmplot</p>'))

result = []
for item in lst:
    result.append(clean_item(str(item)))
print(*result, sep='\n')
print(f'\nКоличество записей: {len(result)}')
