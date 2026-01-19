import requests

from fake_store_api.fake_store_api_tests.endpoints import USERS


class UsersMethods:
    @classmethod
    def get_users(cls):
        response = requests.get(USERS)
        return response

    @classmethod
    def add_user(cls, username, email):
        payload = {'username': username, 'email': email}
        response = requests.post(USERS, json=payload)
        return response

    @classmethod
    def get_single_user(cls, user_id):
        # response = requests.get(f'{USERS}/{user_id}')
        response = requests.get(USERS.format(user_id))
        return response

    @classmethod
    def update_user(cls, user_id, username=None, email=None, password=None):
        payload = {'username': username, 'email': email, 'password': password}
        response = requests.put(USERS.format(user_id), json=payload)
        return response

    @classmethod
    def delete_user(cls, user_id):
        response = requests.delete(USERS.format(user_id))
        return response
