import random
from datetime import date, timedelta
from faker import Faker
import requests
import url
from models.lower_upper import example_name

fake = Faker()

date_today = date.today()
date_checkout = date.today() + timedelta(days=10)

firstnames = ("Ewelina", "Adam", "Mikołaj")
lastnames = ("Brown", "Blue", "Orange")


def get_ids_booking():
    response_get_ids = requests.get(f'{url.get_ids}')
    assert response_get_ids.status_code == 200


def delete_booking(new_booking, new_token):
    headers = {
        "Cookie": "token=" + str(new_token)
    }
    response_delete_booking = requests.delete(f'{url.delete_newbooking}' + '/' + str(new_booking),
                                              headers=headers)
    assert response_delete_booking.status_code == 201


def put_booking(new_booking, new_token):
    headers = {
        "Cookie": "token=" + str(new_token)
    }
    body = {
        "firstname": str(f'{example_name}'),
        "lastname": "Update",
        "totalprice": int(random.randint(99, 999)),
        "depositpaid": "true",
        "bookingdates": {
            "checkin": str(f'{date_today}'),
            "checkout": str(f'{date_checkout}')
        },
        "additionalneeds": 'Break',
    }
    response_put_booking = requests.put(f'{url.put_booking}' + '/' + str(new_booking),
                                        headers=headers, json=body)
    assert response_put_booking.status_code == 200
    put_details = response_put_booking.json()
    print(put_details)


def patch_booking(new_booking, new_token):
    headers = {
        "Cookie": "token=" + str(new_token)
    }
    body = {
        "firstname": 'update',
        "lastname": 'patch'
    }
    response_patch_booking = requests.patch(f'{url.patch_booking}' + '/' + str(new_booking),
                                            headers=headers, json=body)
    assert response_patch_booking.status_code == 200
    patch_details = response_patch_booking.json()
    print(patch_details)


def get_id_fixture(new_booking):
    response_get_id = requests.get(f'{url.get_id}' + '/' + str(new_booking))
    assert response_get_id.status_code == 200


def get_id_details_from_fixture(new_booking):
    response_get_id = requests.get(f'{url.get_id}' + '/' + str(new_booking))
    assert response_get_id.status_code == 200
    firstname = response_get_id.json()['firstname']
    lastname = response_get_id.json()['lastname']
    additionalneeds = response_get_id.json()['additionalneeds']
    bookingdates_checkin = response_get_id.json()['bookingdates']['checkin']
    bookingdates_data = response_get_id.json()['bookingdates']

    print(
        '{', '"firstname": ', '"', firstname, '"',
        ",", '"lastname": ', '"', lastname, '"',
        ",", '"additionalneeds":', '"', additionalneeds, '"',
        ",", '"bookingdates_checkin":', '"', bookingdates_checkin, '"',
        ",", '"bookingdatesdata":', '"', bookingdates_data, '"',
        '}'
    )


class Bookings:

    def __init__(self, fnames=firstnames, lnames=lastnames):
        self.firstname = str(random.choice(fnames))
        self.lastname = str(random.choice(lnames))
        self.totalprice = random.randint(0, 2000)
        self.depositpaid = "true"
        self.checkin = str(f'{date_today}')
        self.checkout = str(f'{date_checkout}')
        self.additionalneeds = "Breakfast"

    def add_booking(self):
        body = {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "bookingdates": {
                "checkin": self.checkin,
                "checkout": self.checkout
            },
            "additionalneeds": self.additionalneeds
        }

        response_add_booking = requests.post(url.post_add_booking, json=body)
        assert response_add_booking.status_code == 200
        id_numer = response_add_booking.json()['bookingid']
        print('{', '"id_numer": ', '"', id_numer, '}')
        return response_add_booking.json()['bookingid']


def get_token():
    body = {
        "username": "admin",
        "password": "password123"
    }
    response_get_token = requests.post(url.url_token, json=body)
    assert response_get_token.status_code == 200
    token = response_get_token.json()
    print(token)
    return response_get_token.json()['token']
