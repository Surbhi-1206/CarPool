from flask_wtf import Form
from wtforms import StringField  , SubmitField
from wtforms import validators , ValidationError

class BookingForm(Form):
    email = StringField("Email", [validators.DataRequired("Please enter your email"),
                                  validators.Email("Please enter a valid email address")])
    submit = SubmitField("Accept")
