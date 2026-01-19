from fake_store_api.fake_store_api_tests.users.assertions import UsersAssertions
from fake_store_api.fake_store_api_tests.users.methods import UsersMethods


class TestUsers:
    def test_should_create_user(self):
        response = UsersMethods.add_user("user", "user@gmail.com")
        UsersAssertions.assert_user_created(response)