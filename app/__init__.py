#import bibliotek
from flask import Flask

#utworzenie instancji(obiektu) klasy Flask reprezentującego aplikację webową
app = Flask(__name__)

#import routing'ów 
from app import views

#uruchomienie aplikacji
if __name__ == "__main__":
    app.run(debug=True)