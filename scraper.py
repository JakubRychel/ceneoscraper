# Import bibliotek
import requests
from bs4 import BeautifulSoup
import pprint
import json
import re

# funkcja do ekstrakcji składowych opinii


def extract_feature(opinion, selector, attribute=None):
    try:
        if attribute:
            return opinion.select(selector).pop(0)[attribute].strip()
        elif "review-feature__title" in selector:
            return opinion.select(selector)
        else:
            return opinion.select(selector).pop(0).text.strip()
    except IndexError:
        return None

def replace_formatting(element, flag=False):
    try:
        if flag:
            if not element:
                return None
            else:
                return ", ".join([x.text for x in element])
        else:
            return element.replace("\n", " ").replace("\r", " ")
    except AttributeError:
        return element

# słownik z selektorami
selectors = {
    "author": ["span.user-post__author-name"], # naprawione
    "recommendation": ["span.user-post__author-recomendation > em"],
    "stars": ["span.user-post__score-count"],
    "content": ["div.user-post__text"], # naprawione
    "cons": ["div.review-feature__title--negatives ~ div"], # naprawione
    "pros": ["div.review-feature__title--positives ~ div"], # naprawione
    "useful": ["button.vote-yes > span"],
    "useless": ["button.vote-no > span"],
    "opinion_date": ["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchase_date": ["span.user-post__published > time:nth-child(2)", "datetime"]
}

# Adres URL pierwszej strony z opiniami o produkcie
url_prefix = "https://www.ceneo.pl"
product_id = input("Podaj identyfikator produktu: ")
url_postfix = "#tab=reviews"
url = url_prefix + "/" + product_id + url_postfix

# Pusta lisa na opinie konsumentów
all_opinions = []

while url:

    # Pobranie kodu pojedynczej strony z opiniami o produkcie
    response = requests.get(url)
    page_dom = BeautifulSoup(response.text, "html.parser")

    # Wyciągnięcie z kodu strony fragmentów odpowiadających poszczególym opiniom
    opinions = page_dom.select("div.js_product-review") #bierze też komentarze, nie wiadomo czemu

    # Dla wszystkich opinii z danej strony wydobycie ich składowych
    
    for opinion in opinions:
        features = {key: extract_feature(opinion, *args)
                    for key, args in selectors.items()}
        features["opinion_id"] = int(opinion["data-entry-id"])
        features["useful"] = int(features["useful"])
        features["useless"] = int(features["useless"])
        features["stars"] = float(features["stars"].split("/")[0].replace(",", "."))
        features["content"] = replace_formatting(features["content"])
        features["pros"] = replace_formatting(features["pros"], True)
        features["cons"] = replace_formatting(features["cons"],True)
        all_opinions.append(features)
    try:
        url = url_prefix + page_dom.select("a.pagination__next").pop()["href"]
    except IndexError:
        url = None
    print(len(all_opinions))
    print(url)
with open("opinions_json/"+product_id+".json", "w", encoding="UTF-8") as fp:
    json.dump(all_opinions, fp, indent=4, ensure_ascii=False)

# pprint.pprint(all_opinions)
