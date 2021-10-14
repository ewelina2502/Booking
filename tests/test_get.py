import requests
import url
id_booking = 1


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

