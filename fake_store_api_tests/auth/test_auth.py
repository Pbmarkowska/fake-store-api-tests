from fake_store_api.fake_store_api_tests.auth.methods import AuthenticationMethods
from fake_store_api.fake_store_api_tests.auth.assertions import AuthAssertions


class TestAuth:
    def test_login_unsuccessful(self):
        response = AuthenticationMethods.login()
        AuthAssertions.assert_login_unsuccessful(response)
