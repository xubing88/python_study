# -*- coding: utf-8 -*-

import unittest

import requests


class RequestsTestSuite(unittest.TestCase):
    """Requests test cases."""#你好
    
    def setUp(self):
        pass

    def tearDown(self):
        """Teardown."""
        pass
        
    def test_invalid_url(self):
        self.assertRaises(ValueError, requests.get, 'hiwpefhipowhefopw')

    def test_HTTP_200_OK_GET(self):
        r = requests.get('http://www.baidu.com')
        self.assertEqual(r.status_code, 200)

    def test_HTTPS_200_OK_GET(self):
        r = requests.get('https://www.baidu.com')
        self.assertEqual(r.status_code, 200)

    def test_HTTP_200_OK_HEAD(self):
        r = requests.head('http://www.baidu.com')
        self.assertEqual(r.status_code, 200)

    def test_HTTPS_200_OK_HEAD(self):
        r = requests.head('https://www.baidu.com')
        self.assertEqual(r.status_code, 200)

    '''def test_AUTH_HTTPS_200_OK_GET(self):
        auth = requests.AuthObject('requeststest', 'requeststest')
        url = 'https://convore.com/api/account/verify.json'
        r = requests.get(url, auth=auth)

        self.assertEqual(r.status_code, 200)
    '''

if __name__ == '__main__':
    unittest.main()
