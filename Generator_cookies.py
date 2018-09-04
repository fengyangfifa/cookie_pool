# 生成Cookie
import random
import requests


class WeiboCookies:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.data = {
            'username': self.username,
            'password': self.password,
            'savestate': 1,
            'r': 'https://m.weibo.cn/',
            'ec': 0,
            'pagerefer': '',
            'entry': 'mweibo',
            'wentry': '',
            'loginfrom': '',
            'client_id': '',
            'code': '',
            'qq': '',
            'mainpageflag': 1,
            'hff': '',
            'hfp': ''
        }
        self.user_agent = [
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
        ]
        self.headers = {
            'Host': 'passport.weibo.cn',
            'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https://m.weibo.cn/',
            'User-Agent': random.choice(self.user_agent)
        }

    def login(self):
        r = self.session.post(url='https://passport.weibo.cn/sso/login', data=self.data, headers=self.headers)
        html = r.json()
        cookies = {}
        if html.get('retcode') == 20000000:
            cookies['status'] = 1
            cookies['content'] = self.get_cookies()
        elif html.get('retcode') == 50011002:
            cookies['status'] = 2
            cookies['content'] = html
        else:
            cookies['status'] = 3
            cookies['content'] = html
        return cookies

    def get_cookies(self):
        cookies = self.session.cookies.items()
        cookie = ''
        for i in cookies:
            cookie += '; ' + '='.join(i)
        cookie = cookie[2:]
        return cookie


w = WeiboCookies('**********', '*********')
w.login()
result = w.get_cookies()
print(result)
