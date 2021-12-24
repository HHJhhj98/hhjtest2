# -*- coding：utf-8 -*-
# @Time ：2021/12/23 0:44
# @Authon :hhj
# @Annotation:
# @File : test.py
import os
import unittest
import HTMLTestRunner
import HTMLTestRunner_cn
import HTMLTestRunnerNew
from HwTestReport import HTMLTestReport


import datetime
import yagmail


# 把测试报告作为附件发送到指定邮箱
def send_mail(report):
    yag = yagmail.SMTP(user="3281502659@qq.com", password="pamhwavwqiofdbdf", host='smtp.qq.com',encoding='GBK')
    subject = "自动化测试报告"
    contents = "自动化用例已执行完毕，详细报告请查看附件"
    res=['2393022053@qq.com']
		#'2265817908@qq.com']
    yag.send(res, subject, contents, report)
    print("邮件已经发送成功！")

if __name__ == '__main__':
    suite = unittest.TestSuite()  # 存储用例的容器
    loader = unittest.TestLoader()  # 创建一个加载器
    import api_test #配合使用
    suite.addTest(loader.loadTestsFromModule(api_test))
    with open("test_report.html", 'wb') as file:
        # runner=HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title="单元测试报告", description="第一次报告")
        # runner=HTMLTestRunner_cn.HTMLTestRunner(stream=file, verbosity=2, title="单元测试报告", description="第一次报告")
        # runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="单元测试报告", description="第一次报告",tester="hhj")
        # runner = HTMLTestReport(stream=file, verbosity=2, title="单元测试报告", description="第一次报告", tester="hhj",
        #                         images=False)
        # runner.run(suite)
        # 获取当前时间，用于命名测试报告标题
        now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        from BeautifulReport import BeautifulReport
        run = BeautifulReport(suite)  # 实例化BeautifulReport模块
        path=os.path.abspath('.')+'\测试报告'+str(now)+'.html'
        run.report(filename='测试报告'+str(now), description='登录、充值模块')
        send_mail(path)


