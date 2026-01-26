import requests

from fake_store_api.fake_store_api_tests.endpoints import PRODUCTS

class ProductsMethods:
    @staticmethod
    def get_products():
        response = requests.get(PRODUCTS)
        return response

    @staticmethod
    def get_single_product(id):
        response = requests.get(f'{PRODUCTS}/{id}')
        return response

    @staticmethod
    def create_product(title, description=None, category=None, image=None):
        payload = {"title": title, "description": description, "category": category, "image": image}
        response = requests.post(PRODUCTS, json=payload)
        return response

    @staticmethod
    def update_product(id, title=None, description=None, category=None, image=None):
        payload = {"title": title, "description": description, "category": category, "image": image}
        response = requests.put(f'{PRODUCTS}/{id}', json=payload)
        return response

    @staticmethod
    def delete_product(id):
        response = requests.delete(f"{PRODUCTS}/{id}")
        return response