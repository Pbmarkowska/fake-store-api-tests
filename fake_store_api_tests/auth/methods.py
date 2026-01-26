import random

import requests
from fake_store_api.fake_store_api_tests.endpoints import LOGIN

class AuthenticationMethods:
    @classmethod
    def login(cls, username=None, password=None):
        if username is None or password is None:
            data = cls.generate_login_data()
            username = data["username"]
            password = data["password"]
        payload = {"username": username, "password": password}
        response = requests.post(LOGIN, json=payload)
        return response

    @staticmethod
    def generate_login_data():
        random_username = f"{random.randint(1,100)}_username"
        random_password = f"pass{random.randint(1,100)}"

        return {
            "username": random_username,
            "password": random_password
        }