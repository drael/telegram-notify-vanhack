import unittest
import json
from app import app
from flask import request

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.config['TOKEN'] = 'test'
        self.app_context = app.app_context()
        self.app_context.push()
        self.client = app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_tgmessage(self):
        with app.test_request_context('/tgmessage', method='GET'):
            assert request.path == '/tgmessage'
            assert request.method == 'GET'

    def test_tgmessage_post(self):
        with app.test_request_context('/tgmessage', method='POST'):
            assert request.path == '/tgmessage'
            assert request.method == 'POST'

    def test_tgmessage_get_status_code(self):
        r = self.client.get('/tgmessage')
        self.assertTrue(r.status_code == 405)

    # def test_tgmessage_post_status_code_200(self):
    #     data = {'van': 'hack'}
    #     r = self.client.post('/tgmessage', data=json.dumps(data), headers={'token': 'test', 'Content-Type': 'application/json'})
    #     print(r)
    #     self.assertTrue(r.status_code == 200)

    def test_tgmessage_post_status_code_400(self):
        data = {'will': 'fail'}
        r = self.client.post('/tgmessage', data=data, headers={'token': 'test'})
        self.assertTrue(r.status_code == 400)

    def test_tgmessage_post_status_code_401(self):
        data = {'not': 'authorized'}
        r = self.client.post('/tgmessage', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        self.assertTrue(r.status_code == 401)

if __name__ == '__main__':
    unittest.main(verbosity=2)