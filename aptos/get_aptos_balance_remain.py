import requests,re,json,datetime

# 本脚本参考以下页面
# https://aptos.dev/guides/system-integrators-guide

# 以下URL由https://explorer.aptoslabs.com/account/0x6c8a3474cb49202515d121fea0f3217d303e41f6bdc43e615f1cd90855118089?network=premainnet
# 通过查找resource文件，预览文件获取得到
url= "https://premainnet.aptosdev.com/v1/accounts/0x6c8a3474cb49202515d121fea0f3217d303e41f6bdc43e615f1cd90855118089/resources"

headers = {"Content-Type": "application/json",
           "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
           }

response = requests.request("GET", url, headers=headers).text

response_dict = json.loads(response)

# print("当前时间：{}".format(datetime.datetime.now()))
# print("APTOS钱包地址：0x6c8a3474cb49202515d121fea0f3217d303e41f6bdc43e615f1cd90855118089")
# print("当前余额：{}".format(response_dict[0]['data']['active']['value']))


time_now = "当前时间： " + str(datetime.datetime.now())
aptos_address = "APTOS钱包地址： 0x6c8a3474cb49202515d121fea0f3217d303e41f6bdc43e615f1cd90855118089"
balance_remaining = "当前余额：" + response_dict[0]['data']['active']['value']
with open('npool_aptos_balance_remaining.txt','w',encoding='utf-8') as f:
    f.write(time_now + "\n")
    f.write(aptos_address + "\n")
    f.write(balance_remaining + "\n")
