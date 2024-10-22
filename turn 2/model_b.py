import unittest
from unittest.mock import patch, MagicMock
import time
import your_module
import requests


class TestAPIs(unittest.TestCase):

    @patch('your_module.requests.post')
    def test_authenticate_success_with_variable_response_time(self, mock_post):
        # Mock response data for successful authentication
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"token": "dummytoken"}

        # Introduce a controlled delay using side_effect
        def delayed_post(*args, **kwargs):
            time.sleep(0.5)  # Simulate a 500ms delay
            return mock_response

        mock_post.side_effect = delayed_post

        username = "dummyuser"
        password = "dummypassword"
        start_time = time.time()
        token = your_module.authenticate(username, password)
        end_time = time.time()

        self.assertEqual(token, "dummytoken")
        self.assertLessEqual(end_time - start_time, 2.0)  # Assert response time is less than 2 seconds
        mock_post.assert_called_once_with(
            'http://example.com/api/login',
            json={"username": username, "password": password}
        )

    @patch('your_module.requests.get')
    def test_get_data_success_with_timeout(self, mock_get):
        # Mock response data for successful data retrieval
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "dummydata"}

        # Simulate a slow response that times out
        def slow_response(*args, **kwargs):
            time.sleep(2.5)
            return mock_response

        mock_get.side_effect = slow_response

        token = "dummytoken"
        with self.assertRaises(requests.exceptions.Timeout):
            your_module.get_data(token, timeout=2)  # Set a timeout of 2 seconds in the API call


if __name__ == "__main__":
    unittest.main()
