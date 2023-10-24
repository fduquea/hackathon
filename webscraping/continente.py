import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time

# URL da página
url_continente = "https://www.continente.pt/"
options = Options()
options.add_argument("--headless")
# Continente
def get_continente_data(products_id):
    # connection to the page
    chrome = webdriver.Chrome(options=options)
    chrome.get(url_continente)

    time.sleep(1)
    cookies = chrome.find_element(By.XPATH, "//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']")
    time.sleep(1)
    cookies.click()
    time.sleep(1)
    area_de_entrega = chrome.find_element(By.XPATH, "//span[@class='delivery-location']")
    time.sleep(1)
    area_de_entrega.click()
    time.sleep(1)
    codigo_postal = chrome.find_element(By.XPATH, "//input[@id='coverage-postal-code']")
    time.sleep(1)
    codigo_postal.send_keys("porto")
    time.sleep(1)
    codigo_postal.send_keys(Keys.ENTER)
    time.sleep(1)
    confirm_codigo_postal = chrome.find_element(By.XPATH, "//input[@type='radio' and @name='customerAddress']")
    time.sleep(1)
    confirm_codigo_postal.click()
    time.sleep(1)
    last_confirm = chrome.find_element(By.XPATH, "//button[@class='button button--primary confirm-coverage-area-select']")
    time.sleep(1)
    last_confirm.click()
    time.sleep(5)
    for key, value in products_id.items():

        chrome.get(url_continente + "pesquisa/?q=" + value)
        # find the link to the product page
        link_element = chrome.find_element(By.CSS_SELECTOR, "a[href^='https://www.continente.pt/produto/']")
        # check if there is content
        if link_element:
            # get the link
            link = link_element.get_attribute("href")
            # check if the link was found
            if (link):
                # connection to the product page
                chrome.get(link)
                # parse the HTML of the page
                soup = BeautifulSoup(chrome.page_source, "html.parser")
                # find the price
                price = soup.find("span", class_="ct-price-formatted")
                price_string = price.text.strip()
                
                # split the price string into the value and currency symbol
                currency_symbol = price_string[0]
                price_value = price_string[1:]

                # concatenate the value and symbol in the desired order
                new_price_string = f"{price_value} {currency_symbol}"
                # find the span tag that contains the unit information
                capacity_span = soup.find("span", class_="ct-pdp--unit col-pdp--unit")
                # extract the unit value from the text of the span tag
                unit = capacity_span.text.strip()
                # extract the capacity value from the text of the span tag
                capacity = unit.split()[1] + " " + unit.split()[2]
                # Get the current date and time
                now = datetime.now()
                #Format the date and time as a string
                date_string = now.strftime("%d/%m/%Y %H:%M:%S")
                # print the results
                print(f"Store name: Continente")
                print(f"Wine name: {key}")
                print(f"Harvest year: N/A")
                print(f"Capacity: {capacity}")
                print(f"Discount: TODO")
                print(f"Price and currency: {new_price_string}")
                print(f"Date of scraping: {date_string}, WEST timezone")
                print(f"Location: Portugal // TODO")
                print(f"Product link: {link}\n")
            else:
                print("Não foi possível acessar a página do artigo.\n")
        else:
            print("Não foi possível acessar a página do artigo.\n")