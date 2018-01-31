from flask import Blueprint, request, render_template, flash, g, redirect, url_for
from flask_login import login_manager, login_required, LoginManager, login_user, current_user
from carpool import app
from carpool import models
from carpool.booking.BookingService import BookingService
from carpool.booking.BookingDto import BookingDto
from .forms import BookingForm
from carpool.notification.NotifyService import  NotifyService
from carpool.auth.UserDto import UserDto
from carpool.auth.AuthService import AuthService

b = Blueprint('booking', __name__, url_prefix='/bookings')


@b.route('/confirm_booking/<sender>/<start>/<end>', methods=['GET', 'POST'])
def confirm_booking(sender, start, end):
    booking_service = BookingService()
    form = BookingForm()

    if request.method == 'GET':
        return render_template('booking/confirmbooking.html', form=form)

    elif request.method == 'POST':
        if form.validate_on_submit():
            owner = form.email.data
            booking_dto1 = BookingDto(pickup=start, drop=end, rider=sender)
            bookings = booking_service.load_bookings(booking_dto1)

            #This loop cancels all other booking requests for the given path and rider
            for booking in bookings:
                if booking.owner == owner and booking.status == "pending":
                    continue
                if booking.owner == owner and booking.status == "cancelled":
                    flash("Sorry! this trip has already been confirmed")
                    return redirect(url_for('home.welcome'))
                booking_dto2 = BookingDto(booking.owner, start, end, rider=sender, status="cancelled")
                booking_service.update_bookings(booking_dto2)
            booking_dto = BookingDto(owner, start, end, rider=sender, status="confirm")
            booking_service.update_bookings(booking_dto)
            confirmed_ride_id = booking_service.get_confirmed_booking_id(booking_dto)
            notify_service = NotifyService()
            notify_service.send_notification_to_rider(sender, owner, confirmed_ride_id)
            return redirect((url_for('booking.success', rider_info=sender)))
        return render_template('booking/confirmbooking.html', form=form)


@b.route('/success/<rider_info>')
def success(rider_info):
    user_dto = UserDto(rider_info)
    auth_service = AuthService()
    user = auth_service.load_user(user_dto)
    name = user.name
    contact = user.contact
    return render_template('booking/success.html', name=name, contact=contact, title="Success")
