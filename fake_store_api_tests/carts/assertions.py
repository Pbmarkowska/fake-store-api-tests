import json
from http import HTTPStatus


class CartsAssertions:
    def __init__(self, response):
        self.response = response
        self._data = None

    @property
    def data(self):
        if self._data is None:
            try:
                self._data = json.loads(self.response.content.decode('utf-8'))
            except json.JSONDecodeError:
                raise AssertionError(
                    f'Response is not valid JSON\n'
                    f'Status code: {self.response.status_code}\n'
                    f'Body: {self.response.content[:300]}'
                )
        return self._data

    def assert_carts_retrieval_successful(self):
        assert self.response.status_code == HTTPStatus.OK
        assert isinstance(self.data, list)
        assert len(self.data) > 0

    @staticmethod
    def assert_carts_creation_successful(response):
        assert response.status_code == HTTPStatus.CREATED

    @staticmethod
    def assert_carts_update_successful(response):
        assert response.status_code == HTTPStatus.OK

    @staticmethod
    def assert_carts_delete_successful(response):
        assert response.status_code == HTTPStatus.OK


