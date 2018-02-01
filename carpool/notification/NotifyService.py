import requests
import json
from carpool.auth.AuthService import AuthService
from carpool.auth.UserDto import UserDto
from carpool.rides.RideService import RideService


class NotifyService:

    def send_notification_to_rider(self, rider, owner, ride_id):
        """
        send driver details to rider
        :param rider:
        :param owner:
        :param ride_id:
        """
        email = []
        email.append(str(rider))
        auth_service = AuthService()
        ride_service = RideService()
        user_dto = UserDto(owner)
        user = auth_service.load_user(user_dto)
        owner_name = user.name
        owner_contact = user.contact
        ride_details = ride_service.get_ride_details(ride_id)
        message = "Your booking request from " + ride_details['pickup'] + " to " + ride_details[
            'drop'] + " has been confirmed."
        car_info = "\n Car Details:-" + "\n Driver Name: " + owner_name + "\n Contact: " + owner_contact + "\n Car Number: " + \
                   ride_details['car_num']

        url = "http://api.treebohotels.com/v1/notification/email/"
        data_values = {

            "data": {
                "subject": "CarPool Booking Confirmation",
                "sender": "surbhi.saraogi@treebohotels.com",
                "receivers": {
                    "to": email,
                    "cc": [],
                    "bcc": []
                },
                "consumer": "prowl",
                "attachments": [],
                "body_text": message + "\n" + car_info
            }
        }

        payload = json.dumps(data_values)
        headers = {'content-type': 'application/json'}
        r = requests.post(url=url, data=payload, headers=headers)
        print(r.json())

    def send_notification_to_owners(self, booking_code, owner_email):
        """
        send booking request to driver
         :param booking_code, owner_emal:
        """
        emails = []
        emails.append(owner_email)
        url = "http://api.treebohotels.com/v1/notification/email/"
        data_values = {

            "data": {
                "subject": "CarPool Booking Request",
                "sender": "surbhi.saraogi@treebohotels.com",
                "receivers": {
                    "to": emails,
                    "cc": [],
                    "bcc": []
                },
                "consumer": "prowl",
                "attachments": [],
                "body_text": "Click on the link below to confirm the booking request" + "\n http://127.0.0.1:5000/bookings/confirm_booking/" + booking_code
            }
        }
        payload = json.dumps(data_values)
        headers = {'content-type': 'application/json'}
        r = requests.post(url=url, data=payload, headers=headers)
        print(r.json())
