import requests

from fake_store_api.fake_store_api_tests.endpoints import PRODUCTS

class FakeStoreAPIMethods:
    @classmethod
    def get_products(cls):
        response = requests.get(PRODUCTS)
        return response

    @classmethod
    def get_single_product(cls, id):
        response = requests.get(f'{PRODUCTS}/{id}')
        return response

    @classmethod
    def create_product(cls, title, description=None, category=None, image=None):
        payload = {"title": title, "description": description, "category": category, "image": image}
        response = requests.post(PRODUCTS, json=payload)
        return response

    @classmethod
    def update_product(cls, id, title=None, description=None, category=None, image=None):
        payload = {"title": title, "description": description, "category": category, "image": image}
        response = requests.put(f'{PRODUCTS}/{id}', json=payload)
        return response

    @classmethod
    def delete_product(cls, id):
        response = requests.delete(f"{PRODUCTS}/{id}")
        return response