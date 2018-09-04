# 存cookie和accounts
import redis
import random
from Cookies_pool.configs import *


class RedisClient:
    def __init__(self, types, website, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
        self.type = types
        self.website = website

    def name(self):
        return '{}:{}'.format(self.type, self.website)

    def set(self, username, value):
        return self.db.hset(self.name(), username, value)

    def get(self, username):
        return self.db.hget(self.name(), username)

    def delete(self, username):
        return self.db.hdel(self.name(), username)

    def count(self):
        return self.db.hlen(self.name())

    def random(self):
        return random.choice(self.db.hvals(self.name()))

    def usernames(self):
        return self.db.hkeys(self.name())

    def all(self):
        return self.db.hgetall(self.name())


# if __name__ == '__main__':
#     r = RedisClient('cookies', 'weibo')
#     # r.set('18244325218', 'fywy.fifa1998')
#     # print(r.usernames())
#     # print(r.get('18244325218'))
#     # print(r.random())
#     # r.delete('18244325218')
#     print(r.all())
