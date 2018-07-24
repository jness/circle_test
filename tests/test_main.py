import unittest

import requests_mock

from circle_test.main import *


class MainTestCase(unittest.TestCase):

    def setUp(self):
        """
        Setup test case
        """

        self.url = 'http://circleci.com/'

    @requests_mock.Mocker()
    def test_main(self, mock):
        """
        Test main with request mock
        """

        mock.get(self.url, text='resp')
        main()


    @requests_mock.Mocker()
    def test_main_failure(self, mock):
        """
        Test main with request mock as failure
        """

        mock.get(self.url, text='resp', status_code=500)
        main()
