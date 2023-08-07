import unittest
import app as tested_app
import json


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_hello_endpoint(self):
        r = self.app.get('/')
        self.assertIn('CRUD',str(r.data))

    def test_post_hello_endpoint(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)

    # def test_post_add_endpoint(self):
        # r = self.app.post('/add',data='any')
        # self.assertEqual(r.json, {'status': 'OK'})
        # self.assertEqual(r.status_code, 200)

    def test_post_update_endpoint(self):
        r = self.app.post('/update')
        self.assertEqual(r.status_code, 302)

if __name__ == '__main__':
    unittest.main()