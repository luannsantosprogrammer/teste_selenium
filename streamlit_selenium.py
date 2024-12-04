import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search_google():
    # Configurar o WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Executar em modo invisível (opcional)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service  = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service,options=options)  # Substitua por webdriver.Firefox() se estiver usando Firefox
    driver.get("https://estoque.brisanet.net.br/#/estoque/itens/item/liste")

    # Encontrar o campo de pesquisa e realizar a busca
    # search_box = driver.find_element(By.NAME, "q")
    # search_box.send_keys(query)
    # search_box.send_keys(Keys.RETURN)

    # Esperar os resultados carregarem
    time.sleep(2)

    # Capturar os títulos dos resultados
    results = driver.title
    # titles = [result.text for result in results if result.text]

    # Fechar o WebDriver
    driver.quit()

    return results

# Interface Streamlit
st.title("Automatizar Pesquisa no Google")
query = st.text_input("Digite algo para pesquisar no Google:")

if st.button("Pesquisar"):
    with st.spinner("Realizando a pesquisa..."):
        try:
            results = search_google()
            if results:
                st.success("Resultados encontrados:")
                st.write(results)
            else:
                st.warning("Nenhum resultado encontrado.")
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
