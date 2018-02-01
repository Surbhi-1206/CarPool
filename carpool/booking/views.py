from flask import Blueprint, request, render_template, flash, g, redirect, url_for
from carpool import app
from carpool.booking.BookingService import BookingService
from carpool.booking.BookingDto import BookingDto
from carpool.notification.NotifyService import NotifyService
from carpool.auth.UserDto import UserDto
from carpool.auth.AuthService import AuthService

b = Blueprint('booking', __name__, url_prefix='/bookings')


@b.route('/confirm_booking/<booking_code>')
def confirm_booking(booking_code):
    booking_service = BookingService()
    booking_dto = BookingDto(booking_code)
    booking = booking_service.load_booking_by_code(booking_dto)
    if booking.status == "cancelled":
        flash("Sorry! this trip has already been confirmed")
        return redirect(url_for('home.welcome'))
    booking_dto.status = "confirm"
    booking_service.confirm_booking(booking_dto)
    rider = booking.rider
    pickup = booking.pickup
    drop = booking.drop
    cancel_bookings(rider, pickup, drop, "pending")
    confirmed_ride_id = booking.ride_id
    owner = booking.owner
    notify_service = NotifyService()
    notify_service.send_notification_to_rider(rider, owner, confirmed_ride_id)
    return redirect((url_for('booking.success', booking_code=booking_code)))


def cancel_bookings(rider, pickup, drop, status):
    booking_service = BookingService()
    booking_dto = BookingDto(booking_code="", rider=rider, pickup=pickup, drop=drop, status=status)
    bookings = booking_service.load_bookings_by_path(booking_dto)
    for booking in bookings:
        booking_dto = BookingDto(booking_code=booking.booking_code, status="cancelled")
        booking_service.cancel_bookings(booking_dto)


@b.route('/success/<booking_code>')
def success(booking_code):
    booking_service = BookingService()
    booking_dto = BookingDto(booking_code=booking_code)
    booking = booking_service.load_booking_by_code(booking_dto)
    user_dto = UserDto(booking.rider)
    auth_service = AuthService()
    user = auth_service.load_user(user_dto)
    name = user.name
    contact = user.contact
    return render_template('booking/success.html', name=name, contact=contact, title="Success")
