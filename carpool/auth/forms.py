from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField, FloatField, PasswordField
from wtforms import validators, ValidationError


class SignUpForm(Form):
    name = StringField("Username", [validators.DataRequired("Please enter your name")])
    email = StringField("Email", [validators.DataRequired("Please enter your email"),
                                  validators.Email("Please enter a valid email address")])
    contact = StringField("Contact Number", [validators.DataRequired("Please enter your contact number")])
    password = PasswordField("Password", [validators.DataRequired("Please enter the password")])
    submit = SubmitField("Sign Up")


class SignInForm(Form):
    email = StringField("Email", [validators.DataRequired("Please enter your email"),
                                  validators.Email("Please enter a valid email id")])
    password = PasswordField("Password", [validators.DataRequired("Please enter the password")])
    submit = SubmitField("Login")
