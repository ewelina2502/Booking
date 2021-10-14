import random
import requests
import url

id_booking = 1


def get_ids_booking():
    response_get_ids = requests.get(f'{url.get_ids}')
    assert response_get_ids.json()
    get_ids = response_get_ids.json()
    print(get_ids)


def test_get_id():
    response_get_id = requests.get(f'{url.get_id}' + f'{id_booking}')
    assert response_get_id.json()
    get_id = response_get_id.json()
    print(get_id)


def test_get_id_details():
    response_get_id = requests.get(f'{url.get_id}' + f'{id_booking}')
    assert response_get_id.status_code == 200
    get_details = response_get_id.json()['totalprice']
    firstname = response_get_id.json()['firstname']
    lastname = response_get_id.json()['lastname']
    additionalneeds = response_get_id.json()['additionalneeds']
    print(
        '{', '"total": ', get_details, ",", '"firstname": ', '"', firstname, '"', ",", '"lastname": ', '"',
        lastname, '"', ",", '"additionalneeds":', '"', additionalneeds, '"', '}')


class Bookings:

    def __init__(self):
        self.firstname = "James"
        self.lastname = "Browns"
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
        add_booking = response_add_booking.json()['bookingid']
        print(add_booking)
