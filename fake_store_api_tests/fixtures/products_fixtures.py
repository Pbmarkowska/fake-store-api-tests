import pytest

from fake_store_api.fake_store_api_tests.products.methods import FakeStoreAPIMethods

@pytest.fixture(scope="class")
def get_product_id(request):
    response = FakeStoreAPIMethods.create_product(title="teddy bear")
    assert response.status_code == 201
    product_id = response.json()["id"]
    yield product_id
    FakeStoreAPIMethods.delete_product(product_id)