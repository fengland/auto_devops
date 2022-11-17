import requests,json,time,datetime,csv
import send_mail_with_attachment

url = "https://api.filscan.io:8700/rpc/v1"
headers = {
    'Connection': 'keep-alive',
    'Host': 'api.filscan.io:8700',
    'Origin': 'https://filscan.io',
    'Referer': 'https://filscan.io/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Mobile Safari/537.36 Edg/102.0.1245.44',
    'Content-Type':"application/json;charset=UTF-8"
}

def get_node_info(node_id):
    node_id = node_id
    row = []

    row.append(time.strftime("%Y-%m-%d", time.localtime()))
    row.append(time.strftime("%H:%M:%S", time.localtime()))

    basic_datas = {
        "id": 1,
        "jsonrpc": "2.0",
        "params": [
            f"{node_id}"
        ],
        "method": "filscan.FilscanActorById"
    }

    result = requests.post(url, headers=headers, data=json.dumps(basic_datas)).text
    result_json = json.loads(result)

    # print(result_json['result']['basic']['actor'])
    # print(result_json['result']['basic']['balance'])
    # print(result_json['result']['basic']['block_count'])
    # print(result_json['result']['extra']['available_balance'])
    # print(result_json['result']['extra']['addresses']['worker_address'])
    worker_address = result_json['result']['extra']['addresses']['worker_address']
    quality_adjust_power = float(result_json['result']['extra']['quality_adjust_power']) / 1024 / 1024 / 1024 / 1024
    available_balance = result_json['result']['extra']['available_balance']
    block_count = result_json['result']['basic']['block_count']

    statistics_datas = {
        "id": 1,
        "jsonrpc": "2.0",
        "params": [
            [
                f"{node_id}"
            ],
            "24h",
            1
        ],
        "method": "filscan.FilscanStatisticalIndicatorsUnite"
    }

    result = requests.post(url, headers=headers, data=json.dumps(statistics_datas)).text
    result_json = json.loads(result)

    # print(result_json['result']['power_incr'])
    # print(result_json['result']['power_ratio'])
    # print(result_json['result']['sector_incr'])
    # print(result_json['result']['lucky'])
    lucky = result_json['result']['lucky']
    power_incr = result_json['result']['power_incr']
    power_ratio = result_json['result']['power_ratio']
    sector_incr = result_json['result']['sector_incr']

    row.append(float(power_incr)/1024/1024/1024/1024)
    row.append(float(power_ratio)/1024/1024/1024/1024)
    row.append(float(sector_incr)/1024/1024/1024/1024)

    row.append(quality_adjust_power)
    row.append(available_balance)

    worker_datas = {
        "id": 1,
        "jsonrpc": "2.0",
        "params": [
            f"{worker_address}",
            # "f3s7jzjakywsb24xov7l4tnq4w6fidd7at7vde726qy7glyfapza6k7467jrnf6ultkm3xeutpszo6fvxj4avq",
            "24h"
        ],
        "method": "filscan.GeneralAddressBalanceTrend"
    }

    result = requests.post(url, headers=headers, data=json.dumps(worker_datas)).text
    result_json = json.loads(result)

    # print(result_json)
    # print(float(result_json['result'][0]['balance'])/(10**18))
    worker_balance = float(result_json['result'][0]['balance']) / (10 ** 18)
    row.append(worker_balance)
    row.append(block_count)
    row.append(lucky)
    print(row)

    with open(f"/root/lsf_fil_report/{node_id}.csv", 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)


if __name__ == '__main__':
    node_ids=['f01876488','f01953944','f01953959','f079815']
    for node_id in node_ids:
        print(f"getting node {node_id}")
        get_node_info(node_id)
        time.sleep(5)

    for node_id in node_ids:
        send_mail_with_attachment.add_attachment(f"/root/lsf_fil_report/{node_id}.csv")
    send_mail_with_attachment.send_mail()
