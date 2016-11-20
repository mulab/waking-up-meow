from unittest import TestCase
import datetime
from app import create_app
from tests.util import create_message_from_wechat


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

    def test_rename(self):
        data = create_message_from_wechat(content='我是纯纯')
        headers = { 'Content-type': 'application/xml' }
        resp = self.client.post('/wechat/', data=data, headers=headers)
        resp_xml = resp.data.decode('utf-8')
        self.assertEqual(resp.status_code, 200, 'Should return 200')
        self.assertIn('改名成功', resp_xml)

    def test_checkin_success(self):
        create_time = datetime.datetime(2016, 11, 20, 8) + datetime.timedelta(hours=8) # 8:00 a.m.
        data = create_message_from_wechat(content='签到', create_time=create_time)
        headers = { 'Content-type': 'application/xml' }
        resp = self.client.post('/wechat/', data=data, headers=headers)
        resp_xml = resp.data.decode('utf-8')
        self.assertEqual(resp.status_code, 200, 'Should return 200')
        self.assertIn('签到成功', resp_xml)

    def test_checkin_fail(self):
        create_time = datetime.datetime(2016, 11, 20, 11) + datetime.timedelta(hours=8) # 11:00 a.m.
        data = create_message_from_wechat(content='签到', create_time=create_time)
        headers = { 'Content-type': 'application/xml' }
        resp = self.client.post('/wechat/', data=data, headers=headers)
        resp_xml = resp.data.decode('utf-8')
        self.assertEqual(resp.status_code, 200, 'Should return 200')
        self.assertIn('签到失败', resp_xml)

    # TODO: you should add more tests, such as checkin rank and other functions needed.
