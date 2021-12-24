# -*- coding：utf-8 -*-
# @Time ：2021/12/22 23:15
# @Authon :hhj
# @Annotation:
# @File : Api.py


from hhjtest.HttpRequest import HttpRequest

class Api:

    def __init__(self,url,method,data,headers):
        self.url=url
        self.method=method
        self.data=data
        self.headers=headers

    def login(self):
        # print(self.url,self.method,self.data,self.headers)
        login_res=HttpRequest().http_request(self.url,'post',self.data,self.headers)
        return login_res

    def recharge(self):
        recharge_res=HttpRequest().http_request(self.url,self.method,self.data,self.headers)
        return recharge_res

# if __name__=='__main__':
#     hq = HttpRequest()
#     # hq.http_request(url,"get")
#     url = "http://8.129.91.152:8766/futureloan/member/login"
#     data = {"mobile_phone": "15512345678", "pwd": "test12345"}
#     headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
#     login_res = hq.http_request(url, "post", data, headers)
#     member_id = login_res.json()["data"]["id"]
#     token = login_res.json()["data"]["token_info"]["token"]
#     print(login_res.json())