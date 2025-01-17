import requests
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from base_ctrl import BaseCtrl


class Swapi(BaseCtrl):

    def __init__(self, url='https://www.swapi.tech/api/'):
        self.url=url


    def get_user(self, user_id: int, expected_status_code=200):
        return self.send_request(method='GET', url=f'{self.url}people/{user_id}',
                                 expected_status_code=expected_status_code)

    def get_users(self, params =None, expected_status_code=200):
        return self.send_request(method='GET', url=f'{self.url}people/', params=params,
                                 expected_status_code=expected_status_code)

    def get_planet(self, planet_id: int, expected_status_code=200):
        return self.send_request(method='GET', url=f'{self.url}planets/{planet_id}',
                                 expected_status_code=expected_status_code)

    # def get_search_user(self, search_by_name: str):
    #     return requests.get(f'{self.url}people/', params={'name': search_by_name})



