#!/user/bin/python3
#coding=utf-8

#运行指定文件夹下得测试用例--py文件以test为头
import inspect
import os
import unittest

if __name__ == "__main__":
    #指定tests文件夹，并且把其中得module拿出来
    m = inspect.getmodulename(os.path.join(os.path.dirname(__file__), 'tests'))
    unittest.main(module=m, verbosity=2)