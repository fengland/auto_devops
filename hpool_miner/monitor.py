import requests,json
from pathlib import Path
import send_mail_with_attachment


# URL="https://www.hpool.in/api/pool/miner?status=all&type=aleo&count=20&page=1"


__dir__: Path = Path(__file__).parent
LOG_FILE=__dir__ / "hpool_aleo.log"
RESULT_FILE=__dir__ / "hpool_aleo.csv"
result = {}
line = []


BASE_URL="https://www.hpool.in/api/hpool/miner"

headers = {
    'Connection': 'keep-alive',
    # 'Host': 'api.filscan.io:8700',
    # 'Origin': 'https://filfox.info',
    # 'Referer': 'https://filfox.info',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Mobile Safari/537.36 Edg/102.0.1245.44',
    'Content-Type':"application/json;charset=UTF-8"
}

def get_one_page(owner,page,api_key,secret_key):
    data = {
        "api_key": f"{api_key}",
        "secret_key": f"{secret_key}",
        "type": "ironfish",
        "page": page,
        "count": 50
    }

    result = requests.post(BASE_URL, headers=headers, data=json.dumps(data)).text
    result_json = json.loads(result)
    print(result_json)
    for item in result_json['data']['list']:
        if len(item) <= 0:
            break
        # elif item['online'] == False:
            # print(f"产权：{owner} 主机：{item['miner_name']}  离线了，请尽快处理")
             # send_mail_with_attachment.MAIL_CONTENT = send_mail_with_attachment.MAIL_CONTENT + f"产权：{owner}  主机：{item['miner_name']}  离线了，请尽快处理\n"
        else:
            print(item)
            # pass


def main():
    with open(__dir__ / "tenant.list", 'r', encoding='utf-8') as f:
        line = f.readline()
        title = line.split()
        # print(title)
        while line:
            line = f.readline().split()
            if line:
                print(line)
                owner = line[0]
                email = line[1]
                api_key = line[2]
                secret_key = line[3]
                for i in range(1,20):
                    get_one_page(owner,i,api_key,secret_key)


    if len(send_mail_with_attachment.MAIL_CONTENT) > 10 :
        # print(send_mail_with_attachment.MAIL_CONTENT)
        # print(len(send_mail_with_attachment.MAIL_CONTENT))
        send_mail_with_attachment.mail_content(send_mail_with_attachment.MAIL_CONTENT)
        send_mail_with_attachment.send_mail()

if __name__ == '__main__':
    main()
