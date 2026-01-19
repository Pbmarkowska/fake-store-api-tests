from operator import contains


class AuthAssertions:
    @classmethod
    def assert_login_successful(cls, response):
        assert response.status_code == 200
        assert 'token' in response.json()
        assert response.json('token') is not None

    @classmethod
    def assert_login_unsuccessful(cls, response):
        assert response.status_code == 401
        assert response.text == 'username or password is incorrect'