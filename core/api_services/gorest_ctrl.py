import requests
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from base_ctrl import BaseCtrl


class Gorest(BaseCtrl):
    headers = None
    def __init__(self, url='https://gorest.co.in/'):
        self.url=url


    @classmethod
    def _get_token(cls):
        return 'Bearer 02d047a8a46b9de36678ec848d7309cfc6e9828a7ee42f5af8c4bc84c5731487'

    @classmethod
    def _get_auth_headers(cls):
        if not cls.headers:
            cls.headers= dict()
            cls.headers['authorization'] = cls._get_token()
        return cls.headers


    def create_user(self, json, headers=None,expected_status_code=201):
        url = f'{self.url}public/v2/users'
        if not headers:
            headers = dict()
        headers.update(Gorest._get_auth_headers())
        return self.send_request(method='POST', json=json, url=url, headers=__class__.headers,
                                 expected_status_code=expected_status_code)

    def get_user(self, user_id, expected_status_code=200):
        url = f'{self.url}public/v2/users/{user_id}'
        return self.send_request(method='GET', url=url,
                                 expected_status_code=expected_status_code)



