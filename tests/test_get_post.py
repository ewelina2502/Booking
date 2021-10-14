import pytest
from models import booking
from models.booking import Bookings


def test_get_ids():
    get_ids = booking
    get_ids.get_ids_booking()


def test_get_id():
    get_id = booking
    get_id.get_id()


def test_get_id_fixture(new_booking):
    get_id_fixture = booking
    get_id_fixture.get_id_fixture(new_booking)


def test_get_id_details_from_fixture(new_booking):
    get_id_details = booking
    get_id_details.get_id_details_from_fixture(new_booking)


def test_add_booking():
    add_booking = Bookings()
    add_booking.add_booking()


@pytest.fixture
def new_booking():
    new_booking_one = Bookings()
    return new_booking_one.add_booking()
