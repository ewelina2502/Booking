import requests
import url
from models.booking import Bookings

id_booking = 3


def test_get_ids():
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
    print(
        '{', '"total": ', get_details, ",", '"firstname": ', '"', firstname, '"', ",", '"lastname": ', '"', lastname, '"', '}'
    )


def test_add_booking():
    add_booking = Bookings()
    add_booking.add_booking()


