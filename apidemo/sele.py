def pegardados():
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    driver.get("https://www.ipma.pt/pt/otempo/prev.localidade.hora/")

    weekly_div = driver.find_element(By.ID, "weekly")
    print(weekly_div.text)  # Se tiver conteúdo, ele deve aparecer aqui

    driver.quit()
    return "Dados obtidos com sucesso!"

# chamando a função para testar
if __name__ == "__main__":
    resultado = pegardados()
    print(resultado)


def buscar_localidade(localidade):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    driver = webdriver.Chrome()
    url = f"https://www.ipma.pt/pt/otempo/prev.localidade.hora/#{localidade}&{localidade}"
    driver.get(url)

    # Espera até que a div 'weekly' esteja presente
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "weekly")))
    
    weekly_div = driver.find_element(By.ID, "weekly")
    print(weekly_div.text)  # Se tiver conteúdo, ele deve aparecer aqui

    driver.quit()
    return "Dados obtidos com sucesso! Pela localidade: " + localidade

if __name__ == "__main__":
    localidade = "aveiro"  # Exemplo de localidade
    resultado = buscar_localidade(localidade)
    print(resultado)
