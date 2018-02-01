from carpool import models, db


class RidesRepository:

    def create_ride(self, ride_dto):
        """
        creates a new ride in db
        :param ride_dto:
        """
        ride = models.Rides(ride_dto.email, ride_dto.start, ride_dto.end, ride_dto.car_num, ride_dto.seats,
                            ride_dto.user_id)
        db.session.add(ride)
        db.session.commit()

    def get_ride(self, ride_dto):
        """
        fetches existing rides for a given path from db
        :param ride_dto:
        :return rides:
        """
        rides = models.Rides.query.filter_by(start=ride_dto.start, end=ride_dto.end).all()
        return rides

    def get_ride_details(self, ride_id):
        """

        :param ride_id:
        :return:
        """
        ride = models.Rides.query.filter_by(id=ride_id).first()
        ride_details = {}
        ride_details['car_num'] = ride.car_num
        ride_details['pickup'] = ride.start
        ride_details['drop'] = ride.end
        return ride_details
