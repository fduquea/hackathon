import requests, continente, elcorteingles
from bs4 import BeautifulSoup
from datetime import datetime
from fake_useragent import UserAgent
import mysql.connector

db_connection = mysql.connector.connect(host='35.234.124.11', database='wines', user='root', password='root')

# URL da página do artigo
url_continente = "https://www.continente.pt/"
url_elcorteingles = "https://www.elcorteingles.pt/supermercado/"

products_id = {
    "Mateus Rosé Original": "5601012011500",
    "Mateus Sparkling": "5601012001310",
    "Trinca Bolotas Tinto": "5601012004427",
    "Papa Figos Branco": "5601012011920"
}

# Continente
continente.get_continente_data(products_id)

# EL CORTE INGLÉS
elcorteingles.get_elcorteingles_data(products_id)

