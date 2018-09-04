# 调度模块进行验证cookie的可用性和生成cookie
import time
from Cookies_pool.test import *
from Cookies_pool.configs import *
from multiprocessing import Process
from Cookies_pool.generators import *


class Scheduler:
    @classmethod
    def valid_cookie(cls, cycle=VALID_CYCLE):
        while True:
            print('Cookies检测进程开始运行')
            try:
                for website, fun in TESTER_MAP.items():
                    tester = eval(fun + '(website="' + website + '")')
                    tester.run()
                    print('Cookies检测完成')
                    del tester
                    time.sleep(cycle)
            except Exception as e:
                print(e.args)

    @classmethod
    def generate_cookie(cls, cycle=GENERATE_CYCLE):
        while True:
            print('Cookies生成进程开始运行')
            try:
                for website, fun in GENERATOR_MAP.items():
                    generator = eval(fun + '(website="' + website + '")')
                    generator.run()
                    print('Cookies生成完成')
                    del generator
                    time.sleep(cycle)
            except Exception as e:
                print(e.args)

    def run(self):
        if GENERATOR_PROCESS:
            generate_process = Process(target=Scheduler.generate_cookie)
            generate_process.start()
        if VALID_PROCESS:
            valid_process = Process(target=Scheduler.valid_cookie)
            valid_process.start()
