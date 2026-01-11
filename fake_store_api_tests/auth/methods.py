import requests
from fake_store_api.fake_store_api_tests.endpoints import LOGIN

class LoginMethods:
    @classmethod
    def login(cls, username, password):
        payload = {"username": username, "password": password}
        response = requests.post(LOGIN, json=payload)
        return response