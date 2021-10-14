import requests
import url


class Bookings:

    def __init__(self):
        self.firstname = "James"
        self.lastname = "Browns"
        self.totalprice = 1121
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
        add_booking = response_add_booking.json()
        print(add_booking)

