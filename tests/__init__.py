from unittest import TestCase
from app import create_app


class Tester(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_helper(self):
        resp = self.client.get('/helper/')
        self.assertEqual(resp.status_code, 200, 'Should return 200')
        self.assertEqual(resp.data, b'Hello World', 'Should return correct text')
