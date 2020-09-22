import requests
from bs4 import BeautifulSoup

url = 'http://www.cbr.ru/scripts/XML_daily.asp'


names_values = {}

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
name = soup.findAll('name')
values = soup.findAll('value')
for i in range(0, len(name)):
    values[i] = str(values[i]).replace('<value>', '')
    values[i] = str(values[i]).replace('</value>', '')
    names_values[str(name[i])] = values[i]

print('Курс гонконского доллара к российскому рублю: ', names_values['<name>Гонконгских долларов</name>'])
