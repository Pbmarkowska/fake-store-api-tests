

class UsersAssertions:
    @classmethod
    def assert_user_created(cls, response):
        assert response.status_code == 201
        assert response.json()['id'] is not None