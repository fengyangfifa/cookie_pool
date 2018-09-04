# Redis数据库地址
REDIS_HOST = 'localhost'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

# 产生器类，如扩展其他站点，请在此配置
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}

# 测试类, 如扩展其他站点, 请在此配置
TESTER_MAP = {
    'weibo': 'WeiboValidTester'
}

TEST_URL_MAP = {
    'weibo': 'https://m.weibo.cn/'
}

# 产生器和验证器循环周期
VALID_CYCLE = 3600
GENERATE_CYCLE = 4000

# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = True
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = True
