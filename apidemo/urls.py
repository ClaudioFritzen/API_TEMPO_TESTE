from django.contrib import admin
from django.urls import path
from selenium import webdriver
from selenium.webdriver.common.by import By

from ninja import NinjaAPI 

# Inicializa a API
api = NinjaAPI()

# Função para obter previsão do tempo padrão
""" @api.get("/weather")
def pesquisapadrao(request):
    import time
    driver = webdriver.Chrome()  # Inicia o navegador
    driver.get("https://www.ipma.pt/pt/otempo/prev.localidade.hora/")  # Abre a página

    # esperamos 3 segundos para garantir que a página carregue completamente
    time.sleep(3)
    
    element = driver.find_element(By.ID, "weekly").text
    print(f"Elementos {element}")  # Exibe o texto do elemento 'weekly'

    # Fecha o navegador
    driver.quit()

    return {"previsao_semanal": element}  # Retorna os dados da previsão """



#buscar por dia

# peço o dia da semana e distrito e cidade
#@api.get("/weather/{distrito}/{cidade}/{dia}")
# criamos uma funcao onde pegamos os dados e procuros esse dias la 
# encontramos o card onde diz dia e pegamos todos os dias que tem acho sao 5 dias a partir da data atual

@api.get("/")
def abrindo_api(request):
    import time
    driver = webdriver.Chrome()
    driver.get("https://www.ipma.pt/pt/otempo/prev.localidade.hora/")
    time.sleep(3)

    # Encontrar o elemento pai 
    div_pai = driver.find_element(By.ID, "weekly")

    # pegamos filhos do elemento pai
    proximos_dias = div_pai.find_elements(By.CLASS_NAME, "weekly-column")

    # lista dos dias
    previsao_dias = []

    #  Vamos passar por todos os item encontrados
    for dia in proximos_dias:
        # Capturamos o texto de cada dia
        dia_texto = dia.find_element(By.CLASS_NAME, "date").text
        temp_min = dia.find_element(By.CLASS_NAME, "tempMin").text
        temp_max = dia.find_element(By.CLASS_NAME, "tempMax").text

        # pegar o title do img
        img = dia.find_element(By.TAG_NAME, "img")
        img_title = img.get_attribute("title")
        print(f"Dia: {dia_texto}, Temperatura Mínima: {temp_min}, Temperatura Máxima: {temp_max}, Condição: {img_title}")
        
        # Adicionamos os dados à lista
        previsao_dias.append({
            "dia": dia_texto,
            "temperatura_minima": temp_min,
            "temperatura_maxima": temp_max,
            "condicao": img_title
        })

    driver.quit()  # Fecha o navegador

    return {"message": "Bem-vindo à API de previsão do tempo!",
            "previsao_dias": previsao_dias
    }

@api.get("dia")
def pegar_dia_especifico(request, dia: str):

    dia = dia.strip() # Remover espaços em branco desnecessários

    # conferir se o dia esta na lista de date do weekly
    import time
    driver = webdriver.Chrome()
    driver.get("https://www.ipma.pt/pt/otempo/prev.localidade.hora/")
    time.sleep(3)

    # Encontrar o elemento pai 
    div_pai = driver.find_element(By.ID, "weekly")

    # pegamos filhos do elemento pai
    proximos_dias = div_pai.find_elements(By.CLASS_NAME, "weekly-column")
    
    # pesquisando no proximos dias
    for dia_pesquisado in proximos_dias:
        # usaremos o dia 15
        dia_str = dia_pesquisado.find_element(By.CLASS_NAME, "date").text.strip()
        print(f"Dia_str {dia_str}")
        numero_dia = dia_str.split(',')[-1].strip()
        print(f"numero_dia {numero_dia}")

        print("Antes do if")
        print(f"Dia_str {dia_str}")
        print(f"numero_dia {numero_dia}")
        print(f"[DEBUG] numero_dia: {numero_dia} (tipo: {type(numero_dia)})")
        print(f"[DEBUG] dia: {dia} (tipo: {type(dia)})")


        if numero_dia == dia:
            temp_min = dia_pesquisado.find_element(By.CLASS_NAME, "tempMin").text
            temp_max = dia_pesquisado.find_element(By.CLASS_NAME, "tempMax").text
            descricao_tempo = dia_pesquisado.find_element(By.CLASS_NAME, "weatherImg").get_attribute("title")
            driver.quit()
            return {
                "dia": dia_str,
                "temperatura_minima": temp_min,
                "temperatura_maxima": temp_max,
                "descricao_tempo": descricao_tempo
            }
    driver.quit()
    return {"Erro": f"O dia {dia} não foi encontrado na previsão semanal."}
    
# Função para pesquisar previsão do tempo por localidade
@api.get("/{distrito}/{cidade}")
def pesquisa_por_localidade(request, distrito: str, cidade: str):
    import time

    driver = webdriver.Chrome()  

    distrito = distrito.capitalize()
    cidade = cidade.capitalize()
    # Como o site faz a procura nos filtros https://www.ipma.pt/pt/otempo/prev.localidade.hora/#Aveiro&Aveiro
    driver.get(f"https://www.ipma.pt/pt/otempo/prev.localidade.hora/#{distrito}&{cidade}")  # Abre a página para a localidade

    # esperamos 3 segundos para garantir que a página carregue completamente
    time.sleep(3)
    
    # Pegar a weekly 
    element = driver.find_element(By.ID, "weekly").text


    print(type(element))  # Verifica o tipo do elemento capturado

    # tranformar em uma lista
    element_lista = list(element)
    print("Tipo do elemento capturado:", type(element_lista))
  
    driver.quit()  # Fecha o navegador
    return {"previsao_semanal": element}  # Retorna os dados da previsão

# Configuração das rotas no Django
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]

