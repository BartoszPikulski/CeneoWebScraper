import requests
import bs4

class Product:
    def __init__(self, product_id, product_name = None, opinions = []):
        self.product_id = product_id
        self.product_name = product_name
        self.opinions = opinions

    def extract_product(self):
        next_page = "https://www.ceneo.pl/{}#tab=reviews".format(self.product_id)

        while next_page:
            respons = requests.get(next_page)
            page_dom = BeautifulSoup(respons.text, "html.parser")
            opinions = page_dom.select("div.js_product-review")
            for opinion in opinions:
                self.opinions.append(Opinion().extract_opinion(opinion))
        
            try:
                next_page = "https://www.ceneo.pl" + \
                page_dom.select("a.pagination__next").pop()["href"]
            except IndexError:
                next_page = None
            print(next_page)



