from carpool.rides.RideRepository import RidesRepository


class RideService:
    ride_repository = RidesRepository()

    def create_ride(self, ride_dto):
        """
        creates a new ride
        :param ride_dto:
        """
        self.ride_repository.create_ride(ride_dto)

    def load_rides(self, ride_dto):
        """
        fetch existing rides
        :param ride_dto:
        :return rides:
        """
        rides = self.ride_repository.get_ride(ride_dto)
        return rides

    def get_ride_details(self, ride_id):
        ride_details = self.ride_repository.get_ride_details(ride_id)
        return ride_details
