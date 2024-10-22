
import unittest
from unittest.mock import patch, MagicMock
import requests

# Import the API module to be tested
import my_api

class TestMyAPI(unittest.TestCase):

    @patch('requests.post')
    def test_authenticate_success(self, mock_post):
        # Mock the response object
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "access_token": "dummy_access_token",
            "refresh_token": "dummy_refresh_token"
        }
        mock_post.return_value = mock_response

        # Call the authenticate function with dummy data
        result = my_api.authenticate("dummy_username", "dummy_password")

        # Assert that the function returned the expected result
        self.assertEqual(result, {
            "access_token": "dummy_access_token",
            "refresh_token": "dummy_refresh_token"
        })

        # Assert that the requests.post function was called with the correct arguments
        mock_post.assert_called_once_with(
            'https://example.com/api/authenticate',
            json={
                "username": "dummy_username",
                "password": "dummy_password"
            }
        )

if __name__ == '__main__':
    unittest.main()
