import requests
from requests.auth import HTTPDigestAuth
from requests.exceptions import RequestException
import urllib3
import pickle
import json

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

def get_pool_info(miner_url, username, password):
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
            print("JSON数据:", json.dumps(data, indent=4, ensure_ascii=False))
            
            print("状态：", data.get("STATUS").get("STATUS"))
            print("当前时间：", data.get("STATUS").get("when"))
            print("Msg：", data.get("STATUS").get("Msg"))
            print("api_version：", data.get("STATUS").get("api_version"))


            print("miner_version：", data.get("INFO").get("miner_version"))
            print("CompileTime：", data.get("INFO").get("CompileTime"))
            print("矿机型号：", data.get("INFO").get("type"))


            print("#"*30+"矿池0信息"+"#"*30)
            print("矿池0 编号:", data.get("POOLS")[0].get("index"))
            print("矿池0 url:", data.get("POOLS")[0].get("url"))
            print("矿池0 user:", data.get("POOLS")[0].get("user"))
            print("矿池0 pstatus:", data.get("POOLS")[0].get("status"))
            print("矿池0 priority:", data.get("POOLS")[0].get("priority"))
            print("矿池0 getworks:", data.get("POOLS")[0].get("getworks"))
            print("矿池0 accepted:", data.get("POOLS")[0].get("accepted"))
            print("矿池0 rejected:", data.get("POOLS")[0].get("rejected"))
            print("矿池0 discarded:", data.get("POOLS")[0].get("discarded"))
            print("矿池0 stale:", data.get("POOLS")[0].get("stale"))
            print("矿池0 diff:", data.get("POOLS")[0].get("diff"))
            print("矿池0 diff1:", data.get("POOLS")[0].get("diff1"))
            print("矿池0 diffa:", data.get("POOLS")[0].get("diffa"))
            print("矿池0 diffr:", data.get("POOLS")[0].get("diffr "))
            print("矿池0 diffs:", data.get("POOLS")[0].get("diffs"))
            print("矿池0 lsdiff:", data.get("POOLS")[0].get("lsdiff"))
            print("矿池0 lstime:", data.get("POOLS")[0].get("lstime"))

            print("#"*30+"矿池1信息"+"#"*30)
            print("矿池1 编号:", data.get("POOLS")[1].get("index"))
            print("矿池1 url:", data.get("POOLS")[1].get("url"))
            print("矿池1 user:", data.get("POOLS")[1].get("user"))
            print("矿池1 pstatus:", data.get("POOLS")[1].get("status"))
            print("矿池1 priority:", data.get("POOLS")[1].get("priority"))
            print("矿池1 getworks:", data.get("POOLS")[1].get("getworks"))
            print("矿池1 accepted:", data.get("POOLS")[1].get("accepted"))
            print("矿池1 rejected:", data.get("POOLS")[1].get("rejected"))
            print("矿池1 discarded:", data.get("POOLS")[1].get("discarded"))
            print("矿池1 stale:", data.get("POOLS")[1].get("stale"))
            print("矿池1 diff:", data.get("POOLS")[1].get("diff"))
            print("矿池1 diff1:", data.get("POOLS")[1].get("diff1"))
            print("矿池1 diffa:", data.get("POOLS")[1].get("diffa"))
            print("矿池1 diffr:", data.get("POOLS")[1].get("diffr "))
            print("矿池1 diffs:", data.get("POOLS")[1].get("diffs"))
            print("矿池1 lsdiff:", data.get("POOLS")[1].get("lsdiff"))
            print("矿池1 lstime:", data.get("POOLS")[1].get("lstime"))

            print("#"*30+"矿池2信息"+"#"*30)
            print("矿池2 编号:", data.get("POOLS")[2].get("index"))
            print("矿池2 url:", data.get("POOLS")[2].get("url"))
            print("矿池2 user:", data.get("POOLS")[2].get("user"))
            print("矿池2 pstatus:", data.get("POOLS")[2].get("status"))
            print("矿池2 priority:", data.get("POOLS")[2].get("priority"))
            print("矿池2 getworks:", data.get("POOLS")[2].get("getworks"))
            print("矿池2 accepted:", data.get("POOLS")[2].get("accepted"))
            print("矿池2 rejected:", data.get("POOLS")[2].get("rejected"))
            print("矿池2 discarded:", data.get("POOLS")[2].get("discarded"))
            print("矿池2 stale:", data.get("POOLS")[2].get("stale"))
            print("矿池2 diff:", data.get("POOLS")[2].get("diff"))
            print("矿池2 diff1:", data.get("POOLS")[2].get("diff1"))
            print("矿池2 diffa:", data.get("POOLS")[2].get("diffa"))
            print("矿池2 diffr:", data.get("POOLS")[2].get("diffr "))
            print("矿池2 diffs:", data.get("POOLS")[2].get("diffs"))
            print("矿池2 lsdiff:", data.get("POOLS")[2].get("lsdiff"))
            print("矿池2 lstime:", data.get("POOLS")[2].get("lstime"))

        except json.JSONDecodeError:
            print("响应内容不是有效的JSON格式")

# 使用示例
if __name__ == "__main__":
    # 配置你的矿机信息
    MINER_URL = "http://10.1.1.34"  # 替换为实际的矿机地址
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

# 如果还是失败，尝试其他可能的URL路径

    # 获取系统信息
    url=f"{MINER_URL}/cgi-bin/get_system_info.cgi"
    print(f"\n尝试访问: {url}")
    get_system_info(url, USERNAME, PASSWORD)
    
    # 获取矿池信息
    url=f"{MINER_URL}/cgi-bin/pools.cgi"
    print(f"\n尝试访问: {url}")
    get_pool_info(url, USERNAME, PASSWORD)
