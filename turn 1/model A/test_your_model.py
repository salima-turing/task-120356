import unittest
from unittest.mock import patch, MagicMock
import your_module


class TestAPIs(unittest.TestCase):

    @patch('your_module.requests.post')
    def test_authenticate_success(self, mock_post):
        # Mock response data for successful authentication
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"token": "dummytoken"}
        mock_post.return_value = mock_response

        username = "dummyuser"
        password = "dummypassword"
        token = your_module.authenticate(username, password)

        self.assertEqual(token, "dummytoken")
        mock_post.assert_called_once_with(
            'http://example.com/api/login',
            json={"username": username, "password": password}
        )

    @patch('your_module.requests.get')
    def test_get_data_success(self, mock_get):
        # Mock response data for successful data retrieval
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "dummydata"}
        mock_get.return_value = mock_response

        token = "dummytoken"
        data = your_module.get_data(token)

        self.assertEqual(data, {"data": "dummydata"})
        mock_get.assert_called_once_with(
            'http://example.com/api/data',
            headers={"Authorization": "Bearer dummytoken"}
        )


if __name__ == "__main__":
    unittest.main()
