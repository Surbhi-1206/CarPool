from carpool import models, db


class BookingRepository:

    def create_booking(self, booking_dto):
        """
        creates a new booking in db
        :param booking_dto:
        """
        booking = models.Bookings(booking_dto.rider, booking_dto.owner, booking_dto.ride_id, booking_dto.pickup,
                                  booking_dto.drop, booking_dto.status, booking_dto.booking_code)
        db.session.add(booking)
        db.session.commit()

    def get_bookings_by_path(self, booking_dto):
        """
        fetches existing booking requests from db
        :param booking__dto:
        :return bookings:
        """
        bookings = models.Bookings.query.filter_by(rider=booking_dto.rider, pickup=booking_dto.pickup,
                                                   drop=booking_dto.drop, status=booking_dto.status).all()
        return bookings

    def get_booking_by_code(self, booking_dto):
        booking = models.Bookings.query.filter_by(booking_code=booking_dto.booking_code).first()
        return booking

    def cancel_bookings(self, booking_dto):
        """
        update booking status to cancelled
        :param booking_dto:
        """
        booking = models.Bookings.query.filter_by(booking_code=booking_dto.booking_code).update(
            dict(status=booking_dto.status))
        db.session.commit()

    def confirm_booking(self, booking_dto):
        """
        update booking request to confirm
        :param booking_dto:
        """
        booking = models.Bookings.query.filter_by(booking_code=booking_dto.booking_code).update(
            dict(status=booking_dto.status))
        db.session.commit()
