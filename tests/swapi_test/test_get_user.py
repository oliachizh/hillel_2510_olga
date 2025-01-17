import requests
import pytest
from hillel_2510_olga.core.api_services.swapi_ctrl import Swapi

swapi_ctrl= Swapi()

@pytest.mark.swapi
@pytest.mark.parametrize('user_id', [1,2,3])
def test_get_user(user_id):
    resp = swapi_ctrl.get_user(user_id)
    resp_data = resp.json()
    assert  resp_data['message'] == 'ok','Message is not OK'
    assert  int(resp_data['result']['uid']) == user_id,'Message is not OK'


@pytest.mark.swapi
@pytest.mark.parametrize('planet_id', [1,2,3])
def test_get_planet(planet_id):
    resp = swapi_ctrl.get_planet(planet_id)
    resp_data = resp.json()
    assert  resp_data['message'] == 'ok','Message is not OK'
    assert  int(resp_data['result']['uid']) == planet_id,'Message is not OK'


# # resp = requests.get('https://www.swapi.tech/api/planet/3')
# # print(resp.text)
# # print(resp.json()) #json.loads(resp.text)
#
