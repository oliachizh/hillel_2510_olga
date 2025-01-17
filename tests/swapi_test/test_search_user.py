import requests
import pytest
from hillel_2510_olga.core.api_services.swapi_ctrl import Swapi

swapi_ctrl= Swapi()

@pytest.mark.swapi
def test_get_search_user():
    resp = swapi_ctrl.get_users(params={'name':'r2'})
    resp_data = resp.json()
    print(resp_data)
    assert  resp_data['message'] == 'ok','Message is not OK'
    assert 'r2' in resp_data['result'][0]['properties']['name'].lower(),'Message is not OK'
