from http import HTTPStatus

from fake_store_api.fake_store_api_tests.products.methods import ProductsMethods


class FakeStoreAPIAssertions:
    @classmethod
    def assert_product_created(cls, response, product_id):
        assert response.status_code == HTTPStatus.CREATED
        data = ProductsMethods.get_single_product(id=product_id)
        assert data.status_code == HTTPStatus.OK
        assert 'application/json' in response.headers['Content-Type']

    @classmethod
    def assert_endpoint_not_existing(cls, response):
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert 'text/html' in response.headers['Content-Type']