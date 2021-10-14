import pytest

from models import booking
from models.booking import Bookings


def test_get_ids():
    get_ids = booking
    get_ids.get_ids_booking()


def test_add_booking():
    add_booking = Bookings()
    add_booking.add_booking()


def test_get_id():
    get_id = booking
    get_id.test_get_id()


def test_get_id_details(new_booking):
    get_id_details = booking
    get_id_details.test_get_id_details()


@pytest.fixture
def new_booking():
    new_booking = Bookings()
    return new_booking.add_booking()

