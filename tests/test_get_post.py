from models import booking
from models.booking import Bookings, new_booking


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


def test_get_id_fixture():
    get_id_fixture = booking
    get_id_fixture.get_id_fixture(new_booking)


# def test_get_id_fixture(new_booking):
#     response_get_id = requests.get(f'{url.get_id}' + '/' + '44')
#     assert response_get_id.status_code == 200


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
#     return response_add_booking.json()['bookingid']

#

