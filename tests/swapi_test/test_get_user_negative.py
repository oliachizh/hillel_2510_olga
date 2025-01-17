import requests
import pytest
from hillel_2510_olga.core.api_services.swapi_ctrl import Swapi

swapi_ctrl= Swapi()

@pytest.mark.swapi
@pytest.mark.parametrize('user_id', ['1'])
def test_get_user(user_id):
    resp = swapi_ctrl.get_user(user_id, expected_status_code=404)
    resp_data = resp.json()
