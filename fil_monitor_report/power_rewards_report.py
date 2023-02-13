import requests,json,time,datetime,csv
import send_mail_with_attachment
import vars,utils
from pathlib import *
import logging,os


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#os.chdir(os.path.dirname(sys.argv[0]))
LOG_FILE=Path.cwd()/'power_rewards_report.log'
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


try:
    def get_extra_datas(url,node_no,duration):
        extra_datas = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "filscan.FilscanStatisticalIndicatorsUnite",
            "params": [
                [
                    f"{node_no}"
                ],
                f"{duration}",
                1
            ]
        }
        result = requests.post(url, headers=headers, data=json.dumps(extra_datas)).text
        time.sleep(1)
        result_json = json.loads(result)
        return result_json
except Exception as e:
    logger.debug(e)
    print(e)


try:
    def get_24h_info(url):
        logger.info(f"开始获取node:{node_no}基础信息")
        result = requests.post(url, headers=headers, data=json.dumps(basic_datas)).text
        result_json = json.loads(result)
        # print(result_json)
        quality_adjust_power=int(result_json['result']['extra']['quality_adjust_power'])
        # print(quality_adjust_power)
        human_quality_adjust_power=utils.bytes2human(quality_adjust_power)
        # print(human_quality_adjust_power)

        fault_sector_count = result_json['result']['extra']['fault_sector_count']
        # print(fault_sector_count)

        mail.MAIL_CONTENT = mail.MAIL_CONTENT + "节点号：" + f"{node_no}" + "\t" + "有效算力：" + f"{human_quality_adjust_power}"

        # print(mail.MAIL_CONTENT)
        logger.info(f"节点号：{node_no}基础信息获取完成")
        logger.info(f"开始获取节点号：{node_no} extra信息")
        result_json = get_extra_datas(url,node_no, "24h")
        # print(result_json)
        power_incr = utils.bytes2human(int(result_json['result']['power_incr']))
        blocks = result_json['result']['blocks']
        blocks_rewards=result_json['result']['blocks_rewards']
        # print(round(int(blocks_rewards) / 10 ** 18, 4))
        # print('%.4f'%(int(blocks_rewards)/10**18))
        blocks_rewards = '%.4f'%(int(blocks_rewards)/10**18)


        lucky = result_json['result']['lucky'][0:4]
        # mail.MAIL_CONTENT = mail.MAIL_CONTENT+"\t\t" + "24H算力增量："+ str(power_incr) + "\t\t" + "24H出块数：" + str(blocks) + "\t\t"+"出块奖励：" + str(int(blocks_rewards)) +"扇区错误："+f"{fault_sector_count}"+ "\t" + "24h幸运值：" + f"{lucky}"
        mail.MAIL_CONTENT = mail.MAIL_CONTENT + "\t\t" + "24H算力增量：" + str(power_incr) + "\t\t" + "24H出块数：" + str(
            blocks) + "\t\t" + "出块奖励：" + str(
            blocks_rewards) + "\n" + "错误区块："+ f"{fault_sector_count}"+"\n\t\t" +"24h幸运值：" + f"{lucky}"
        # print(mail.MAIL_CONTENT)

        result_json = get_extra_datas(url, node_no, "1w")
        lucky = result_json['result']['lucky'][0:4]
        mail.MAIL_CONTENT = mail.MAIL_CONTENT + "\t" + "1w幸运值：" + f"{lucky}"

        result_json = get_extra_datas(url, node_no, "1m")
        lucky = result_json['result']['lucky'][0:4]
        mail.MAIL_CONTENT = mail.MAIL_CONTENT + "\t" + "1m幸运值：" + f"{lucky}"

        result_json = get_extra_datas(url, node_no, "1y")
        lucky = result_json['result']['lucky'][0:4]
        mail.MAIL_CONTENT = mail.MAIL_CONTENT + "\t" + "1y幸运值：" + f"{lucky}"
        # mail.MAIL_CONTENT = mail.MAIL_CONTENT + "\n"
        logger.info(f"节点号：{node_no} extra信息获取完成")
        print(mail.MAIL_CONTENT)
except Exception as e:
    logger.debug(e)
    print(e)


if __name__ == '__main__':
    logger.info("程序开始执行")

    receivers=['jiankong@npool.com','wangxufeng@npool.com']
    mail = send_mail_with_attachment.SendMail(receivers)
    for node_no in vars.ALL_NODE_NO:
        # node_no = "f079426"
        url=base_url+ node_no

        basic_datas = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "filscan.FilscanActorById",
            "params": [
                f"{node_no}"
            ]
        }

        try:
            logger.info(f"开始获取node:{node_no}")
            get_24h_info(url)
            mail.MAIL_CONTENT = mail.MAIL_CONTENT + "\n"
            logger.info(f"获取node:{node_no}完成")
            time.sleep(1)
        except Exception as e:
            logger.debug(e)
            print(e)
        # break


    # print(len(mail.MAIL_CONTENT))
    mail.subject='FIL STATUS REPORT'
    # print(mail.receivers)
    mail.mail_subject("FIL STATUS REPORT DAILY")
    mail.mail_content(mail.MAIL_CONTENT)
    logger.info(f"开始发送邮件，收件人：{receivers}")
    mail.send_mail()
    logger.info(f"发送邮件完成")
    logger.info("程序执行结束")

