from carpool.booking.BookingRepository import BookingRepository


class BookingService:
    booking_repository = BookingRepository()

    def create_booking(self, booking_dto):
        """
        creates a new booking
        :param booking_dto:
        """
        # booking_repository = BookingRepository()
        self.booking_repository.create_booking(booking_dto)

    def load_bookings(self, booking_dto):
        """
        fetch existing bookings requests from a rider for a given path
        :param booking_dto:
        :return bookings:
        """
        # booking_repository = BookingRepository()
        bookings = self.booking_repository.get_booking(booking_dto)
        return bookings

    def update_bookings(self, booking_dto):
        """
        update the booking status
        """

        # booking_repository = BookingRepository()
        self.booking_repository.update_booking(booking_dto)

    def get_confirmed_booking_id(self, booking_dto):

        ride_id = self.booking_repository.get_confirmed_bookings_id(booking_dto)
        return ride_id