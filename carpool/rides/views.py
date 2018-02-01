from flask import Blueprint, request, render_template, flash, g, redirect, url_for
from flask_login import login_manager, login_required, LoginManager, login_user, current_user
from carpool import app
from carpool import models
from .forms import Ride, SearchRide
from carpool.rides.RideDto import RideDto
from carpool.rides.RideService import RideService
from carpool.auth.UserDto import UserDto
from carpool.auth.AuthService import AuthService, InvalidUserException
from carpool.notification.NotifyService import NotifyService
from carpool.booking.BookingService import BookingService
from carpool.booking.BookingDto import BookingDto
from random import randint

r = Blueprint('rides', __name__, url_prefix='/rides')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.signin'


@login_manager.user_loader
def load_user(email):
    return models.Users.query.filter_by(email=email).first()


@app.before_request
def before_request():
    g.user = current_user


@r.route('/registeride', methods=['GET', 'POST'])
@login_required
def registerRide():
    """
    registers a new ride
    """
    ride_service = RideService()
    auth_service = AuthService()
    form = Ride()

    if request.method == 'GET':
        return render_template('rides/register.html', title='Register Ride', form=form)

    elif request.method == 'POST':
        if form.validate_on_submit():
            email = g.user.get_id()
            user_dto = UserDto(email)
            try:
                user = auth_service.load_user(user_dto)
                ride_dto = RideDto(form.start.data, form.end.data, form.car_num.data, user.id, form.seats.data, email)
                ride_service.create_ride(ride_dto)
                flash("Ride successfully registered!")
                return redirect(url_for('home.welcome'))
            except InvalidUserException:
                flash("Invalid User")
                return redirect(url_for('rides.registerRide'))
        flash('Service registration failed')
        return render_template('rides/register.html', title='Register Ride', form=form)


@r.route('/searchride', methods=['GET', 'POST'])
@login_required
def searchRide():
    """
    search for rides
    """

    form = SearchRide()
    if request.method == 'GET':
        return render_template('rides/search.html', title='Search Ride', form=form)

    elif request.method == 'POST':
        if form.validate_on_submit():
            pickup = form.pickup.data
            drop = form.drop.data
            return redirect(url_for('rides.bookRide', start=pickup, end=drop))
        return render_template('rides/search.html', title='Search Ride', form=form)


@r.route('/bookride/<start>/<end>', methods=['GET', 'POST'])
def bookRide(start, end):
    """
    send booking notification to drivers
    :param start location:
    :param end location:

    """
    ride_service = RideService()
    booking_service = BookingService()
    notify_service = NotifyService()
    ride_dto = RideDto(start, end)

    # rides = findRides(start, end)
    available_rides = ride_service.load_rides(ride_dto)

    if request.method == 'GET':
        if available_rides:
            count_available_rides = 0
            for ride in available_rides:
                count_available_rides += 1
            return render_template('rides/showrides.html', pickup=start, drop=end, ride_count=count_available_rides)
        flash('No rides available for the entered locations')
        return redirect(url_for('rides.searchRide'))


    elif request.method == 'POST':
        print('request method is post')
        rider_email = g.user.get_id()
        for ride in available_rides:
            owner_email = ride.email
            print(ride.email)
            random_int = randint(100, 999)
            booking_code = "b" + str(random_int)
            booking_dto = BookingDto(booking_code, ride.email, ride.start, ride.end, rider_email, ride.id)
            booking_service.create_booking(booking_dto)
            notify_service.send_notification_to_owners(booking_code, owner_email)
        flash('Booking Request has been sent to drivers. Check your email for booking confirmation and driver details')
        return redirect(url_for('home.welcome'))
