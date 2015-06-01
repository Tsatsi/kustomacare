import unittest
from app import app


class TestHomeAPI(unittest.TestCase):
    def test_home_controller_should_return_list_of_companies(self):
        self.app_test_client = app.test_client()
        response = self.app_test_client.get('/')
        self.assertEqual('200 OK', response.status)
