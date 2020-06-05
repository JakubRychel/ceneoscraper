# CeneoScrapper
## Etap 1 - Analiza struktury opinii w serwisie [Ceneo](https://ceneo.pl)
|Składowa             |Selektor                                            |Nazwa zmiennej|
|---------------------|----------------------------------------------------|--------------|
|Opinia               |`div.js-product-review`                              |`opinion`
|Identyfikator opinii |`["data-entry-id"]`                                 |`opinion_id`
|Autor                |`span.user-post__author-name`                       |`author`
|Rekomendacja         |`span.user-post__author-recomendation > em`         |`recommendation`
|Ocena                |`span.user-post__score-count`                       |`stars`
|Treść opinii         |`div.user-post__text`                               |`content`
|Lista wad            |`div.review-feature__title--negatives ~ div`        |`cons`
|Lista zalet          |`div.review-feature__title--positives ~ div`        |`pros`
|Przydatna            |`button.vote-yes > span`                            |`useful`
|Nieprzydatna         |`button.vote-no > span`                             |`useless`
|Data wystawienia     |`span.review-time > time:first-child["datetime"]`   |`opinion_date`
|Data zakupu          |`span.review-time > time:nth-child(2)["datetime"]`  |`purchase_date`
## Etap 2 - Pobranie składowych pojedynczej opinii
- Pobranie kodu jednej strony z opiniami o konkretnym produkcie
- Wyciągnięcie z kodu strony fragmentów odpowiadających poszczególym opiniom
- Zapisanie do pojedynczych zmiennych wartości poszczególnych składowych opinii
## Etap 3 - Pobranie wszystkich opinii o pojedynczym produkcie
- Zapisanie do złożonej struktury danych składowych wszystkich opinii z pojedynczej strony
- Przechodzenie po kolejnych stronach z opiniami
- Zapis wszystkich opinii o pojedynczym produkcie do pliku
## Etap 4
- Transformacja i wyczyszczenie danych
- Refaktoring kodu
- Parametryzacja
## Etap 5
- Wczytanie opinii do ramki danych
- Policzenie podstawowych statystyk
- Narysowanie wykresów funkcji
## Etap 6 - Interfejs webowy dla scrapera (Flask)
>   /CeneoScraper/
>>      /run.py
>>      /config.py
>>      /app
>>>         /__init__.py
>>>         /views.py
>>>         /models.py
>>>         /static/
>>>>            /main.css
>>>>            /figures_png/
>>>         /templates/
>>>>            /layout.html
>>>>            /extract.html
>>>         /opinions_json/
>>      /requirements.txt
>>      /.venv