import requests
import curlify

class BaseCtrl:
    def send_request(self, method, url, params=None, headers=None, json=None, expected_status_code=None):
        print(f'Sending {method} request to {url}')
        response = getattr(requests, method.lower())(url=url, params=params, json=json, headers=headers)
        print(f'curl: \n{curlify.to_curl(response.request)}')
        if expected_status_code:
            assert response.status_code == expected_status_code, f'Status code is not {expected_status_code} but {response.status_code}'
        return response




        # if method.lower() == 'get':
        #     print(f'Sending {method} request to {url}')
        #     response = requests.get(url=url, params=params, headers=headers)
        #     print(f'curl: \n{curlify.to_curl(response.request)}')
        #     if expected_status_code:
        #         assert expected_status_code == expected_status_code, f'Status code is not {expected_status_code} but {response.status_code}'
        #     return response
        #
        # if method.lower() == 'post':
        #     print(f'Sending {method} request to {url}')
        #     response = requests.post(url=url, json=json, headers=headers)
        #     print(f'curl: \n{curlify.to_curl(response.request)}')
        #     if expected_status_code:
        #         assert expected_status_code == expected_status_code, f'Status code is not {expected_status_code} but {response.status_code}'
        #     return response
