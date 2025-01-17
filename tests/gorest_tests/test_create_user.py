import pytest
import time
from hillel_2510_olga.core.api_services.gorest_ctrl import Gorest

gorest = Gorest()

@pytest.mark.gorest
def test_create_user():
    body ={
        "name": "Tenali Ramakrishna",
        "gender": "male",
        "email": f"tenali.ramakrishna@{time.time()}.com",
        "status": "active"
    }
    resp = gorest.create_user(json=body)


    # def test_get_user(user_id):
    #     resp = swapi_ctrl.get_user(user_id)
    #     resp_data = resp.json()
    #     assert resp_data['message'] == 'ok', 'Message is not OK'
    #     assert int(resp_data['result']['uid']) == user_id, 'Message is not OK'


