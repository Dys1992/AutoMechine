'''
Created on 2017年10月16日

@author: fy39919
'''

import unittest
import time 
import HTMLTestRunner


if __name__ == '__main__':
    test_case = './CaseList/'
    test_report = './Report/'
    discover = unittest.TestLoader()
    discover = unittest.defaultTestLoader.discover(test_case,pattern = 'search*.py')    
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    file_path = './Report/' + now +'test_report.html'
    file_result = open(file_path,'wb')
    
    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title = u"测试报告", description = u"用例执行情况")      
    runner.run(discover)
    
    file_result.close 
    
    