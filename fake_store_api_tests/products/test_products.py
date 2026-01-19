import pytest
import requests
from fake_store_api.fake_store_api_tests.products.methods import ProductsMethods
from fake_store_api.fake_store_api_tests.products.assertions import FakeStoreAPIAssertions


class TestProducts:
    def test_should_return_products(self):
        response = requests.get('https://fakestoreapi.com/products')
        assert response.status_code == 200

    def test_should_create_single_product(self):
        response = ProductsMethods.create_product(title="teddy bear")
        FakeStoreAPIAssertions.assert_product_created(response, response.json()['id'])

    def test_should_update_product(self, create_product_and_get_product_id):
        response = ProductsMethods.update_product(create_product_and_get_product_id, title="barbie doll")
        assert response.status_code == 200
        assert response.json()['title'] == 'barbie doll'

    def test_should_delete_product(self, create_product_and_get_product_id):
        response = ProductsMethods.delete_product(create_product_and_get_product_id)
        assert response.status_code == 200