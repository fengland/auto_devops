import requests
import json

url = "https://www.antpool.com/auth/v3/observer/api/hash/query?accessKey=tpsQqkJYc9o1F6F4hKoY&coinType=BTC&observerUserId=KJDETH006"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
data = json.loads(response.text)
# print("JSON数据:", json.dumps(data, indent=4, ensure_ascii=False))
print("矿工号：", data.get("data").get("userId"))
print("nickName：", data.get("data").get("nickName"))
print("10分钟算力：", data.get("data").get("hsNow"), data.get("data").get("hsNowUnit"))
print("24小时算力：", data.get("data").get("hsLast1D"), data.get("data").get("hsLast1DUnit"))
print("矿工总数：", data.get("data").get("totalWorkerNum"))
print("在线矿工数：", data.get("data").get("onlineWorkerNum"))
print("掉线矿工数：", data.get("data").get("offlineWorkerNum"))
print("disableWorkerNum：", data.get("data").get("disableWorkerNum"))


url1="https://www.antpool.com/auth/v3/observer/api/earnings/query?accessKey=tpsQqkJYc9o1F6F4hKoY&coinType=BTC&observerUserId=KJDETH006"
payload={}
headers = {}

response = requests.request("GET", url1, headers=headers, data=payload)
data = json.loads(response.text)
# print("JSON数据:", json.dumps(data, indent=4, ensure_ascii=False))
print("币种：", data.get("data").get("coin"))
print("昨日收益：", data.get("data").get("earningsYesterday"))
print("未支付：", data.get("data").get("earningsNoPay"))
print("历史总收益：", data.get("data").get("earningsTotal"))
