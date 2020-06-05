#import bibliotek
from flask import Flask

#utworzenie instancji klasu Flask reprezentującego aplikację webową
app=Flask(__name__)

#import routingów
from app import views

#uruchomienie aplikacji

if __name__ == "__main__":
    app.run(debug=True)