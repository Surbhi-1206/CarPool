from flask import Blueprint, render_template

h = Blueprint('home', __name__, url_prefix='/home')


@h.route('/')
def welcome():
    return render_template('home/home.html')
