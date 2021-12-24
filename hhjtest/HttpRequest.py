# -*- coding：utf-8 -*-
# @Time ：2021/9/1 22:33
# @Authon :hhj
# @Annotation:
# @File : HttpRequest.py

import requests

class HttpRequest:
    '''
    利用request封装get请求和post请求
    '''

    def http_request(self,url,method,data=None,headers=None,cookies=None):
        '''
        url:请求地址 http：xxx：port
        data：传递参数，非必填，字典的格式传递参数
        cookies：非必填
        method:请求方式：get、post
        :return: 响应的json结果
        '''

        # print(url,method,data,headers)
        if method.lower()=='get': #强制转换为小写
            res=requests.get(url=url,data=data,headers=headers,cookies=cookies,verify=False)
        elif method.lower()=='post':
            res = requests.post(url=url,json=data,headers=headers, cookies=cookies,verify=False)
        print("响应正文:",res.json())
        return res #返回消息实体
        #return res.json()#返回消息正文

# if __name__=='__main__':
# # #     url = "http://8.129.91.152:8765/Index/login.html"
#     hq=HttpRequest()
#     # hq.http_request(url,"get")
#     url = "http://8.129.91.152:8766/futureloan/member/login"
#     data = {"mobile_phone": "15512345678", "pwd": "test12345"}
#     headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
#     login_res=hq.http_request(url,"post",data,headers)
#     member_id=login_res.json()["data"]["id"]
#     token=login_res.json()["data"]["token_info"]["token"]
#     print(login_res.json())
#
#     url = "http://8.129.91.152:8766/futureloan/member/recharge"
#     data = {"member_id": member_id, "amount": -100}
#     headers = {"user-agent": ":Mozilla/5.0", "X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json",
#                "Authorization": "Bearer " + token}
#     recharge_res = hq.http_request(url,"post",data,headers)
#     print(recharge_res.json())


    # login_url='https://v4.ketangpai.com/UserApi/login'
    # data={'email':'17307428595','password':'huhuijia1998','remember':1}
    # hq = HttpRequest()
    # res=hq.http_request(login_url,'post',data)
    # print("登录：{0}".format(res.json()))
    # print("cookies:",res.cookies)
    #
    # work_url='https://v4.ketangpai.com/HomeworkApi/listsHomework?courseid=MDAwMDAwMDAwMLOGpd6Gz6tqhNtyoQ'
    # res_w=hq.http_request(work_url,'get',{},res.cookies)
    #print("作业：{0}".format(res_w.text))