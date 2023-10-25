import requests
from bs4 import BeautifulSoup
from datetime import datetime
from fake_useragent import UserAgent

# URL da página
url_elcorteingles = "https://www.elcorteingles.pt/supermercado/"

# EL CORTE INGLÉS
def get_elcorteingles_data(products_id):
    for key, value in products_id.items():
        # connection to the page
        headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
        response = requests.get(url_elcorteingles + "pesquisar/?term=" + value, headers=headers ,allow_redirects=True)
        # check if the request was successful
        if response.status_code == 200:
            # parse the HTML of the page
            soup = BeautifulSoup(response.text, "html.parser")
            # find the link to the product page
            link_element = soup.find("a", href=lambda href: href and href.startswith("/supermercado/010"))
            # check if there is content
            if link_element:
                # get the link
                link = link_element.get("href")
                # check if the link was found
                if (link):
                    real_link = "https://www.elcorteingles.pt" + link
                    # connection to the product page
                    response = requests.get(real_link, headers=headers ,allow_redirects=True)

                    # check if the request was successful
                    if (response.status_code == 200):
                        soup = BeautifulSoup(response.text, "html.parser")

                        # find the capacity
                        p_tags = soup.find_all("p")

                        # loop through the p tags
                        for p_tag in p_tags:
                            # check if the p tag contains the text "garrafa"
                            if "garrafa" in p_tag.text:
                                # extract the capacity value from the p tag text
                                capacity = p_tag.text.split("\n")[2].strip()


                        # find if there is discount
                        if '<g><circle fill="#E21E04" cx="128" cy="128" r="128"></circle></g>' in response.text:
                            discount_bool = 1
                        else:
                            discount_bool = 0

                        # find the price
                        if discount_bool == 0:
                            # find the div tag that contains the price
                            price_div = soup.find("div", {"data-synth": "LOCATOR_PRECIO"})
                            # extract the price from the text of the div tag
                            price = price_div.text.strip().replace(",", ".")
                        else:
                            # find the div tag that contains the price
                            price_div = soup.find('div', {'class': 'prices-price _offer'})

                            # extract the price from the text of the div tag
                            price = price_div.text.strip().replace(',', '.')
                            discount_div = soup.find('div', {'class': 'prices-price _before'})
                            before_price = discount_div.text.strip().replace(',', '.')
                            discount = (float(before_price) - float(price)) / float(before_price) * 100
                        # Get the current date and time
                        now = datetime.now()
                        #Format the date and time as a string
                        date_string = now.strftime("%d/%m/%Y %H:%M:%S")
#
                        # print the results
                        print(f"Store name: El Corte Inglés")
                        print(f"Wine name: {key}")
                        print(f"Harvest year: N/A")
                        print(f"Capacity: {capacity} cl")
                        if discount_bool == 1:
                            print(f"Discount: Yes, {discount}%")
                        else:
                            print(f"Discount: No")
                        print(f"Price and currency: {price}")
                        print(f"Date of scraping: {date_string}, WEST timezone")
                        print(f"Location: Online store. Nationwide delivery.")
                        print(f"Product link: {real_link}\n")
#
                    else:
                        print("Não foi possível acessar a página do artigo.\n")
                else:
                    print("Não foi possível acessar a página do artigo.\n")
            else:
                print("Não foi possível acessar a página do artigo.\n")
        else:
            print("Não foi possível acessar a página do artigo.\n")
#        return ("El Corte Inglés", {key}, "N/A", "{capacity} cl", "Yes, {discount}%", "{price}", "{date_string}, WEST timezone", "Online store. Nationwide delivery.", "{real_link}")