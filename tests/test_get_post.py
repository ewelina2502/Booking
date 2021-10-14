import pytest
import requests

import url
from models import booking
from models.booking import Bookings


def test_get_ids():
    get_ids = booking
    get_ids.get_ids_booking()


def test_get_id():
    get_id = booking
    get_id.get_id()


def test_get_id_details():
    get_id_details = booking
    get_id_details.get_id_details()


def test_add_booking():
    add_booking = Bookings()
    add_booking.add_booking()


def test_get_id_fixture(new_booking):
    get_id_fixture = booking
    get_id_fixture.get_id_fixture(new_booking)


@pytest.fixture
def new_booking():
    new_booking_one = Bookings()
    return new_booking_one.add_booking()


# def test_add_booking_second():
#     body = {
#         "firstname": "James",
#         "lastname": "Browns",
#         "totalprice": 1121,
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": "2021-01-01",
#             "checkout": "2021-01-02"
#         },
#         "additionalneeds": "Breakfast"
#     }
#
#     response_add_booking = requests.post(url.post_add_booking, json=body)
#     assert response_add_booking.status_code == 200
#     response_add_booking = response_add_booking.json()['bookingid']
#     print(response_add_booking)


# def test_add_booking_return_id():
#     body = {
#         "firstname": "James",
#         "lastname": "Browns",
#         "totalprice": 1121,
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": "2021-01-01",
#             "checkout": "2021-01-02"
#         },
#         "additionalneeds": "Breakfast"
#     }
#
#     response_add_booking = requests.post(url.post_add_booking, json=body)
#     assert response_add_booking.status_code == 200
#     return response_add_booking.json()['bookingid']
