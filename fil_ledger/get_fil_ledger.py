# _*_ coding : utf-8 _*_
# @Time : 025, Oct 25, 2022 8:20
# @Author : feng_land
# @File : get_fi_release
# @Project : test_project
import requests,json,time,datetime,csv
#from datetime import datetime


#url = "https://filfox.info/api/v1/address/f023152/blocks?pageSize=100&page=0"
#url = f"https://filfox.info/api/v1/address/{node_id}/blocks?pageSize=100&page={page}"

def today_release(reward, days):
    if days == 0:
        #print(reward*0.25)
        return reward*0.25
    elif 0 < days and days <=180:
        #print((reward * 0.25) + (reward * 0.75)/180*days)
        return (reward * 0.25) + (reward * 0.75)/180*days
    else:
        #print("超过180天，已释放完毕")
        return "超过180天，已释放完毕"

def get_one_page(node_id,page):
    url = f"https://filfox.info/api/v1/address/{node_id}/blocks?pageSize=100&page={page}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Mobile Safari/537.36 Edg/102.0.1245.44'
    }
    result = requests.get(url, headers=headers).text
    result_json = json.loads(result)

    for block  in result_json['blocks']:
        #print(block)
        now = time.time()
        reward_days = int((now - block['timestamp'])//86400)
        if reward_days > 180:
            print("超过180天，退出")
            global d180
            d180 = 1
            break
        print(block['height'],block['cid'],float(block['reward'])/(10**18),datetime.datetime.fromtimestamp(block['timestamp']),reward_days,today_release(float(block['reward'])/(10**18),reward_days))
        line = [block['height'],block['cid'],float(block['reward'])/(10**18),datetime.datetime.fromtimestamp(block['timestamp']),reward_days,today_release(float(block['reward'])/(10**18),reward_days)]
        with open(csv_file_name,'a',encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(line)



if __name__ == '__main__':
    #page = 0
    node_ids = ["f01735897","f0422266","f01211859","f0418086","f0832131","f01146045","f0159883","f023152","f071664","f01876488","f0111584","f01713152","f079426","f0134006","f0159632","f0705704","f079815"]
    head_list = ["区块高度", "区块ID", "奖励", "时间", "区块天数", "已释放"]


    for node_id in node_ids:
        csv_file_name = f'{node_id}-{datetime.date.today()}.csv'
        with open(csv_file_name, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(head_list)
        for page in range(50):
            d180 = 0
            get_one_page(node_id,page)
            if d180 == 1:
                break
