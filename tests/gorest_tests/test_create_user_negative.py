import pytest
from hillel_2510_olga.core.api_services.gorest_ctrl import Gorest

gorest = Gorest()

@pytest.mark.gorest
def test_create_user():
    body ={

    }
    resp = gorest.create_user(json=body, expected_status_code=422)