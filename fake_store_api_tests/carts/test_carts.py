from fake_store_api.fake_store_api_tests.carts.assertions import CartsAssertions
from fake_store_api.fake_store_api_tests.carts.methods import CartsMethods


class TestCarts:
    def test_get_all_carts(self):
        response = CartsMethods.get_all_carts()
        CartsAssertions(response).assert_carts_retrieval_successful()

