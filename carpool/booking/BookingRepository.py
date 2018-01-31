from carpool import models, db


class BookingRepository:

    def create_booking(self, booking_dto):
        """
        creates a new booking in db
        :param booking_dto:
        """
        booking = models.Bookings(booking_dto.rider, booking_dto.owner, booking_dto.ride_id, booking_dto.pickup,
                                  booking_dto.drop, booking_dto.status)
        db.session.add(booking)
        db.session.commit()

    def get_booking(self, booking_dto):
        """
        fetches existing booking requests from db
        :param booking__dto:
        :return bookings:
        """
        bookings = models.Bookings.query.filter_by(rider=booking_dto.rider, pickup=booking_dto.pickup,
                                                   drop=booking_dto.drop).all()
        return bookings

    def update_booking(self, booking_dto):
        """
        :param booking_dto:
        updates the booking status
        """

        booking = models.Bookings.query.filter_by(rider=booking_dto.rider, owner=booking_dto.owner,
                                                  pickup=booking_dto.pickup,
                                                  drop=booking_dto.drop).update(dict(status=booking_dto.status))
        db.session.commit()

    def get_confirmed_bookings_id(self, booking_dto):
        """

        :param booking_dto:
        :return:
        """

        #print(booking_dto.rider)
        #print(booking_dto.pickup)
        #print(booking_dto.drop)
        #print(booking_dto.owner)
        #print(booking_dto.status)
        booking = models.Bookings.query.filter_by(rider=booking_dto.rider, pickup=booking_dto.pickup,
                                                  drop=booking_dto.drop, owner=booking_dto.owner,
                                                  status=booking_dto.status).first()
        if booking:
            #print("found it")
            #print(booking.ride_id)
            return booking.ride_id
