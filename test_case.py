import unittest
from dict import Urls
from unittest.mock import patch


class TestUrls(unittest.TestCase):

    def test_valid_urls(self):
        self.link = Urls()
        with patch('dict.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Valid Url'
            schedule = self.link.valid_url_1()
            mocked_get.assert_called_with('http://127.0.0.1:5000/')
            self.assertEqual(schedule, 'Valid Url')


if __name__ == '__main__':
    unittest.main()
