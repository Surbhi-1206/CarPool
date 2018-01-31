import requests
from flask import Flask, g
import json
from carpool.auth.AuthService import AuthService
from carpool.auth.UserDto import UserDto
from carpool.rides.RideService import RideService


class NotifyService:

    def send_notification_to_rider(self, rider, owner, ride_id):
        """
        send owner details to rider when booking is confirmed
        :return:
        """
        print(rider)
        email = []
        email.append(str(rider))
        print(email)
        auth_service = AuthService()
        ride_service = RideService()
        user_dto = UserDto(owner)
        user = auth_service.load_user(user_dto)
        owner_name = user.name
        owner_contact = user.contact
        ride_details = ride_service.get_ride_details(ride_id)
        message = "Your booking request from " + ride_details['pickup'] + " to " + ride_details[
            'drop'] + " has been confirmed."
        car_info = "Car Details:-"+"\n" + "Driver Name: " + owner_name + " Contact: " + owner_contact + " Car Number: " + \
                   ride_details['car_num']

        URL = "http://api.treebohotels.com/v1/notification/email/"
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
                "body_text": message+"\n"+car_info
            }
        }

        payload = json.dumps(data_values)
        headers = {'content-type': 'application/json'}
        r = requests.post(url=URL, data=payload, headers=headers)
        # print(r.url)
        print(r.json())


    def send_notification_to_owners(self, rides, sender, start, end):
        """
        send booking request to ride owners via email
         :param list_of_owners:
        """
        emails = []
        for ride in rides:
            print(ride.email)
            emails.append(ride.email)

        # print(emails)

        URL = "http://api.treebohotels.com/v1/notification/email/"
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
                "body_text": "http://127.0.0.1:5000/bookings/confirm_booking/" + sender + "/" + start + "/" + end
            }
        }

        payload = json.dumps(data_values)
        headers = {'content-type': 'application/json'}
        r = requests.post(url=URL, data=payload, headers=headers)
        # print(r.url)
        print(r.json())
