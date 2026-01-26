from http import HTTPStatus

import pytest
import requests

from fake_store_api.fake_store_api_tests.endpoints import PRODUCTS
from fake_store_api.fake_store_api_tests.products.methods import ProductsMethods
from fake_store_api.fake_store_api_tests.products.assertions import FakeStoreAPIAssertions


class TestProducts:
    def test_returns_products(self):
        response = requests.get(f'{PRODUCTS}')
        assert response.status_code == HTTPStatus.OK

    def test_creates_single_product(self):
        response = ProductsMethods.create_product(title="teddy bear")
        FakeStoreAPIAssertions.assert_product_created(response, response.json()['id'])

    def test_updates_product(self, create_product_and_get_product_id):
        response = ProductsMethods.update_product(create_product_and_get_product_id, title="barbie doll")
        assert response.status_code == HTTPStatus.OK
        assert response.json()['title'] == 'barbie doll'

    def test_deletes_product(self, create_product_and_get_product_id):
        response = ProductsMethods.delete_product(create_product_and_get_product_id)
        assert response.status_code == HTTPStatus.OK

    def test_returns_404_for_non_existing_endpoint(self):
        response = requests.get('https://fakestoreapi.com/produtcs')
        FakeStoreAPIAssertions.assert_endpoint_not_existing(response)
