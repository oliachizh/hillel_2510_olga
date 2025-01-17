import pytest
import time
from hillel_2510_olga.core.api_services.gorest_ctrl import Gorest

gorest = Gorest()

@pytest.mark.gorest
def test_get_user():
    resp = gorest.get_user(1, expected_status_code=404)