# 调用redis中的accounts, 生成Cookie
from Cookies_pool.db import RedisClient
from Cookies_pool.Generator_cookies import WeiboCookies


class CookiesGenerator:
    def __init__(self, website='default'):
        self.website = website
        self.cookies_db = RedisClient('cookies', self.website)
        self.accounts_db = RedisClient('accounts', self.website)

    def new_cookies(self, username, password):
        raise NotImplementedError

    def run(self):
        accounts_username = self.accounts_db.usernames()
        cookies_username = self.cookies_db.usernames()

        for username in accounts_username:
            if username not in cookies_username:
                password = self.accounts_db.get(username)
                print('正在生成Cookies', '账号', username, '密码', password)
                result = self.new_cookies(username, password)
                if result.get('status') == 1:
                    cookies = result.get('content')
                    print('成功获取到Cookies', cookies)
                    if self.cookies_db.set(username, cookies):
                        print('成功保存Cookies')
                elif result.get('status') == 2:
                    print(result.get('content'))
                    if self.accounts_db.delete(username):
                        print('成功删除账号')
                else:
                    print(result.get('content'))
        print('所有账号都已经成功获取Cookies')


class WeiboCookiesGenerator(CookiesGenerator):
    def __init__(self, website='weibo'):
        CookiesGenerator.__init__(self, website)

    def new_cookies(self, username, password):
        result = WeiboCookies(username, password).login()
        return result


# if __name__ == '__main__':
#     g = WeiboCookiesGenerator()
#     g.run()
