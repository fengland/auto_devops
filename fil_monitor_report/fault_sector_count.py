import requests,json,time,datetime,csv
import send_mail_with_attachment
import vars
from pathlib import *
import logging,os,time


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#os.chdir(os.path.dirname(sys.argv[0]))
LOG_FILE=Path.cwd()/'fault_sector_count.log'
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

#url = "https://api.filscan.io:8700/rpc/v1"
base_url="https://api.filscan.io:8700/rpc/v1?0="
#url = "https://api.filscan.io:8700/rpc/v1?0[]=f07824&1=1w&2=1"


# NODE_NO="f01146045"
# url=base_url+NODE_NO
headers = {
    'Connection': 'keep-alive',
    'Host': 'api.filscan.io:8700',
    'Origin': 'https://filscan.io',
    'Referer': 'https://filscan.io/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Mobile Safari/537.36 Edg/102.0.1245.44',
    'Content-Type':"application/json;charset=UTF-8"
}





def get_fault_sector_count(url):
    result = requests.post(url, headers=headers, data=json.dumps(basic_datas)).text
    result_json = json.loads(result)
    fault_sector_count = result_json['result']['extra']['fault_sector_count']



    if fault_sector_count > 0:
        mail.MAIL_CONTENT = mail.MAIL_CONTENT + "节点号：" + str(node_no) +  "\t" + "扇区错误数量：" + str(fault_sector_count) + "\n"

        print(mail.MAIL_CONTENT)




if __name__ == '__main__':
    logger.info("程序开始执行")

    receivers=['yangxuedong@npool.com','project@npool.com','jiankong@npool.com','77ab2a93-fbfe-4ecc-91ff-bd55ccf42a48@fwalert.com']
    mail = send_mail_with_attachment.SendMail(receivers)
    for node_no in vars.ALL_NODE_NO:
        url=base_url+node_no

        basic_datas = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "filscan.FilscanActorById",
            "params": [
                f"{node_no}"
            ]
        }
        print(f"getting node:{node_no}")
        logger.info(f"开始检测节点:{node_no}")
        get_fault_sector_count(url)
        time.sleep(1)
        logger.info(f"检测节点号：{node_no}结束")

    print(f"邮件正文长度：{len(mail.MAIL_CONTENT)}")
    if len(mail.MAIL_CONTENT) > 0:
        print("aaaaa"*10)
        logger.debug(f"告警内容：{mail.MAIL_CONTENT}")
        print(len(mail.MAIL_CONTENT))
        mail.subject='FIL fault_sector_count ALERT'
        print(mail.receivers)
        mail.mail_subject("FIL fault_sector_count ALERT")
        mail.MAIL_CONTENT = mail.MAIL_CONTENT +  """
        该告警为掉算力告警，如看到此邮件，请截图发在微信群，并艾特唐红，
        如果唐红未回复信息，请拔打手机号：13612203199 ，联系kk
        """
        mail.mail_content(mail.MAIL_CONTENT)
        logger.info(f"开始发送告警邮件，收件人：{receivers}")

        mail.send_mail()
        logger.info("邮件已发送")

