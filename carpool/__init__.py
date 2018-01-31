from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager , login_required  , logout_user ,LoginManager,login_user , current_user , LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from carpool.home.views import h as home_module
from carpool.auth.views import a as auth_module
from carpool.rides.views import r as ride_module
from carpool.booking.views import b as booking_module

app.register_blueprint(home_module)
app.register_blueprint(auth_module)
app.register_blueprint(ride_module)
app.register_blueprint(booking_module)

db.create_all()