#import aplikacji
from app import app
from flask import render_template, redirect, url_for
from flaskext.markdown import Markdown
from app.forms import ProductForm
from app.scraper import scraper
import pandas as pd
import os

Markdown(app, extensions=['tables'])

app.config['SECRET_KEY'] = "ToJestBrdzoTajnyKLucz"

#routing dla strony głównej
@app.route('/')
@app.route('/index')
def index():
    return render_template("main.html")

@app.route('/about')
def about():
    with open("README.md", "r", encoding="UTF-8") as fp:
        text = fp.read()
    return render_template("about.html", text=text)

@app.route('/extract', methods=['GET', 'POST'])
def extract():
    form = ProductForm()
    if form.validate_on_submit():
        product_id = form.product_id.data
        scraper(product_id)
        return redirect(url_for('product', id=product_id))
    return render_template("extract.html", form=form)

@app.route('/product/<id>')
def product(id):
    input_directory = "app/opinions_json"
    opinions = pd.read_json(input_directory+"/"+id+".json")
    return render_template(
        "product.html", 
        tables=[
            opinions.to_html(
                classes="table table-hover table-responsive",
                table_id = "opinions",
                index = False
            )
        ]
    )

@app.route('/products')
def products():
    input_directory = "app/opinions_json"
    products = [product.replace(".json","") for product in os.listdir(input_directory)]
    return render_template("products.html", products=products)