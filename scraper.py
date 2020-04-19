#import bibliotek
import requests
from bs4 import BeautifulSoup
import pprint
import json

#funkcja do ekstrakcji składowych opinii
def extract_feature(opinion,selector,attribute=None):
    try:
        if attribute:
            return opinion.select(selector).pop()[attribute].strip()
        else:
            return opinion.select(selector).pop().text.strip()
    except IndexError:
        return None

#słownik z atrybutami opinii i ich selektorami
selectors = {
    "author":["div.reviewer-name-line"],
    "recommendation":["div.product-reviewer-sumary > em"],
    "stars":["span.review-score-count"],
    "content":None,
    "cons":None,
    "pros":None,
    "useful":None,
    "useless":None,
    "opinion_date":None,
    "purchase_date":None
}

#adres url pierwszej strony z opiniami o produkcie
url_prefix = "https://www.ceneo.pl/"
product_id = input("Podaj identyfikator produktu: ")
url_postfix = "#tab=reviews"
url = url_prefix+product_id+url_postfix

#pusta lista na opinie konsumentów 
all_opinions = []

while url:
    #pobranie kodu pojedynczej strony z opiniami o produkcie
    respons = requests.get(url)
    page_dom = BeautifulSoup(respons.text, 'html.parser')

    #wydobycie z kodu strony fragmentów odpowiadających opiom konsumentów
    opinions = page_dom.select("li.js_product-review")

    #dla wszystkich opinii z danej strony wydobycie ich składowych
    for opinion in opinions:
        features = {key:extract_feature(opinion, *args)
            for key, args in selectors.items()}
        features["opinion_id"] = int(opinion["date-entry-id"])
        features["useful"] = int(features["useful"])
        features["useless"] = int(features["useless"])
        features["stars"] = float(features["stars"].split("/")[0].replace(",","."))
        all_opinions.append(features)
        
    try:
        url = url_prefix+page_dom.select("a.pagination__next").pop()["href"]
    except IndexError:
        url = None
    print(len(all_opinions))
    print(url)

with open('opinions.json', 'w', encoding="UTF-8") as fp:
    json.dump(all_opinions, fp, indent=4, ensure_ascii=False)

# pprint.pprint(all_opinions)