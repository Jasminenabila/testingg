import unittest
from TestCaseRegis import TestCaseFFRegisInvalidFormat
import os
import HTMLTestRunner
import time

direct = os.getcwd()

class TestSuite(unittest.TestCase):
    def test_report(self):

        regis = unittest.TestLoader().loadTestsFromTestCase(TestCaseFFRegisInvalidFormat)

        smoke_test = unittest.TestSuite([regis])

        dir = os.getcwd()

        outfile = open(dir + "/ReportFF.html", "w")

        runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title="Test Report Turnamen FF", description='Smoke Test FF')
        runner.run(smoke_test)

if __name__ == '__main__':
    unittest.main()