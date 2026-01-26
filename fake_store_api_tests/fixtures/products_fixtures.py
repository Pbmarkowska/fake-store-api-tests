import pytest

from fake_store_api.fake_store_api_tests.products.methods import ProductsMethods

@pytest.fixture(scope="class")
def create_product_and_get_product_id(request):
    response = ProductsMethods.create_product(title="teddy bear")
    assert response.status_code == 201
    assert 'application/json' in response.headers['Content-Type']
    product_id = response.json()["id"]
    yield product_id
    ProductsMethods.delete_product(product_id)