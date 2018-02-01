from carpool.booking.BookingRepository import BookingRepository


class BookingService:
    booking_repository = BookingRepository()

    def create_booking(self, booking_dto):
        """
        creates a new booking
        :param booking_dto:
        """
        self.booking_repository.create_booking(booking_dto)

    def load_bookings_by_path(self, booking_dto):
        """
        fetch existing bookings requests from a rider for a given path
        :param booking_dto:
        :return bookings:
        """
        bookings = self.booking_repository.get_bookings_by_path(booking_dto)
        return bookings

    def load_booking_by_code(self, booking_dto):
        """
        :param booking_dto:
        :return:
        """
        booking = self.booking_repository.get_booking_by_code(booking_dto)
        return booking

    def confirm_booking(self, booking_dto):
        """
        confirm booking request
        :param booking_dto:
        :return:
        """
        self.booking_repository.confirm_booking(booking_dto)

    def cancel_bookings(self, booking_dto):
        """
        cancel booking request
        """
        self.booking_repository.cancel_bookings(booking_dto)
