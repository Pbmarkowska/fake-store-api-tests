import requests

from fake_store_api.fake_store_api_tests.endpoints import USERS


class UsersMethods:
    @staticmethod
    def get_users():
        response = requests.get(USERS)
        return response

    @staticmethod
    def add_user(username, email):
        payload = {'username': username, 'email': email}
        response = requests.post(USERS, json=payload)
        return response

    @staticmethod
    def get_single_user(user_id):
        # response = requests.get(f'{USERS}/{user_id}')
        response = requests.get(USERS.format(user_id))
        return response

    @staticmethod
    def update_user(user_id, username=None, email=None, password=None):
        payload = {'username': username, 'email': email, 'password': password}
        response = requests.put(USERS.format(user_id), json=payload)
        return response

    @staticmethod
    def delete_user(user_id):
        response = requests.delete(USERS.format(user_id))
        return response
