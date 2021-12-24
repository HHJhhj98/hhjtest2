# -*- coding：utf-8 -*-
# @Time ：2021/12/22 23:23
# @Authon :hhj
# @Annotation:
# @File : api_test.py
import unittest
import time
from HwTestReport import HTMLTestReport
from hhjtest.Api import Api

login_url='http://8.129.91.152:8766/futureloan/member/login'
login_headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
recharge_url = "http://8.129.91.152:8766/futureloan/member/recharge"
# member_id=login_res.json()["data"]["id"]
# token=login_res.json()["data"]["token_info"]["token"]

class ApiTest(unittest.TestCase):

    def test_alogin_azc(self):
        data = {"mobile_phone": "15512345678", "pwd": "test12345"}
        res=Api(login_url,'post',data,login_headers).login()
        try:
            self.assertEqual('OK', res.json()['msg'])#判断相等
            member_id=res.json()['data']['id']
            token=res.json()["data"]["token_info"]["token_type"]+' '+res.json()["data"]["token_info"]["token"]
            print(member_id,token)
            # self.assertIsNone(res)#判断为空
            # self.assertIsNotNone(res)#判断不为空
            # self.assertIsInstance(a,b)#a是否为b的实例
            # self.assertNotIsInstance(a, b)  # a是否不为b的实例
        except AssertionError as e:
            print("出错了！断言错误是{0}".format(e))
            raise e  # 异常抛出


    def test_login_bszh(self):
        data = {"mobile_phone": "", "pwd": "test12345"}
        res=Api(login_url,'post',data,login_headers).login()
        try:
            self.assertEqual('手机号码为空', res.json()['msg'])#判断相等
            # self.assertIsNone(res)#判断为空
            # self.assertIsNotNone(res)#判断不为空
            # self.assertIsInstance(a,b)#a是否为b的实例
            # self.assertNotIsInstance(a, b)  # a是否不为b的实例
        except AssertionError as e:
            print("出错了！断言错误是{0}".format(e))
            raise e  # 异常抛出

    def test_login_bsmm(self):
        data = {"mobile_phone": "15512345678", "pwd": ""}
        res=Api(login_url,'post',data,login_headers).login()
        try:
            self.assertEqual('密码为空', res.json()['msg'])#判断相等
            # self.assertIsNone(res)#判断为空
            # self.assertIsNotNone(res)#判断不为空
            # self.assertIsInstance(a,b)#a是否为b的实例
            # self.assertNotIsInstance(a, b)  # a是否不为b的实例
        except AssertionError as e:
            print("出错了！断言错误是{0}".format(e))
            raise e  # 异常抛出

    def test_login_bsmmcw(self):
        data = {"mobile_phone": "15512345678", "pwd": "test123456"}
        res = Api(login_url, 'post', data, login_headers).login()
        try:
            self.assertEqual('账号信息错误', res.json()['msg'])  # 判断相等
            # self.assertIsNone(res)#判断为空
            # self.assertIsNotNone(res)#判断不为空
            # self.assertIsInstance(a,b)#a是否为b的实例
            # self.assertNotIsInstance(a, b)  # a是否不为b的实例
        except AssertionError as e:
            print("出错了！断言错误是{0}".format(e))
            raise e  # 异常抛出

    def test_recharge_zc(self):
        login_data = {"mobile_phone": "15512345678", "pwd": "test12345"}
        res = Api(login_url, 'post', login_data, login_headers).login()
        member_id = res.json()['data']['id']
        token = res.json()["data"]["token_info"]["token_type"] + ' ' + res.json()["data"]["token_info"]["token"]
        data = {"member_id": member_id, "amount": 100}
        print(member_id)
        headers = {"user-agent": ":Mozilla/5.0", "X-Lemonban-Media-Type": "lemonban.v2",
                   "Content-Type": "application/json","Authorization": token}
        res = Api(recharge_url, 'post', data, headers).recharge()
        try:
            self.assertEqual('OK', res.json()['msg'])  # 判断相等
            # self.assertIsNone(res)#判断为空
            # self.assertIsNotNone(res)#判断不为空
            # self.assertIsInstance(a,b)#a是否为b的实例
            # self.assertNotIsInstance(a, b)  # a是否不为b的实例
        except AssertionError as e:
            print("出错了！断言错误是{0}".format(e))
            raise e  # 异常抛出

    def test_recharge_bszh1(self):
        '''不输账号'''
        login_data = {"mobile_phone": "15512345678", "pwd": "test12345"}
        res = Api(login_url, 'post', login_data, login_headers).login()
        member_id = res.json()['data']['id']
        token = res.json()["data"]["token_info"]["token_type"] + ' ' + res.json()["data"]["token_info"]["token"]
        data = {"member_id": '', "amount": 100}
        headers = {"user-agent": ":Mozilla/5.0", "X-Lemonban-Media-Type": "lemonban.v2",
                   "Content-Type": "application/json","Authorization": token}
        res = Api(recharge_url, 'post', data, headers).recharge()
        try:
            self.assertEqual('用户id为空1', res.json()['msg'])  # 判断相等
            # self.assertIsNone(res)#判断为空
            # self.assertIsNotNone(res)#判断不为空
            # self.assertIsInstance(a,b)#a是否为b的实例
            # self.assertNotIsInstance(a, b)  # a是否不为b的实例
        except AssertionError as e:
            print("出错了！断言错误是{0}".format(e))
            raise e  # 异常抛出

    def test_recharge_bszh(self):
        login_data = {"mobile_phone": "15512345678", "pwd": "test12345"}
        res = Api(login_url, 'post', login_data, login_headers).login()
        member_id = res.json()['data']['id']
        token = res.json()["data"]["token_info"]["token_type"] + ' ' + res.json()["data"]["token_info"]["token"]
        data = {"member_id": "", "amount": 100}
        headers = {"user-agent": ":Mozilla/5.0", "X-Lemonban-Media-Type": "lemonban.v2",
                   "Content-Type": "application/json","Authorization": token}
        res = Api(recharge_url, 'post', data, headers).recharge()
        try:
            self.assertEqual('用户id为空', res.json()['msg'])  # 判断相等
            # self.assertIsNone(res)#判断为空
            # self.assertIsNotNone(res)#判断不为空
            # self.assertIsInstance(a,b)#a是否为b的实例
            # self.assertNotIsInstance(a, b)  # a是否不为b的实例
        except AssertionError as e:
            print("出错了！断言错误是{0}".format(e))
            raise e  # 异常抛出

    def test_recharge_bsje(self):
        login_data = {"mobile_phone": "15512345678", "pwd": "test12345"}
        res = Api(login_url, 'post', login_data, login_headers).login()
        member_id = res.json()['data']['id']
        token = res.json()["data"]["token_info"]["token_type"] + ' ' + res.json()["data"]["token_info"]["token"]
        data = {"member_id": member_id}
        headers = {"user-agent": ":Mozilla/5.0", "X-Lemonban-Media-Type": "lemonban.v2",
                   "Content-Type": "application/json","Authorization": token}
        res = Api(recharge_url, 'post', data, headers).recharge()
        try:
            self.assertEqual('数字格式化异常', res.json()['msg'])  # 判断相等
            # self.assertIsNone(res)#判断为空
            # self.assertIsNotNone(res)#判断不为空
            # self.assertIsInstance(a,b)#a是否为b的实例
            # self.assertNotIsInstance(a, b)  # a是否不为b的实例
        except AssertionError as e:
            print("出错了！断言错误是{0}".format(e))
            raise e  # 异常抛出

    def test_recharge_srfs(self):
        login_data = {"mobile_phone": "15512345678", "pwd": "test12345"}
        res = Api(login_url, 'post', login_data, login_headers).login()
        member_id = res.json()['data']['id']
        token = res.json()["data"]["token_info"]["token_type"] + ' ' + res.json()["data"]["token_info"]["token"]
        data = {"member_id": member_id, "amount": -100}
        headers = {"user-agent": ":Mozilla/5.0", "X-Lemonban-Media-Type": "lemonban.v2",
                   "Content-Type": "application/json","Authorization": token}
        res = Api(recharge_url, 'post', data, headers).recharge()
        try:
            self.assertEqual('余额必须大于0并且小于或者等于500000', res.json()['msg'])  # 判断相等
            # self.assertIsNone(res)#判断为空
            # self.assertIsNotNone(res)#判断不为空
            # self.assertIsInstance(a,b)#a是否为b的实例
            # self.assertNotIsInstance(a, b)  # a是否不为b的实例
        except AssertionError as e:
            print("出错了！断言错误是{0}".format(e))
            raise e  # 异常抛出

    def login(self):
        data = {"mobile_phone": "15512345678", "pwd": "test12345"}
        res = Api(login_url, 'post', data, login_headers).login()
        return res

# if __name__=='__main__':
    # unittest.main()#执行所有的用例
    # url = "http://8.129.91.152:8766/futureloan/member/recharge"
    # data = {"member_id": member_id, "amount": 100}
    # headers = {"user-agent": ":Mozilla/5.0", "X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json",
    #            "Authorization": "Bearer " + token}
    # recharge_res = hq.http_request(url,"post",data,headers)

    # from python_11.day_1015 import class_01  # 配合使用

