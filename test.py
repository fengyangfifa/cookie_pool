# 验证Cookie的可用性
import re
import requests
from Cookies_pool.configs import *
from Cookies_pool.db import RedisClient
from requests.exceptions import ConnectionError


class ValidTester:
    def __init__(self, website='default'):
        self.website = website
        self.cookies_db = RedisClient('cookies', self.website)
        self.accounts_db = RedisClient('accounts', self.website)

    def test(self, username, cookies):
        raise NotImplementedError

    def run(self):
        cookies_groups = self.cookies_db.all()
        for username, cookies in cookies_groups.items():
            self.test(username, cookies)


class WeiboValidTester(ValidTester):
    def __init__(self, website='weibo'):
        ValidTester.__init__(self, website)

    def test(self, username, cookies):
        print('正在测试Cookies', '用户名', username)
        try:
            headers = {
                'Host': 'm.weibo.cn',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
                'Cookie': cookies
            }
            test_url = TEST_URL_MAP[self.website]
            response = requests.get(test_url, headers=headers, timeout=5, allow_redirects=False)
            if response.status_code == 200 and re.findall('userName', response.text):
                print('Cookies有效', username)
            else:
                print('Cookies失效', username)
                self.cookies_db.delete(username)
                print('删除Cookies', username)
        except ConnectionError as e:
            print(e.args)


# if __name__ == '__main__':
#     w = WeiboValidTester()
#     w.run()
