#!/user/bin/python3
#coding=utf-8
import unittest
#这里导入TestToRun这个测试类
from tests.test_to_run import TestSample
from tests.itesting_test import ItestingTest
if __name__ ==  "__main__":
    suite = unittest.TestSuite()
    #把导入进来得TestToRun这个测试类下面得测试方法加入测试用例
    suite.addTest(TestSample('test_02_not_equal'))
    suite.addTest(ItestingTest('test_01_itesting'))
    #指定runner为TextTestRunner
    runner = unittest.TextTestRunner(verbosity=2)

    runner.run(suite)