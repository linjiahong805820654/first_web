#!/user/bin/python3
#coding=utf-8

import os
import unittest
from commer import run_html_report

#动态查找测试用例，discovery
if __name__ == "__main__":
    loader = unittest.defaultTestLoader

    #指定测试用例以什么开头
    #loader.testMethodPrefix = 'test'

    #生成测试用例
    #参数pattern='*.py',更改查找pattern得方式，查找所有py文件
    suite = loader.discover(os.path.join(os.path.dirname(__file__),"tests") ,pattern='*.py', top_level_dir=os.path.dirname(__file__))
    #指定runner为testtestrunner
    #runner = unittest.TextTestRunner(verbosity=2)
    #runner.run(suite)

    run_html_report.GenerateReport.generate_report(suite)
