""" #TODO: Este script acessa o site do IPMA e extrai a previsão do tempo para os próximos dias.


 from selenium import webdriver
from selenium.webdriver.common.by import By

# Configurar o navegador (Chrome)
driver = webdriver.Chrome()

# Acessar o site do IPMA
url = "https://www.ipma.pt/pt/otempo/prev.localidade.hora/"
driver.get(url)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Espera até que a div 'weekly' esteja presente
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "weekly")))
# Localizar a div 'weekly'
weekly_div = driver.find_element(By.XPATH, "//div[@id='weekly']")

# Listar os elementos dentro da div
dias = weekly_div.find_elements(By.XPATH, "./div[contains(@class, 'weekly-column')]")

# Imprimir os textos
for dia in dias:
    print(dia.text)  # Deve exibir a previsão do tempo
 """
""" 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Inicializar o navegador
driver = webdriver.Chrome()
url = "https://www.ipma.pt/pt/otempo/prev.localidade.hora/"
driver.get(url)

# Esperar até que os elementos sejam carregados
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "weekly")))

# Localizar os elementos dentro da div 'weekly'
dias = driver.find_elements(By.XPATH, "//div[@id='weekly']//div[contains(@class, 'weekly-column')]")
sleep(5)
# Criar lista dinâmica para armazenar os dados
previsao = []

for dia in dias:
    data = dia.find_element(By.XPATH, ".//div[@class='date']").text
    temp_min = dia.find_element(By.XPATH, ".//span[@class='tempMin']").text
    temp_max = dia.find_element(By.XPATH, ".//span[@class='tempMax']").text
    prec_prob = dia.find_element(By.XPATH, ".//div[@class='precProb']").text
    
    previsao.append({
        "data": data,
        
        "temp_min": temp_min,
        "temp_max": temp_max,
       
        "prec_prob": prec_prob,
        
    })

# Exibir o JSON gerado dinamicamente
import json
print(json.dumps(previsao, indent=4, ensure_ascii=False))

# Fechar o navegador
driver.quit()
 """

import requests
from bs4 import BeautifulSoup


def get_weather_condition():
    url = "https://www.ipma.pt/pt/otempo/prev.localidade.hora/"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": f"Falha ao obter dados: {response.status_code}"}

    soup = BeautifulSoup(response.content, "html.parser")

    # Encontrar o primeiro elemento com a previsão do tempo
    weather_element = soup.find("img", class_="weatherImg")

    if not weather_element:
        return {"error": "Não foi possível encontrar a previsão do tempo"}

    # Extrair o texto do atributo 'title', que indica a condição climática
    condition = weather_element.get("title")

    return {"condicao": condition}

# Testar a função
print(get_weather_condition())
