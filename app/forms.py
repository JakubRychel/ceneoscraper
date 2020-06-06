from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class ProductForm(FlaskForm):
    product_id = StringField(
        "Podaj kod produktu z serwisu Ceneo.pl: ",
        validators=[
            DataRequired("Musisz podać kod produktu!"),
            Length(min=8, max=8, message="Kod produktu musi mieć dokładnie 8 znaków!"),
            Regexp("^[\d]+$", message="Kod produktu może zawierać wyłącznie cyfry!")
        ]
    )
    submit = SubmitField("Pobierz")