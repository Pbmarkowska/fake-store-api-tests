import requests

from fake_store_api.fake_store_api_tests.endpoints import CARTS


class CartsMethods:
    @staticmethod
    def get_all_carts():
        response = requests.get(f'{CARTS}')
        return response

    @staticmethod
    def add_new_cart(user_id, product_id):
        payload = {'userId': user_id, 'products':[{'id': product_id}]}
        response = requests.post(f'{CARTS}', json=payload)
        return response

    @staticmethod
    def get_single_cart(cart_id):
        response = requests.get(f'{CARTS}/{cart_id}')
        return response

    @staticmethod
    def update_cart(user_id, cart_id):
        payload = {'userId': user_id, 'products':[{'id': cart_id}]}
        response = requests.put(f'{CARTS}/{cart_id}', json=payload)
        return response

    @staticmethod
    def delete_cart(cart_id):
        response = requests.delete(f'{CARTS}/{cart_id}')
        return response

