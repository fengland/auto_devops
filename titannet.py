import requests,json,time,datetime,csv
import send_mail_with_attachment
from pathlib import *
import logging,os,time
from lxml import etree
from lxml import html


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#os.chdir(os.path.dirname(sys.argv[0]))
LOG_FILE=Path.cwd()/'titanet.log'
#LOG_FILE=Path('/root/check_post_account/check_account.log')
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

#Output_statistics_url="https://api.filutils.com/api/v2/miner/f01146045/mining-data"
BASE_URL="https://testnet.titan.explorers.guru/validator/titanvaloper1rjlk6ym8xpafk6vtjreaxx4hmmquyqfmvvyqq8"


# NODE_NO="f01146045"
# url=base_url+NODE_NO
headers = {
    'Connection': 'keep-alive',
    #'Host': 'api.filscan.io:8700',
    #'Origin': 'https://filscan.io',
    #'Referer': 'https://filscan.io/',
    # 'Host': "api-v2.filscan.io",
    # 'Origin:': 'api-v2.filscan.io',
    # 'Refer': 'https://filscan.io/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Mobile Safari/537.36 Edg/102.0.1245.44',
    'Content-Type': "application/json;charset=UTF-8"
}



def titan():

    response=requests.get(BASE_URL,headers=headers)
    tree=html.fromstring(response.content)
    # 素尾的/text()是加上去的，如果不加变量值显示成<Element p at 0x1faeb5fa0d0>
    elements=tree.xpath('//*[@id="__next"]/div[2]/div[1]/div[2]/div[2]/div[1]/p[1]/text()')
    print(elements[0])
    if elements[0] == "Active":
        print("状态正常")
    else:
        # print("状态异常")
        mail.MAIL_CONTENT = mail.MAIL_CONTENT + f"{BASE_URL}" +"\t"+  f"{elements[0]}" + "\n"
        print(mail.MAIL_CONTENT)



if __name__ == '__main__':
    logger.info("程序开始执行")

    receivers=['jiankong@npool.com']
    mail = send_mail_with_attachment.SendMail(receivers)
    titan()

    print(f"邮件正文长度：{len(mail.MAIL_CONTENT)}")
    print(mail.MAIL_CONTENT)
    if len(mail.MAIL_CONTENT) > 0:
        print("aaaaa"*10)
        logger.debug(f"告警内容：{mail.MAIL_CONTENT}")
        print(len(mail.MAIL_CONTENT))
        mail.subject='TITANNET ALERT'
        print(mail.receivers)
        mail.mail_subject("TITANNET ALERT")
        mail.MAIL_CONTENT = mail.MAIL_CONTENT +  """
TITANNET STATUS DOWN
        """
        mail.mail_content(mail.MAIL_CONTENT)
        logger.info(f"开始发送告警邮件，收件人：{receivers}")

        mail.send_mail()
        logger.info("邮件已发送")
