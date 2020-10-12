#!/user/bin/python3
#coding=utf-8

import unittest

class ItestingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("itestingtest 只执行一次")

    def setUp(self) -> None:
        print("itestingtest 每个用例执行一次")

    def test_01_itesting(self):
        self.assertEqual(1 , 1)

    def test_02_itesting(self):
        self.assertNotEqual(2 , 4)

    def equal_test_01(self):
        self.assertEqual( 3 , 3)

    def tearDown(self) -> None:
        print("itestingtest 每次用例都输出一次")

    @classmethod
    def tearDownClass(cls) -> None:
        print("itestingtest 结束，只输出一次")

if __name__ == "__main__":
    unittest.main()