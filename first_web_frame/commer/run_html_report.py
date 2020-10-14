#!/user/bin/python3
#coding=utf-8

import os
import HTMLTestRunner
import time
class GenerateReport():
    def __init__(self):
        now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        self.report_name = "/report/test_report" + now + ".html"
        self.test_base = os.path.dirname(os.path.dirname(__file__))
        if os.path.exists(os.path.join(self.test_base, self.report_name)):
            os.remove(os.path.join(self.test_base, self.report_name))
        fp = open(os.path.join(self.test_base, self.report_name), "a")
        fp.close()

    def generate_report(self, test_suits):
        fp = open(os.path.join(self.test_base, self.report_name),'a')
        runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = "test_report_itesting", description = "below report show the results of auto run")
        runner.run(test_suits)