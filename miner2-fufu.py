import requests
from requests.auth import HTTPDigestAuth
from requests.exceptions import RequestException
import urllib3
import pickle
import json
import pytz
import time
from datetime import datetime
import os



# 本脚本仅用于fufu固件
# 禁用SSL警告（如果使用HTTPS）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def login_and_check_status(miner_url, username, password):
    """
    使用Digest认证登录矿机管理界面并检查状态码
    
    Args:
        miner_url (str): 矿机管理界面的URL
        username (str): 登录用户名
        password (str): 登录密码
    
    Returns:
        tuple: (是否登录成功, 状态码, 响应内容)
    """
    # 创建会话对象
    session = requests.Session()
    
    try:
        # 使用Digest认证
        print("尝试使用Digest认证...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        
        response = session.get(
            miner_url,
            auth=HTTPDigestAuth(username, password),
            headers=headers,
            verify=False  # 如果是HTTPS且证书有问题，禁用验证
        )
        
        if response.status_code == 200:
            print("登录成功！")
            return True, response.status_code, response.text
        else:
            print(f"登录失败，状态码: {response.status_code}")
            return False, response.status_code, response.text
        
            
    except RequestException as e:
        print(f"请求出错: {str(e)}")
        return False, None, None


def get_miner_summary(url, username, password):
    # url=f"{MINER_URL}/cgi-bin/get_system_info.cgi"
    # print(f"\n尝试访问: {url}")
    success, status_code, content = login_and_check_status(url, username, password)
    print(success)
    print(f"状态码: {status_code}")
    # print("响应内容预览:", content[:500] if content else "无响应内容")
    # 获取content的json格式
    if content:
        try:
            data = json.loads(content)
            # print("JSON数据:", data)
            # print("JSON数据:", json.dumps(data, indent=4, ensure_ascii=False))
            print("矿机类型:", data.get("minertype"))
            print("网络类型:", data.get("nettype", []))
            print("网络设备:", data.get("netdevice"))
            print("MAC地址:", data.get("macaddr"))
            print("主机名:", data.get("hostname"))
            print("IP地址:", data.get("ipaddress"))
            print("memory_total:", data.get("memory_total"))
            print("memory_used:", data.get("memory_used"))
            print("memory_free:", data.get("memory_free"))
            print("系统类型:", data.get("system_mode"))
            print("ant_hwv:", data.get("ant_hwv"))
            print("system_kernel_version:", data.get("system_kernel_version"))
            print("system_filesystem_version:", data.get("system_filesystem_version"))  
            print("firmware_type:", data.get("firmware_type"))
            print("cgminer_version:", data.get("cgminer_version"))
        except json.JSONDecodeError:
            print("响应内容不是有效的JSON格式")



def get_miner_stats(url, username, password):
    # url=f"{MINER_URL}/cgi-bin/get_system_info.cgi"
    # print(f"\n尝试访问: {url}")
    success, status_code, content = login_and_check_status(url, username, password)
    print(success)
    print(f"状态码: {status_code}")
    # print("响应内容预览:", content[:500] if content else "无响应内容")
    # 获取content的json格式
    if content:
        try:
            data = json.loads(content)
            # print("JSON数据:", data)
            # print("JSON数据:", json.dumps(data, indent=4, ensure_ascii=False))
            print("STATUS:", data.get("STATUS")[0].get("STATUS"))
            print("Code:", data.get("STATUS")[0].get("Code"))
            print("Msg:", data.get("STATUS")[0].get("Msg"))
            print("Description:", data.get("STATUS")[0].get("Description"))
            
            print("CGMINER:", data.get("STATS")[0].get("CGMINER"))
            print("Miner:", data.get("STATS")[0].get("Miner"))
            print("CompileTime:", data.get("STATS")[0].get("CompileTime"))
            print("Type:", data.get("STATS")[0].get("Type"))
            
            print("STATS:", data.get("STATS")[1].get("STATS"))
            print("ID:", data.get("STATS")[1].get("ID"))
            print("Elapsed:", data.get("STATS")[1].get("Elapsed"))
            print("Calls:", data.get("STATS")[1].get("Calls"))
            print("Wait:", data.get("STATS")[1].get("Wait"))
            print("Max:", data.get("STATS")[1].get("Max"))
            print("Min:", data.get("STATS")[1].get("Min"))
            print("GHS 5s:", data.get("STATS")[1].get("GHS 5s"))
            print("GHS av:", data.get("STATS")[1].get("GHS av"))
            print("rate_30m:", data.get("STATS")[1].get("rate_30m"))
            print("Mode:", data.get("STATS")[1].get("Mode"))
            print("miner_count:", data.get("STATS")[1].get("miner_count"))
            print("frequency:", data.get("STATS")[1].get("frequency"))
            print("fan_num:", data.get("STATS")[1].get("fan_num"))
            print("fan1:", data.get("STATS")[1].get("fan1"))
            print("fan2:", data.get("STATS")[1].get("fan2"))
            print("fan3:", data.get("STATS")[1].get("fan3"))
            print("fan4:", data.get("STATS")[1].get("fan4"))
            print("temp_num:", data.get("STATS")[1].get("temp_num"))
            print("temp1:", data.get("STATS")[1].get("temp1")) 
            print("temp2_1:", data.get("STATS")[1].get("temp2_1"))
            print("temp2:", data.get("STATS")[1].get("temp2"))
            print("temp2_2:", data.get("STATS")[1].get("temp2_2"))
            print("temp3:", data.get("STATS")[1].get("temp3"))
            print("temp2_3:", data.get("STATS")[1].get("temp2_3"))
            print("temp_pcb1:", data.get("STATS")[1].get("temp_pcb1"))
            print("temp_pcb2:", data.get("STATS")[1].get("temp_pcb2"))
            print("temp_pcb3:", data.get("STATS")[1].get("temp_pcb3"))
            print("temp_pcb4:", data.get("STATS")[1].get("temp_pcb4"))
            print("temp_chip1:", data.get("STATS")[1].get("temp_chip1"))
            print("temp_chip2:", data.get("STATS")[1].get("temp_chip2"))
            print("temp_chip3:", data.get("STATS")[1].get("temp_chip3"))
            print("temp_chip4:", data.get("STATS")[1].get("temp_chip4"))
            print("temp_pic1:", data.get("STATS")[1].get("temp_pic1"))
            print("temp_pic2:", data.get("STATS")[1].get("temp_pic2"))
            print("temp_pic3:", data.get("STATS")[1].get("temp_pic3"))
            print("temp_pic4:", data.get("STATS")[1].get("temp_pic4"))
            print("total_rateideal:", data.get("STATS")[1].get("total_rateideal"))
            print("rate_unit:", data.get("STATS")[1].get("rate_unit"))
            print("total_freqavg:", data.get("STATS")[1].get("total_freqavg"))
            print("total_acn:", data.get("STATS")[1].get("total_acn"))
            print("total rate:", data.get("STATS")[1].get("total rate"))
            print("temp_max:", data.get("STATS")[1].get("temp_max"))
            print("no_matching_work:", data.get("STATS")[1].get("no_matching_work"))
            print("chain_acn1:", data.get("STATS")[1].get("chain_acn1"))
            print("chain_acn2:", data.get("STATS")[1].get("chain_acn2"))
            print("chain_acn3:", data.get("STATS")[1].get("chain_acn3"))
            print("chain_acn4:", data.get("STATS")[1].get("chain_acn4"))
            print("chain_acs1:", data.get("STATS")[1].get("chain_acs1"))
            print("chain_acs2:", data.get("STATS")[1].get("chain_acs2"))
            print("chain_acs3:", data.get("STATS")[1].get("chain_acs3"))
            print("chain_acs4:", data.get("STATS")[1].get("chain_acs4"))
            print("chain_hw1:", data.get("STATS")[1].get("chain_hw1"))
            print("chain_hw2:", data.get("STATS")[1].get("chain_hw2"))
            print("chain_hw3:", data.get("STATS")[1].get("chain_hw3"))
            print("chain_hw4:", data.get("STATS")[1].get("chain_hw4"))
            print("chain_rate1:", data.get("STATS")[1].get("chain_rate1"))
            print("chain_rate2:", data.get("STATS")[1].get("chain_rate2"))
            print("chain_rate3:", data.get("STATS")[1].get("chain_rate3"))
            print("chain_rate4:", data.get("STATS")[1].get("chain_rate4"))
            print("freq1:", data.get("STATS")[1].get("freq1")) 
            print("freq2:", data.get("STATS")[1].get("freq2"))
            print("freq3:", data.get("STATS")[1].get("freq3"))
            print("freq4:", data.get("STATS")[1].get("freq4"))
            print("miner_version:", data.get("STATS")[1].get("miner_version"))
            print("miner_id:", data.get("STATS")[1].get("miner_id"))



        except json.JSONDecodeError:
            print("响应内容不是有效的JSON格式")






def get_network_info(url, username, password):
    # url=f"{MINER_URL}/cgi-bin/get_system_info.cgi"
    # print(f"\n尝试访问: {url}")
    success, status_code, content = login_and_check_status(url, username, password)
    print(success)
    print(f"状态码: {status_code}")
    # print("响应内容预览:", content[:500] if content else "无响应内容")
    # 获取content的json格式
    if content:
        try:
            data = json.loads(content)
            # print("JSON数据:", data)
            print("JSON数据:", json.dumps(data, indent=4, ensure_ascii=False))
            print("nettype:", data.get("nettype"))
            print("netdevice:", data.get("netdevice"))
            print("macaddr:", data.get("macaddr"))
            print("ipaddress:", data.get("ipaddress"))
            print("netmask:", data.get("netmask"))
            print("conf_nettype:", data.get("conf_nettype"))
            print("conf_hostname:", data.get("conf_hostname"))
            print("conf_ipaddress:", data.get("conf_ipaddress"))
            print("conf_netmask:", data.get("conf_netmask"))
            print("conf_gateway:", data.get("conf_gateway"))
            print("conf_dnsservers:", data.get("conf_dnsservers"))

        except json.JSONDecodeError:
            print("响应内容不是有效的JSON格式")


def get_system_info(url, username, password):
    # url=f"{MINER_URL}/cgi-bin/get_system_info.cgi"
    # print(f"\n尝试访问: {url}")
    success, status_code, content = login_and_check_status(url, username, password)
    print(success)
    print(f"状态码: {status_code}")
    # print("响应内容预览:", content[:500] if content else "无响应内容")
    # 获取content的json格式
    if content:
        try:
            data = json.loads(content)
            #  print("JSON数据:", data)
            # print("JSON数据:", json.dumps(data, indent=4, ensure_ascii=False))
            print("矿机类型:", data.get("minertype"))
            print("网络类型:", data.get("nettype", []))
            print("网络设备:", data.get("netdevice"))
            print("MAC地址:", data.get("macaddr"))
            print("主机名:", data.get("hostname"))
            print("IP地址:", data.get("ipaddress"))
            print("系统类型:", data.get("system_mode"))
            print("system_kernel_version:", data.get("system_kernel_version"))
            print("system_filesystem_version:", data.get("system_filesystem_version"))
            print("firmware_type:", data.get("firmware_type"))
            print("serinum:", data.get("serinum"))
        except json.JSONDecodeError:
            print("响应内容不是有效的JSON格式")




def get_miner_pools(miner_url, username, password):
    # url=f"{MINER_URL}/cgi-bin/get_system_info.cgi"
    # print(f"\n尝试访问: {url}")
    success, status_code, content = login_and_check_status(url, username, password)
    print(success)
    print(f"状态码: {status_code}")
    # print("响应内容预览:", content[:500] if content else "无响应内容")
    # 获取content的json格式
    if content:
        try:
            data = json.loads(content)
            #  print("JSON数据:", data)
            # print("JSON数据:", json.dumps(data, indent=4, ensure_ascii=False))
            print(data.get("STATUS")[0].get("When"))

            print("状态：", data.get("STATUS")[0].get("STATUS"))
            # utc_time = datetime.fromtimestamp(data.get("STATUS").get("When"), tz=pytz.utc)
            utc_time = datetime.fromtimestamp(data.get("STATUS")[0].get("When"), tz=pytz.utc)

            beijing_time = utc_time.astimezone(beijing_tz)
            print("当前时间：", data.get("STATUS")[0].get("When"))
            print("UTC时间：", utc_time)
            print("北京时间：", beijing_time)
            print("Msg：", data.get("STATUS")[0].get("Msg"))
            print("Description：", data.get("STATUS")[0].get("Description"))


            for i in range(len(data.get("POOLS"))):
                print("#"*30+f"矿池{i}信息"+"#"*30)
                print(f"矿池{i} 编号:", data.get("POOLS")[i].get("POOL"))
                print(f"矿池{i} url:", data.get("POOLS")[i].get("URL"))
                print(f"矿池{i} Status:", data.get("POOLS")[i].get("Status"))
                print(f"矿池{i} Priority:", data.get("POOLS")[i].get("Priority"))
                print(f"矿池{i} Quota:", data.get("POOLS")[i].get("Quota"))
                print(f"矿池{i} Long Poll:", data.get("POOLS")[i].get("Long Poll"))
                print(f"矿池{i} Getworks:", data.get("POOLS")[i].get("Getworks"))
                print(f"矿池{i} Accepted:", data.get("POOLS")[i].get("Accepted"))
                print(f"矿池{i} Rejected:", data.get("POOLS")[i].get("Rejected"))
                print(f"矿池{i} Discarded:", data.get("POOLS")[i].get("Discarded"))
                print(f"矿池{i} Stale:", data.get("POOLS")[i].get("Stale"))
                print(f"矿池{i} diff:Get Failures", data.get("POOLS")[i].get("Get Failures"))
                print(f"矿池{i} Remote Failures:", data.get("POOLS")[i].get("Remote Failures"))
                print(f"矿池{i} User:", data.get("POOLS")[i].get("User"))
                print(f"矿池{i} Last Share Time:", data.get("POOLS")[i].get("Last Share Time "))
                print(f"矿池{i} Diff:", data.get("POOLS")[i].get("Diff"))
                print(f"矿池{i} Diff1 Shares:", data.get("POOLS")[i].get("Diff1 Shares"))
                print(f"矿池{i} Proxy Type:", data.get("POOLS")[i].get("Proxy Type"))
                print(f"矿池{i} Proxy:", data.get("POOLS")[i].get("Proxy"))
                print(f"矿池{i} Difficulty Accepted:", data.get("POOLS")[i].get("Difficulty Accepted"))
                print(f"矿池{i} Difficulty Rejected:", data.get("POOLS")[i].get("Difficulty Rejected"))
                print(f"矿池{i} Difficulty Stale:", data.get("POOLS")[i].get("Difficulty Stale"))
                print(f"矿池{i} Last Share Difficulty:", data.get("POOLS")[i].get("Last Share Difficulty"))
                print(f"矿池{i} Has Stratum:", data.get("POOLS")[i].get("Has Stratum"))
                print(f"矿池{i} Stratum Active:", data.get("POOLS")[i].get("Stratum Active"))
                print(f"矿池{i} Stratum URL:", data.get("POOLS")[i].get("Stratum URL"))
                print(f"矿池{i} Has GBT:", data.get("POOLS")[i].get("Has GBT"))    
                print(f"矿池{i} Best Share:", data.get("POOLS")[i].get("Best Share"))
                print(f"矿池{i} Pool Rejected%:", data.get("POOLS")[i].get("Pool Rejected%"))
                print(f"矿池{i} Pool Stale%%:", data.get("POOLS")[i].get("Pool Stale%%"))
        except json.JSONDecodeError:
            print("响应内容不是有效的JSON格式")


def get_Miner_General_Configuration(miner_url, username, password):
    success, status_code, content = login_and_check_status(url, username, password)
    print(success)
    print(f"状态码: {status_code}")
    # print("响应内容预览:", content[:500] if content else "无响应内容")
    # 获取content的json格式
    if content:
        try:
            data = json.loads(content)
            #  print("JSON数据:", data)
            #  print("JSON数据:", json.dumps(data, indent=4, ensure_ascii=False))
            print(data)
            print("bitmain-work-mode：", data.get("bitmain-work-mode"))
            print("bitmain-voltage：", data.get("bitmain-voltage"))
            print("bitmain-ccdelay：", data.get("bitmain-ccdelay"))
            print("bitmain-pwth：", data.get("bitmain-pwth"))
            print("bitmain-ex-hashrate：", data.get("bitmain-ex-hashrate"))

            print("pool0-url：", data.get("pools")[0].get("url"))
            print("pool0-user：", data.get("pools")[0].get("user"))
            print("pool0-pass：", data.get("pools")[0].get("pass"))
            print("pool1-url：", data.get("pools")[1].get("url"))
            print("pool1-user：", data.get("pools")[1].get("user"))
            print("pool1-pass：", data.get("pools")[1].get("pass"))
            print("pool2-url：", data.get("pools")[2].get("url"))
            print("pool2-user：", data.get("pools")[2].get("user"))
            print("pool2-pass：", data.get("pools")[2].get("pass"))
        except json.JSONDecodeError:
            print("响应内容不是有效的JSON格式")

def download_logs(miner_url, username, password):


    if success and status_code == 200:
        host=MINER_URL.split('//')[-1].split('/')[0]  # 得到 "10.1.1.34"
        host_dashed = host.replace('.', '-')  # 得到 "10-1-1-34"
        current_date = time.strftime("%Y-%m-%d")
        # filename = f"{host_dashed}-antminer_log-{current_date}.tar"
        filename = f"{host_dashed}-antminer_log-2026-01-28.tar"

        # 如果文件已存在，先删除它
        try:
            if os.path.exists(filename):
                os.remove(filename)
                print(f"已删除旧文件: {filename}")
        except OSError as e:
            print(f"删除文件失败 {filename}: {e}")
        
        print(f"准备保存日志文件为: {filename}")
        try:
            # 关键：将字符串编码为字节
            with open(filename, 'wb') as f:
                f.write(content.encode('utf-8'))  # 添加 encode()
            print(f"文件已成功保存为: {filename}")
        except Exception as e:
            print(f"文件保存失败: {e}")
    else:
        print(f"下载失败，状态码: {status_code}")


paylod={
  "bitmain-fan-ctrl": False,
  "bitmain-fan-pwm": "100",
  "bitmain-hashrate-percent": "100",
  "miner-mode": 0,
  "pools": [
    {
      "url": "stratum+tcp://ss.antpool.com:3333",
      "user": "KJDTX008.10x1x1x24",
      "pass": ""
    },
    {
      "url": "stratum+tcp://ss.antpool.com:443",
      "user": "KJDTX008.10x1x1x24",
      "pass": ""
    },
    {
      "url": "stratum+tcp://btc.f2pool.com:1314",
      "user": "kjdtx008f2pool.10x1x1x24",
      "pass": ""
    }
  ]
}



def set_miner_config(miner_url, username, password):
    """
    使用Digest认证登录矿机管理界面并检查状态码
    
    Args:
        miner_url (str): 矿机管理界面的URL
        username (str): 登录用户名
        password (str): 登录密码
    
    Returns:
        tuple: (是否登录成功, 状态码, 响应内容)
    """
    # 创建会话对象
    session = requests.Session()
    
    try:
        # 使用Digest认证
        print("尝试使用Digest认证...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        
        # response = session.get(
        #     miner_url,
        #     auth=HTTPDigestAuth(username, password),
        #     headers=headers,
        #     verify=False  # 如果是HTTPS且证书有问题，禁用验证
        # )
        response=session.post(
            miner_url, 
            auth=HTTPDigestAuth(username, password), 
            headers=headers, 
            verify=False,
            json=paylod)
        print(response.text)
        
        if response.status_code == 200:
            print("登录成功！")
            return True, response.status_code, response.text
        else:
            print(f"登录失败，状态码: {response.status_code}")
            return False, response.status_code, response.text
        
            
    except RequestException as e:
        print(f"请求出错: {str(e)}")
        return False, None, None








# 使用示例
if __name__ == "__main__":
    beijing_tz = pytz.timezone('Asia/Shanghai')
    # 配置你的矿机信息
    MINER_URL = "http://172.50.71.31"  # 替换为实际的矿机地址
    USERNAME = "root"  # 矿机通常默认用户名是root
    PASSWORD = "root"  # 替换为实际密码
    
    # 执行登录并检查状态
    success, status_code, content = login_and_check_status(MINER_URL, USERNAME, PASSWORD)

    print(success)
    
    if success:
        print(f"最终状态码: {status_code}")
        # 打印部分响应内容
        # print("响应内容预览:", content[:500] if content else "无响应内容")
    else:
        print("登录失败")
        if content:
            print("错误响应:", content[:500])



    # 获取系统信息
    url=f"{MINER_URL}/cgi-bin/get_system_info.cgi"
    print(f"\n尝试访问: {url}")
    # get_system_info(url, USERNAME, PASSWORD)
    
    # 获取矿池信息
    url=f"{MINER_URL}/cgi-bin/miner_pools.cgi"
    print(f"\n尝试访问: {url}")
    # get_miner_pools(url, USERNAME, PASSWORD)

    # /cgi-bin/miner_summary.cgi
    url=f"{MINER_URL}/cgi-bin/miner_summary.cgi"
    print(f"\n尝试访问: {url}")
    # get_miner_summary(url, USERNAME, PASSWORD)    

    # 获取矿机配置 Miner General Configuration
    url=f"{MINER_URL}/cgi-bin/get_multi_option.cgi"   
    print(f"\n尝试访问: {url}")
    # get_Miner_General_Configuration(url, USERNAME, PASSWORD)

    # 下载日志
    # url=f"{MINER_URL}/log/antminer_log-2026-01-28.tar"
    url="http://172.50.75.69/cgi-bin/get_kernel_log.cgi?_=1773038648595"
    print(f"\n尝试访问: {url}")
    # download_logs(url, USERNAME, PASSWORD)

    # 设置矿机配置
    url=f"{MINER_URL}/cgi-bin/set_miner_conf.cgi"
    print(f"\n尝试访问: {url}")
    # set_miner_config(url, USERNAME, PASSWORD)

    # cgi-bin/miner_stats.cgi
    url=f"{MINER_URL}/cgi-bin/miner_stats.cgi" 
    print(f"\n尝试访问: {url}")
    # get_miner_stats(url, USERNAME, PASSWORD)

    # get_network_info.cgi
    url=f"{MINER_URL}/cgi-bin/get_network_info.cgi"
    print(f"\n尝试访问: {url}")
    get_network_info(url, USERNAME, PASSWORD)
