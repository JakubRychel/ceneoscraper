# CeneoScraper11N
## Etap 1 - analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)
|Składowa                |Selektor                                                           |Nazwa zmiennej|
|------------------------|-------------------------------------------------------------------|--------------|
|opinia                  |div.js_product-review                                              |opinion       |
|identyfikator opinii    |["data-entry-id"]                                                  |opinion_id    |
|autor                   |span.user-post__author-name                                        |author        |
|rekomendacja            |span.user-post__author-recomendation > em                          |recommendation|
|ocena                   |span.user-post__score-count                                        |stars         |
|treść opinii            |div.user-post__text                                                |content       |
|lista wad               |div.review-feature__col:has(> div.review-feature__title--negatives)|cons          |
|lista zalet             |div.review-feature__col:has(> div.review-feature__title--positives)|pros          |
|przydatna               |button.vote-yes > span                                             |useful        |
|nieprzydatna            |button.vote-no > span                                              |useless       |
|data wystawienia opinii |span.user-post__published > time:first-child["datetime"]           |opinion_date  |
|data zakupu             |span.user-post__published > time:nth-child(2)["datetime"]          |purchase_date |

## Etap 2 - pobranie składowych pojedynczej opinii
- pobranie kodu jednej strony z opiniani o konkretnym produkcie
- wyciągnięcie z kodu strony fragmentów odpowiadających poszczególnym opiniom
- zapisanie do pojedynczych zmienych wartości poszczególnych składowych opinii
## Etap 3 - pobranie wszystkich opinii o pojedynczym produkcie
- zapisanie do złożonej struktury danych składowych wszystkich opinii z pojedynczej strony
- przechodzenie po kolejnych stronach z opiniami 
- zapis wszystkich opinii o pojedynczym produkcie do pliku
## Etap 4
- transformacja i wyczyszczenie danych
- refaktoring kodu
- parametryzacja 
## Etap 5 (Pandas, Matplotlib)
- wczytanie opinii do ramki danych
- policzenie podstawowych statystyk
- narysowanie wykresów funkcji
## Etap 6 interfejs webowy dla scrapera (Flask)
>    /CeneoScraper11N  
>>        /run.py  
>>        /config.py  
>>        /app  
>>>            /__init__.py
>>>            /views.py  
>>>            /models.py
>>>            /forms.py
>>>            /scraper.py
>>>            /analizer.py  
>>>            /static/  
>>>>                /main.css
>>>>                /figures_png
>>>            /templates/  
>>>>                /layout.html  
>>>>                /extract.html
>>>>                /about.html
>>>            /opinions_json
>>>        /requirements.txt  
>>>        /.venv