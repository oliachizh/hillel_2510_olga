import requests
import pytest
from hillel_2510_olga.core.api_services.swapi_ctrl import Swapi

swapi_ctrl= Swapi()

@pytest.mark.swapi
def test_get_user():
    resp = swapi_ctrl.get_users()
    resp_data = resp.json()
    print(resp_data)
    # assert  resp_data['message'] == 'ok','Message is not OK'
    # assert  int(resp_data['result']['uid']) == user_id,'Message is not OK'