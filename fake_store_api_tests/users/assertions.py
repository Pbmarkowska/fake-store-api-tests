from http import HTTPStatus


class UsersAssertions:
    @classmethod
    def assert_user_created(cls, response):
        assert response.status_code == HTTPStatus.CREATED
        assert response.json()['id'] is not None