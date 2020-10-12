#!/user/bin/python3
#coding=utf-8
import unittest

#测试类必须要继承TestCase类
class TestSample(unittest.TestCase):

    #类共享fixture
    @classmethod
    def setUpClass(self):
        print("整个测试只输出一次--one")

    def setUp(self):
        print("每次执行用例就输出一次--every one")

    #忽略测试用例得执行
    @unittest.skip('忽略了这条测试用例')                  #执行时直接忽略掉被装饰的测试用例
    #@unittest.skipIf()                #如果 skipIf 里的条件成立，执行时直接忽略掉被装饰的测试用例；
    #@unittest.skipUnless()            #永久在执行时忽略被装饰的测试用例，除非 skipUnless 里的条件成立
    #@unittest.expectedFailure        #标记失败用例，用例失败则标记为测试通过

    def test_01_equal(self):
        self.assertEqual(1 , 1)

    def test_02_not_equal(self):
        self.assertNotEqual(2 , 4)

    def tearDown(self):
        print("每次执行用例结束后就输出一次--end every")

    @classmethod
    def tearDownClass(self):
        print("整个测试只输出一次--end")

if __name__ == "__main__":
    unittest.main()