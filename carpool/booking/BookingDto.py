class IllegalArgumentsException(Exception):

    def __init__(self, *args, **kwargs):
        super(IllegalArgumentsException, self).__init__(self, *args, **kwargs)


# ride data transfer object
class BookingDto:

    def __init__(self, booking_code="", owner="", pickup="", drop="", rider="", ride_id="", status="pending"):
        # if not (booking_code):
        #    raise IllegalArgumentsException('booking_code required')
        self.booking_code = booking_code
        self.rider = rider
        self.pickup = pickup
        self.drop = drop
        self.owner = owner
        self.ride_id = ride_id
        self.status = status
