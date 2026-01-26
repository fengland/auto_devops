# 登录ant miner，并获取 参数
import requests
from requests.auth import HTTPDigestAuth
from requests.exceptions import RequestException
import urllib3
import pickle

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
        print("响应内容预览:", content[:500] if content else "无响应内容")
    else:
        print("登录失败")
        if content:
            print("错误响应:", content[:500])

    # 如果还是失败，尝试其他可能的URL路径
    if  1:
        print("\n尝试其他可能的API端点...")
        alternative_urls = [
            f"{MINER_URL}/cgi-bin/get_system_info.cgi",
            f"{MINER_URL}/cgi-bin/pools.cgi",
            f"{MINER_URL}/cgi-bin/warning.cgi"
        ]
        
        for url in alternative_urls:
            print(f"\n尝试访问: {url}")
            success, status_code, content = login_and_check_status(url, USERNAME, PASSWORD)
            print(success)
            print(f"状态码: {status_code}")
            print("响应内容预览:", content[:500] if content else "无响应内容")
            # if success:
            #     break
