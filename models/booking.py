import random
import requests
import url

id_booking = 2


def get_id():
    response_get_id = requests.get(f'{url.get_id}' + '/' + f'{id_booking}')
    assert response_get_id.status_code == 200


def get_ids_booking():
    response_get_ids = requests.get(f'{url.get_ids}')
    assert response_get_ids.status_code == 200


def get_id_fixture(new_booking):
    response_get_id = requests.get(f'{url.get_id}' + '/' + str(new_booking))
    assert response_get_id.status_code == 200


def get_id_details_from_fixture(new_booking):
    response_get_id = requests.get(f'{url.get_id}' + '/' + str(new_booking))
    assert response_get_id.status_code == 200
    firstname = response_get_id.json()['firstname']
    lastname = response_get_id.json()['lastname']
    additionalneeds = response_get_id.json()['additionalneeds']
    print(
        '{', '"firstname": ', '"', firstname, '"', ",", '"lastname": ', '"',
        lastname, '"', ",", '"additionalneeds":', '"', additionalneeds, '"', '}')


firstnames = ("Ewelina", "Adam", "Mikołaj")
lastnames = ("Brown", "Blue", "Orange")


class Bookings:

    def __init__(self, fnames=firstnames, lnames=lastnames):
        self.firstname = str(random.choice(fnames))
        self.lastname = str(random.choice(lnames))
        self.totalprice = random.randint(0, 1000)
        self.depositpaid = "true"
        self.checkin = "2021-01-01"
        self.checkout = "2021-01-02"
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
