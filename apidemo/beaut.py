""" 

import requests
from bs4 import BeautifulSoup

url = "https://www.ipma.pt/pt/otempo/prev.localidade.hora/"  # Substitua pela URL correta
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

# Agora você pode encontrar a div desejada
weekly_div = soup.find("div", {"id": "weekly"})
daily_div = soup.find("div", {"id": "daily"})

print("Weekly:", weekly_div)
print("Daily:", daily_div)
 """

import requests

url = "https://api.ipma.pt/public-data/forecast/aggregate/1060300.json"  # Use o código correto da sua localidade
response = requests.get(url)
data = response.json()  # Converte para JSON

print(data)  # Exibe os dados da previsão
