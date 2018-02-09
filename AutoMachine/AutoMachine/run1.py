#encoding:utf-8
'''
Created on 2017年12月12日

@author: fy39919
'''
import unittest,HTMLTestRunner,time

test_case = './CaseList/'
test_report = './Report/'
discover = unittest.TestLoader()
discover = unittest.defaultTestLoader.discover(test_case,pattern = 'search*.py')
now = time.strftime("%Y-%m-%d %H-%M-%S")
file_path = './Report/' + now +'test_report.html'
file_result = open(file_path,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title = u"测试报告", description = u"用例执行情况")      
# runner.run(discover)
print(discover)
file_result.close 
    