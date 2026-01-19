from fake_store_api.fake_store_api_tests.products.methods import ProductsMethods


class FakeStoreAPIAssertions:
    @classmethod
    def assert_product_created(cls, response, id):
        assert response.status_code == 201
        data = ProductsMethods.get_single_product(id)
        assert data.status_code == 200