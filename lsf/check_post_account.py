import requests,json
import time
from lxml import etree
import send_mail_with_attachment
from pathlib import *
import logging

#LOG_FILE=Path.cwd()/'check_account.log'
LOG_FILE=Path('/root/check_post_account/check_account.log')
logger = logging.getLogger('test')
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(level=logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# 用于爬取指定账号的POST账户余额

BASE_URL='https://filfox.info/zh/address/'

headers = {
    'Connection': 'keep-alive',
    # 'Host': 'api.filscan.io:8700',
    # 'Origin': 'https://filfox.info',
    # 'Referer': 'https://filfox.info',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Mobile Safari/537.36 Edg/102.0.1245.44',
    'Content-Type':"application/json;charset=UTF-8"
}

#ACCOUNT_INFO=Path.cwd()/'account.info'
ACCOUNT_INFO=Path('/root/check_post_account/account.info')
def get_post_account():
    logger.info(f'信息文件：{ACCOUNT_INFO}')
    with open(ACCOUNT_INFO,'r',encoding='utf-8') as f:
        line=f.readline()
        while line:
            # print(line.split("\t"))
            NODE_ID=line.split("\t")[0]
            PROPERTY_RIGHT=line.split("\t")[1]
            WALLET_ADDRESS=line.split("\t")[2].rstrip('\n')
            # print(BASE_URL+WALLET_ADDRESS)
            URL=BASE_URL+WALLET_ADDRESS
            logger.info(f'checking {NODE_ID} {PROPERTY_RIGHT} {WALLET_ADDRESS}')
            try:
                html = requests.get(URL, headers=headers).text
                # print(html)
                tree = etree.HTML(html, etree.HTMLParser())
                POST_BALANCE=tree.xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div/dl[4]/dd/text()')
                POST_BALANCE=float(str(POST_BALANCE[0]).replace('FIL','').strip())
                # print(POST_BALANCE)
                if 20 > POST_BALANCE:
                    # print(NODE_ID,PROPERTY_RIGHT,WALLET_ADDRESS,'余额不足告警，当前余额：',POST_BALANCE)
                    send_mail_with_attachment.MAIL_CONTENT=send_mail_with_attachment.MAIL_CONTENT +  str(NODE_ID) + str(PROPERTY_RIGHT) + str(WALLET_ADDRESS) +'余额不足告警，当前余额：'+ str(POST_BALANCE) + '\n'
                    logger.info(str(NODE_ID) + str(PROPERTY_RIGHT) + str(WALLET_ADDRESS) +'余额不足告警，当前余额：'+ str(POST_BALANCE) )


            except Exception as e:
                print(e)


            # //*[@id="__layout"]/div/div[1]/div[1]/div[2]/div/dl[4]/dd
            # result_json = json.loads(result)
            # print(result_json)
            line=f.readline()
            time.sleep(5)

def send_mail():
    # print(send_mail_with_attachment.MAIL_CONTENT)
    send_mail_with_attachment.mail_content(send_mail_with_attachment.MAIL_CONTENT)
    send_mail_with_attachment.send_mail()
    logger.info(f'告警邮件已发送,收件人为：{send_mail_with_attachment.receivers}')


if __name__ == '__main__':
    logger.info('starting check....')
    get_post_account()
    send_mail()


