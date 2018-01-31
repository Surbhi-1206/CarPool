from carpool.rides.RideDto import RideDto
from carpool.rides.RideService import RideService


def findRides(pickup, drop):
    """

    :param pickup:
    :param drop:
    :return a list of available drivers:
    """

    available_drivers = [] #for storing the list of available drivers
    ride_dto = RideDto()
    ride_service = RideService()
    rides = ride_service.load_rides(ride_dto)

    for ride in rides:
        start = ride.start
        end = ride.end
        if contains_location(pickup, drop, start, end):
            available_drivers.append(ride)

    return available_drivers

def contains_location(pickup, drop, start, end):
    """
    :param pickup:
    :param drop:
    :param start:
    :param end:
    :return true or false:

    """

    print("If pickup and drop locations lie in driver's route return true else return false")