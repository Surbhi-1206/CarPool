from flask_wtf import Form
from wtforms import StringField  , SubmitField , IntegerField , FloatField
from wtforms import validators , ValidationError

class Ride(Form):
    #email = StringField("Email",[validators.DataRequired("Please enter your email"),validators.Email("Please enter a valid email")])
    start = StringField("Start Location",[validators.DataRequired("Please enter a pickup location")])
    end = StringField("End Location" , [validators.DataRequired("Please enter a drop location")])
    car_num = StringField("Car Number", [validators.DataRequired("Please enter the car number")])
    seats = IntegerField("Number of seats available" , [validators.DataRequired("")])
    submit = SubmitField("Submit")

class SearchRide(Form):
    pickup = StringField("PickUp Location", [validators.DataRequired("Please enter a pickup location")])
    drop = StringField("Drop Location", [validators.DataRequired("Please enter a drop location")])
    submit = SubmitField("Search")