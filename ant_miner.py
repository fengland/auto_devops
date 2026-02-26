import requests
from requests.auth import HTTPDigestAuth
from requests.exceptions import RequestException
import urllib3
import json
import pytz
from datetime import datetime
import time
import os

# 禁用SSL警告（如果使用HTTPS）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Miner:
    def __init__(self, miner_ipaddr, username, password):
        """
        初始化矿机对象
        
        Args:
            miner_ipaddr (str): 矿机IP地址
            username (str): 登录用户名
            password (str): 登录密码
            username (str): 登录用户名
            password (str): 登录密码
        """
        self.miner_ipaddr = miner_ipaddr
        self.miner_url = "http://" + miner_ipaddr  # 构建矿机URL
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.beijing_tz = pytz.timezone('Asia/Shanghai')
        
    def login_and_check_status(self, url=None):
        """
        使用Digest认证登录矿机管理界面并检查状态码
        
        Args:
            url (str, optional): 要访问的URL，默认为矿机URL
        
        Returns:
            tuple: (是否登录成功, 状态码, 响应内容)
        """
        target_url = url if url else self.miner_url
        
        try:
            # 使用Digest认证
            print(f"尝试使用Digest认证访问: {target_url}")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            }
            
            response = self.session.get(
                target_url,
                auth=HTTPDigestAuth(self.username, self.password),
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
    
    def get_system_info(self):
        """
        获取矿机系统信息
        
        Returns:
            dict: 包含系统信息的字典，如果失败则返回None
        """
        url = f"{self.miner_url}/cgi-bin/get_system_info.cgi"
        print(f"\n尝试访问: {url}")
        success, status_code, content = self.login_and_check_status(url)
        
        if success and content:
            try:
                data = json.loads(content)
                system_info = {
                    "minertype": data.get("minertype"),
                    "nettype": data.get("nettype", []),
                    "netdevice": data.get("netdevice"),
                    "macaddr": data.get("macaddr"),
                    "hostname": data.get("hostname"),
                    "ipaddress": data.get("ipaddress"),
                    "system_mode": data.get("system_mode"),
                    "system_kernel_version": data.get("system_kernel_version"),
                    "system_filesystem_version": data.get("system_filesystem_version"),
                    "firmware_type": data.get("firmware_type"),
                    "serinum": data.get("serinum")
                }
                
                # 打印系统信息
                print("矿机类型:", system_info["minertype"])
                print("网络类型:", system_info["nettype"])
                print("网络设备:", system_info["netdevice"])
                print("MAC地址:", system_info["macaddr"])
                print("主机名:", system_info["hostname"])
                print("IP地址:", system_info["ipaddress"])
                print("系统类型:", system_info["system_mode"])
                print("system_kernel_version:", system_info["system_kernel_version"])
                print("system_filesystem_version:", system_info["system_filesystem_version"])
                print("firmware_type:", system_info["firmware_type"])
                print("serinum:", system_info["serinum"])
                
                return system_info
            except json.JSONDecodeError:
                print("响应内容不是有效的JSON格式")
                return None
        else:
            print(f"获取系统信息失败，状态码: {status_code}")
            return None
    
    def get_pool_info(self):
        """
        获取矿池信息
        
        Returns:
            dict: 包含矿池信息的字典，如果失败则返回None
        """
        url = f"{self.miner_url}/cgi-bin/pools.cgi"
        print(f"\n尝试访问: {url}")
        success, status_code, content = self.login_and_check_status(url)
        
        if success and content:
            try:
                data = json.loads(content)
                pool_info = {
                    "STATUS": data.get("STATUS"),
                    "INFO": data.get("INFO"),
                    "POOLS": data.get("POOLS", [])
                }
                
                # 打印状态信息
                print("状态：", pool_info["STATUS"].get("STATUS"))
                utc_time = datetime.fromtimestamp(pool_info["STATUS"].get("when"), tz=pytz.utc)
                beijing_time = utc_time.astimezone(self.beijing_tz)
                print("当前时间：", pool_info["STATUS"].get("when"))
                print("UTC时间：", utc_time)
                print("北京时间：", beijing_time)
                print("Msg：", pool_info["STATUS"].get("Msg"))
                print("api_version：", pool_info["STATUS"].get("api_version"))
                
                # 打印矿机信息
                print("miner_version：", pool_info["INFO"].get("miner_version"))
                print("CompileTime：", pool_info["INFO"].get("CompileTime"))
                print("矿机型号：", pool_info["INFO"].get("type"))
                
                # 打印矿池信息
                for i, pool in enumerate(pool_info["POOLS"]):
                    print(f"{'#'*30}矿池{i}信息{'#'*30}")
                    print(f"矿池{i} 编号:", pool.get("index"))
                    print(f"矿池{i} url:", pool.get("url"))
                    print(f"矿池{i} user:", pool.get("user"))
                    print(f"矿池{i} pstatus:", pool.get("status"))
                    print(f"矿池{i} priority:", pool.get("priority"))
                    print(f"矿池{i} getworks:", pool.get("getworks"))
                    print(f"矿池{i} accepted:", pool.get("accepted"))
                    print(f"矿池{i} rejected:", pool.get("rejected"))
                    print(f"矿池{i} discarded:", pool.get("discarded"))
                    print(f"矿池{i} stale:", pool.get("stale"))
                    print(f"矿池{i} diff:", pool.get("diff"))
                    print(f"矿池{i} diff1:", pool.get("diff1"))
                    print(f"矿池{i} diffa:", pool.get("diffa"))
                    print(f"矿池{i} diffr:", pool.get("diffr "))
                    print(f"矿池{i} diffs:", pool.get("diffs"))
                    print(f"矿池{i} lsdiff:", pool.get("lsdiff"))
                    print(f"矿池{i} lstime:", pool.get("lstime"))
                
                return pool_info
            except json.JSONDecodeError:
                print("响应内容不是有效的JSON格式")
                return None
        else:
            print(f"获取矿池信息失败，状态码: {status_code}")
            return None
    
    def get_miner_config(self):
        """
        获取矿机配置
        
        Returns:
            dict: 包含矿机配置的字典，如果失败则返回None
        """
        url = f"{self.miner_url}/cgi-bin/get_miner_conf.cgi"
        print(f"\n尝试访问: {url}")
        success, status_code, content = self.login_and_check_status(url)
        
        if success and content:
            try:
                data = json.loads(content)
                miner_config = {
                    "bitmain-work-mode": data.get("bitmain-work-mode"),
                    "bitmain-voltage": data.get("bitmain-voltage"),
                    "bitmain-ccdelay": data.get("bitmain-ccdelay"),
                    "bitmain-pwth": data.get("bitmain-pwth"),
                    "bitmain-ex-hashrate": data.get("bitmain-ex-hashrate"),
                    "pools": data.get("pools", [])
                }
                
                # 打印配置信息
                print("bitmain-work-mode：", miner_config["bitmain-work-mode"])
                print("bitmain-voltage：", miner_config["bitmain-voltage"])
                print("bitmain-ccdelay：", miner_config["bitmain-ccdelay"])
                print("bitmain-pwth：", miner_config["bitmain-pwth"])
                print("bitmain-ex-hashrate：", miner_config["bitmain-ex-hashrate"])
                
                # 打印矿池配置
                for i, pool in enumerate(miner_config["pools"]):
                    print(f"pool{i}-url：", pool.get("url"))
                    print(f"pool{i}-user：", pool.get("user"))
                    print(f"pool{i}-pass：", pool.get("pass"))
                
                return miner_config
            except json.JSONDecodeError:
                print("响应内容不是有效的JSON格式")
                return None
        else:
            print(f"获取矿机配置失败，状态码: {status_code}")
            return None
    
    def download_logs(self, log_date=None):
        """
        下载矿机日志
        
        Args:
            log_date (str, optional): 日志日期，格式为"YYYY-MM-DD"，默认为当前日期
        
        Returns:
            bool: 是否下载成功
        """
        if not log_date:
            log_date = time.strftime("%Y-%m-%d")
            
        url = f"{self.miner_url}/log/antminer_log-{log_date}.tar"
        print(f"\n尝试访问: {url}")
        success, status_code, content = self.login_and_check_status(url)
        
        if success and status_code == 200:
            host = self.miner_url.split('//')[-1].split('/')[0]  # 得到 "10.1.1.24"
            host_dashed = host.replace('.', '-')  # 得到 "10-1-1-24"
            filename = f"{host_dashed}-antminer_log-{log_date}.tar"
            
            # 如果文件已存在，先删除它
            try:
                if os.path.exists(filename):
                    os.remove(filename)
                    print(f"已删除旧文件: {filename}")
            except OSError as e:
                print(f"删除文件失败 {filename}: {e}")
            
            print(f"准备保存日志文件为: {filename}")
            try:
                # 将字符串编码为字节
                with open(filename, 'wb') as f:
                    f.write(content.encode('utf-8'))
                print(f"文件已成功保存为: {filename}")
                return True
            except Exception as e:
                print(f"文件保存失败: {e}")
                return False
        else:
            print(f"下载失败，状态码: {status_code}")
            return False
    
    def set_miner_config(self, config):
        """
        设置矿机配置
        
        Args:
            config (dict): 包含矿机配置的字典
        
        Returns:
            tuple: (是否设置成功, 状态码, 响应内容)
        """
        url = f"{self.miner_url}/cgi-bin/set_miner_conf.cgi"
        print(f"\n尝试访问: {url}")
        
        try:
            # 使用Digest认证
            print("尝试使用Digest认证...")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            }
            
            response = self.session.post(
                url,
                auth=HTTPDigestAuth(self.username, self.password),
                headers=headers,
                verify=False,
                json=config
            )
            
            print(response.text)
            
            if response.status_code == 200:
                print("配置设置成功！")
                return True, response.status_code, response.text
            else:
                print(f"配置设置失败，状态码: {response.status_code}")
                return False, response.status_code, response.text
                
        except RequestException as e:
            print(f"请求出错: {str(e)}")
            return False, None, None


# 使用示例
if __name__ == "__main__":
    # 配置你的矿机信息
    MINER_IPADDR= "10.1.1.24"  # 替换为实际的矿机地址
    USERNAME = "root"  # 矿机通常默认用户名是root
    PASSWORD = "root"  # 替换为实际密码
    
    # 创建矿机对象
    miner = Miner(MINER_IPADDR, USERNAME, PASSWORD)
    
    # 测试登录
    success, status_code, content = miner.login_and_check_status()
    print(f"登录状态: {success}, 状态码: {status_code}")
    
    if success:
        # 获取系统信息
        system_info = miner.get_system_info()
        
        # 获取矿池信息
        pool_info = miner.get_pool_info()
        
        # 获取矿机配置
        miner_config = miner.get_miner_config()
        
        # 下载日志
        # miner.download_logs("2026-01-28")
        
        # 设置矿机配置
        config = {
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
        # miner.set_miner_config(config)
